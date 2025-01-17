#!/bin/bash
set -x

function main {

  init_params "$@"
  run_tuning

}

# init params
function init_params {

  for var in "$@"
  do
    case $var in
      --topology=*)
          topology=$(echo $var |cut -f2 -d=)
      ;;
      --dataset_location=*)
          dataset_location=$(echo $var |cut -f2 -d=)
      ;;
      --input_model=*)
          input_model_prefix=$(echo $var |cut -f2 -d=)
      ;;
      --output_model=*)
          output_model=$(echo $var |cut -f2 -d=)
      ;;
      *)
          echo "Error: No such parameter: ${var}"
          exit 1
      ;;
    esac
  done

}

# run_tuning
function run_tuning {
    extra_cmd='--rgb-mean=123.68,116.779,103.939 --rgb-std=58.393,57.12,57.375'
    batch_size=64
    num_inference_batches=100
    dataset=${dataset_location}
    ctx='cpu'
    symbol_file=${input_model_prefix}/${topology}"-symbol.json"
    param_file=${input_model_prefix}/${topology}"-0000.params"

    if [ "${topology}" = "inceptionv3" ]; then
        extra_cmd="${extra_cmd} --image-shape=3,299,299"
    fi
    if [ "$(basename "$dataset" )" = "val_256_q90.rec" ]; then
        python -u prepare_dataset.py --dataset_location="$(dirname "$dataset")"
    fi
    python -u imagenet_inference.py \
            --symbol-file=${symbol_file} \
            --param-file=${param_file} \
            --batch-size=${batch_size} \
            --num-inference-batches=${num_inference_batches} \
            --dataset=${dataset} \
            --ctx=${ctx} \
            --output-graph=${output_model} \
            ${extra_cmd}

}

main "$@"
