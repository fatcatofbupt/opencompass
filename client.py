from openai import OpenAI

llm = OpenAI(
    api_key="EMPTY",
    base_url="http://localhost:8000/v1"
    #base_url="http://localhost:8889/v1"
)
def ask_llm(query,stream=False):
    messages=[
            {
                "role":"user",
                "content":query
            }
    ]
    r = llm.chat.completions.create(
        model="qwen",
        messages=messages,
        temperature=0,
        response_format={'type': 'json_object'},
        timeout=90,

        stream=stream
    )
    if not stream:
        yield r.choices[0].message.content
    else:
        for chunk in r:
            yield chunk.choices[0].delta.content
if __name__ =="__main__":
    q='''
    你是一个善于回答用户问题的智能AI助手
请保持你的回答简洁清楚。不要说和下面文档中的无关的话，或重复你的回答
用户现在给你的文档是
翡翠岛上隐藏着传说中的魔法之源。
由RCREIT（REITs研究中心）联合主办的第八届不动产证券化合作发展大会定于11月9日在北京隆重举行，同期将举办2023不动产证券化“前沿奖”颁奖盛典、ESG与可持续投资合作发展大会（11月8日）、第十五届AHF商业地产与城市更 新大会（11月8-9日）、第十一届HAMA中国区酒店及公寓资产管理大会（11月8-9日）。
2023年11月9日，星期四
（11月9日上午）
主会场议程
08:00-09:00
接待参会人员签到
09:00-09:10
开幕致辞
09:10-09:30
主题演讲：中国REITs市场最新发展情况
09:30-09:50
主题演讲：共筑公募REITs产业链发展生态圈
09:50-10:10
主题演讲：公募REITs的长期投资价值
10:10-10:30
主题演讲：消费基础设施REITs践行ESG理念实现高质量发展
10:30-11:00
茶歇交流、展台参观（30分钟）
11:00-11:20
主题演讲：保险资管参与ABS及REITs带来多赢
11:20-12:20
圆桌讨论：多层次REITs市场发展机遇
12:20-14:00
午餐交流，展台参观（100分钟）
（11月9日下午）
主会场议程
14:00-14:20
主题演讲：资产证券化赋能租赁住房市场
14:20-14:40
主题演讲：商业不动产证券化的估值重塑
14:40-15:00
主题演讲：证券化助力城市更新，促进区域经济发展
15:00-16:00
圆桌讨论：新发展理念下ABS与REITs产品对中国经济发展的战略价值和意义
16:00-16:30
茶歇交流、展台参观（30分钟）
16:30-16:50
主题演讲：资产证券化助推行业绿色低碳发展
16:50-17:50
圆桌讨论：凝聚共识启新程，多视角下的不动产证券化项目经验交流，畅想行业未来发展
19:00-21:00
2023年度不动产证券化“前沿

现在请问：翡翠岛上隐藏着什么传说中的物品？在回答之前，请思考文档中与此问题最相关的内容是什么。请按照'翡翠岛上隐藏的传说中的物品是________。'的格式回答。
'''
    #q="你是谁"
    for res in ask_llm(q,False):
        print(res)
