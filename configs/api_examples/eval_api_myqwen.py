from mmengine.config import read_base
from opencompass.partitioners import NaivePartitioner
from opencompass.runners.local_api import LocalAPIRunner
from opencompass.tasks import OpenICLInferTask

from opencompass.models import OpenAI4Qwen

models = [
        dict(
            openai_api_base="http://localhost:9999/v1/chat/completions",
            type=OpenAI4Qwen,                             # 使用 OpenAI 模型
            model="qwen",
            max_seq_len=32768,                        # 最大输入长度
            # 以下参数为各类模型都有的参数
            abbr='legalbrain',                            # 模型简称
            key='EMPTY',                            # 模型简称
            run_cfg=dict(num_gpus=0),                # 资源需求（不需要 GPU）
            max_out_len=1024,                         # 最长生成长度
            batch_size=1,                            # 批次大小
            query_per_second=1,
            ),
        ]

with read_base():
    # from ..summarizers.groups.cmmlu import cmmlu_summary_groups
    # from ..datasets.cmmlu.cmmlu_gen import cmmlu_datasets
    # from ..datasets.needlebench.needlebench_32k.needlebench_single_32k import needlebench_zh_datasets
    # from ..summarizers.needlebench import needlebench_32k_summarizer as summarizer
    # from ..datasets.needlebench.needlebench_4k.needlebench_single_4k import needlebench_zh_datasets
    # from ..summarizers.needlebench import needlebench_4k_summarizer as summarizer
    from ..datasets.needlebench.needlebench_32k.needlebench_single_32k import needlebench_zh_datasets
    from ..summarizers.needlebench import needlebench_32k_summarizer as summarizer

# summarizer = dict(
#         summary_groups=sum([v for k, v in locals().items() if k.endswith("_summary_groups")], []),
#         )

# datasets = sum([v for k, v in locals().items() if ('datasets' in k)], [])

datasets = [
        #*ceval_datasets,
        # *cmmlu_datasets,
        *needlebench_zh_datasets
        ]

work_dir = "outputs/api_qwen/"
