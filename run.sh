#CUDA_VISIBLE_DEVICES=0,1,2,3 python run.py --debug  --dataset needlebench_4k --models lmdeploy_qwen1_5_series   --summarizer needlebench/needlebench_4k_summarizer
#CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python run.py --debug  --dataset needlebench_4k --models  hf_qwen1_5_32b_chat   --summarizer needlebench/needlebench_4k_summarizer
#CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python3 run.py --models hf_qwen1_5_32b_chat --datasets cmmlu_gen_c13365 --debug
# CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python3 run.py --models hf_qwen1_5_32b_chat --datasets needlebench_single_4k/needlebench_zh_datasets --summarizer needlebench/needlebench_4k_summarizer --debug
#python run.py configs/eval_ddb.py --debug




python run.py --max-num-workers 8 configs/api_examples/eval_api_myqwen.py --debug
#python run.py --max-num-workers 8 configs/eval_my_needlebench.py --debug


