#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import collections
import numpy as np
from math import ceil, floor
from abc import abstractmethod
from .sampler import IterableSampler, SequentialSampler, BatchSampler
from .fetcher import FETCHERS
from .base_dataloader import BaseDataLoader

def default_collate(batch):
    """Puts each data field into a pd frame with outer dimension batch size"""
    elem = batch[0]
    if isinstance(elem, collections.abc.Mapping):
        return {key: default_collate([d[key] for d in batch]) for key in elem}
    elif isinstance(elem, collections.abc.Sequence):
        batch = zip(*batch)
        return [default_collate(samples) for samples in batch]
    elif isinstance(elem, np.ndarray):
        try:
            return np.stack(batch)
        except:
            return batch
    else:
        return batch

class DefaultDataLoader(BaseDataLoader):
    """DefaultDataLoader

    """

    def __init__(self, dataset, batch_size=1, last_batch='rollover', collate_fn=None,
                 sampler=None, batch_sampler=None, num_workers=0, pin_memory=False,
                 shuffle=False, distributed=False):
        self.dataset = dataset
        self.last_batch = last_batch
        self.sampler = sampler
        self.batch_sampler = batch_sampler
        self.num_workers = num_workers
        self.pin_memory = pin_memory
        self.collate_fn = collate_fn
        self._batch_size = batch_size
        self.shuffle = shuffle
        self.distributed = distributed
        self.drop_last = False if last_batch == 'rollover' else True
        if self.collate_fn == None:
            self.collate_fn = default_collate

    def batch(self, batch_size, last_batch='rollover'):
        self._batch_size = batch_size
        self.last_batch = last_batch

    @property
    def dataloader(self):
        return self

    def __iter__(self):
        return self._generate_dataloader(
            self.dataset,
            batch_size=self.batch_size,
            last_batch=self.last_batch,
            collate_fn=self.collate_fn,
            sampler=self.sampler,
            batch_sampler=self.batch_sampler,
            num_workers=self.num_workers,
            pin_memory=self.pin_memory,
            shuffle=self.shuffle,
            distributed=self.distributed)

    def __len__(self):
        try:
            dataset_len = self.dataset.__len__()
        except (AttributeError, TypeError):
            dataset_len = 0
            for _ in self.dataset:
                dataset_len += 1
        except Exception:
            raise ValueError(f"{self.dataset} is invalid, {self.dataset}" \
                " does not support calculating the length of its dataloader")
        if self.drop_last == False:
            dataloader_len = ceil(dataset_len / self.batch_size)
        else:
            dataloader_len = floor(dataset_len / self.batch_size)
        return dataloader_len

    def _generate_dataloader(self, dataset, batch_size, last_batch, collate_fn, sampler,
                             batch_sampler, num_workers, pin_memory, shuffle, distributed):

        sampler = self._generate_sampler(dataset, distributed)
        self.batch_sampler = BatchSampler(sampler, batch_size, self.drop_last)
        self.fetcher = FETCHERS[self.dataset_type](dataset, collate_fn, self.drop_last, distributed)

        for batched_indices in self.batch_sampler:
            try:
                data = self.fetcher(batched_indices)
                yield data
            except StopIteration:
                return

    def _generate_sampler(self, dataset, distributed):
        if hasattr(dataset, "__getitem__"):
            self.dataset_type = 'index'
            return SequentialSampler(dataset, distributed)
        elif hasattr(dataset, "__iter__"):
            self.dataset_type = 'iter'
            return IterableSampler(dataset)
        else:
            raise ValueError("dataset type only support (index, iter)")
