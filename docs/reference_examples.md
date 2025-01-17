Reference Examples
===
## Validated Models
<table>
<thead>
  <tr>
    <th rowspan="2">Model</th>
    <th colspan="3">Accuracy</th>
    <th colspan="3">Performance</th>
  </tr>
  <tr>
    <th>INT8</th>
    <th>FP32</th>
    <th>Acc Ratio[(INT8-FP32)/FP32]</th>
    <th>INT8</th>
    <th>FP32</th>
    <th>Performance Ratio[INT8/FP32]</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-7zrl"><a href="../examples/baremetal/nlp/squad/bert_large">bert_large_squad_static</a>
    <td class="tg-7zrl">90.78%</td>
    <td class="tg-7zrl">90.87%</td>
    <td align="center">-0.11%</td>
    <td class="tg-7zrl">49.08</td>
    <td class="tg-7zrl">13.48</td>
    <td align="center">3.64x</td>
  </tr>
  <tr>
    <td class="tg-7zrl"><a href="../examples/baremetal/nlp/mrpc/bert_base">bert_base_mrpc_static</a>
    <td class="tg-7zrl">82.35%</td>
    <td class="tg-7zrl">83.09%</td>
    <td align="center">-0.89%</td>
    <td class="tg-7zrl">497.28</td>
    <td class="tg-7zrl">151.16</td>
    <td align="center">3.29x</td>
  </tr>
  <tr>
    <td class="tg-7zrl"><a href="../examples/baremetal/nlp/stsb/bert_base_nli_mean_tokens">bert_base_nli_mean_tokens_stsb_static</a>
    <td class="tg-7zrl">89.23%</td>
    <td class="tg-7zrl">89.55%</td>
    <td align="center">-0.36%</td>
    <td class="tg-7zrl">546.97</td>
    <td class="tg-7zrl">151.77</td>
    <td align="center">3.60x</td>
  </tr>
  <tr>
    <td class="tg-7zrl"><a href="../examples/baremetal/nlp/mrpc/bert_base_sparse">bert_base_sparse_mrpc_static</a>
    <td class="tg-7zrl">70.59%</td>
    <td class="tg-7zrl">70.59%</td>
    <td align="center">0.00%</td>
    <td class="tg-7zrl">551.90</td>
    <td class="tg-7zrl">153.80</td>
    <td align="center">3.59x</td>
  </tr>
  <tr>
    <td class="tg-7zrl"><a href="../examples/baremetal/nlp/mrpc/bert_mini">bert_mini_mrpc_static</a>
    <td class="tg-7zrl">78.19%</td>
    <td class="tg-7zrl">78.68%</td>
    <td align="center">-0.62%</td>
    <td class="tg-7zrl">6962.58</td>
    <td class="tg-7zrl">3252.14</td>
    <td align="center">2.14x</td>
  </tr>
  <tr>
    <td class="tg-7zrl"><a href="../examples/baremetal/nlp/sst2/bert_mini">bert_mini_sst2_static</a>
    <td class="tg-7zrl">87.16%</td>
    <td class="tg-7zrl">86.93%</td>
    <td align="center">0.26%</td>
    <td class="tg-7zrl">6850.38</td>
    <td class="tg-7zrl">3218.98</td>
    <td align="center">2.13x</td>
  </tr>
  <tr>
    <td class="tg-7zrl"><a href="../examples/baremetal/nlp/sst2/distilbert_base_uncased">distilbert_base_uncased_sst2_static</a>
    <td class="tg-7zrl">90.14%</td>
    <td class="tg-7zrl">90.25%</td>
    <td align="center">-0.12%</td>
    <td class="tg-7zrl">1086.13</td>
    <td class="tg-7zrl">306.45</td>
    <td align="center">3.54x</td>
  </tr>
  <tr>
    <td class="tg-7zrl"><a href="../examples/baremetal/nlp/mrpc/distilbert_base_uncased">distilbert_base_uncased_mrpc_static</a>
    <td class="tg-7zrl">83.82%</td>
    <td class="tg-7zrl">84.07%</td>
    <td align="center">-0.30%</td>
    <td class="tg-7zrl">1091.99</td>
    <td class="tg-7zrl">303.92</td>
    <td align="center">3.59x</td>
  </tr>
  <tr>
    <td class="tg-7zrl"><a href="../examples/baremetal/nlp/emotion/distilbert_base_uncased">distilbert_base_uncased_emotion_static</a>
    <td class="tg-7zrl">93.90%</td>
    <td class="tg-7zrl">94.20%</td>
    <td align="center">-0.32%</td>
    <td class="tg-7zrl">1081.35</td>
    <td class="tg-7zrl">306.33</td>
    <td align="center">3.53x</td>
  </tr>
  <tr>
    <td class="tg-7zrl"><a href="../examples/baremetal/nlp/sst2/minilm_l6_h384_uncased">minilm_l6_h384_uncased_sst2_static</a>
    <td class="tg-7zrl">89.33%</td>
    <td class="tg-7zrl">90.14%</td>
    <td align="center">-0.90%</td>
    <td class="tg-7zrl">2594.77</td>
    <td class="tg-7zrl">1083.84</td>
    <td align="center">2.39x</td>
  </tr>
  <tr>
    <td class="tg-7zrl"><a href="../examples/baremetal/nlp/mrpc/roberta_base">roberta_base_mrpc_static</a>
    <td class="tg-7zrl">88.24%</td>
    <td class="tg-7zrl">88.97%</td>
    <td align="center">-0.82%</td>
    <td class="tg-7zrl">508.14</td>
    <td class="tg-7zrl">153.37</td>
    <td align="center">3.31x</td>
  </tr>
  <tr>
    <td class="tg-7zrl"><a href="../examples/baremetal/nlp/wnli/distilroberta_base">distilroberta_base_wnli_static</a>
    <td class="tg-7zrl">56.34%</td>
    <td class="tg-7zrl">56.34%</td>
    <td align="center">0.00%</td>
    <td class="tg-7zrl">1097.22</td>
    <td class="tg-7zrl">315.94</td>
    <td align="center">3.47x</td>
  </tr>
  <tr>
    <td class="tg-7zrl"><a href="../examples/baremetal/nlp/stsb/paraphrase_xlm_r_multilingual_v1">paraphrase_xlm_r_multilingual_v1_stsb_static</a>
    <td class="tg-7zrl">86.66%</td>
    <td class="tg-7zrl">87.23%</td>
    <td align="center">-0.65%</td>
    <td class="tg-7zrl">552.44</td>
    <td class="tg-7zrl">153.74</td>
    <td align="center">3.59x</td>
  </tr>
  <tr>
    <td class="tg-7zrl"><a href="../examples/baremetal/nlp/financial_phrasebank/finbert">finbert_financial_phrasebank_static</a>
    <td class="tg-7zrl">82.57%</td>
    <td class="tg-7zrl">82.80%</td>
    <td align="center">-0.28%</td>
    <td class="tg-7zrl">999.94</td>
    <td class="tg-7zrl">292.55</td>
    <td align="center">3.42x</td>
  </tr>
</tbody>
</table>
Note: measured by batch size 1, 4 cores/instance, 10 instances on 1 socket of Intel Xeon Platinum 8380 Scalable processor
