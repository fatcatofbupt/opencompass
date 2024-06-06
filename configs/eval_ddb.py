from opencompass.models import LocalQwen
from mmengine.config import read_base
from opencompass.partitioners import NaivePartitioner
from opencompass.runners.local_api import LocalAPIRunner
from opencompass.tasks import OpenICLInferTask

with read_base():
    # from .summarizers.medium import summarizer
    # from .datasets.cmmlu.cmmlu_gen import cmmlu_datasets
    

    from .datasets.needlebench.needlebench_4k.needlebench_single_4k import needlebench_zh_datasets
    # from .datasets.needlebench.needlebench_4k.needlebench_single_4k import needlebench_zh_datasets, needlebench_en_datasets
    from .summarizers.needlebench import needlebench_4k_summarizer as summarizer


datasets = [
    *needlebench_zh_datasets
    # *cmmlu_datasets,
    # *bbh_datasets,
    # *humaneval_datasets,
    # *mbpp_datasets,
    # *math_datasets,
    # *gsm8k_datasets,
    # *iwslt2017_datasets,
]

 
ip = 'localhost'
port = 8889
models = [
    dict(
        type=LocalQwen,                             # 使用 OpenAI 模型
        # 以下为 `OpenAI` 初始化参数
        path='qwen',                            # 指定模型类型
        # openai_api_base = f"http://{ip}:{port}/v1/chat/completions",
        # key='EMPTY',                   # OpenAI API Key
        # max_seq_len=32768,                        # 最大输入长度
        # # mode = 'rear',
        # retry = 10,
        # # 以下参数为各类模型都有的参数，非 `OpenAI` 的初始化参数
        # abbr='qwen1.5-32b-chat',                            # 模型简称
        # run_cfg=dict(num_gpus=0),                # 资源需求（不需要 GPU）
        # max_out_len=2048,                         # 最长生成长度
        batch_size=1,                            # 批次大小
        # temperature = 0,
        # meta_template = api_meta_template
    ),
]

infer = dict(
    partitioner=dict(type=NaivePartitioner),
    runner=dict(
        type=LocalAPIRunner,
        max_num_workers=1,
        concurrent_users=1,
        task=dict(type=OpenICLInferTask)),
)

# work_dir ='./output/api_360GPT_S2_V9'


work_dir = "outputs/ddb/"