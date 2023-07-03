# 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

import openai

# api_key = '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'
# openai.api_key = "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"
import openai

openai.api_key = "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"

PROMPT = """请从文章中抽取出所有的航空航天领域科学技术术语，以列表形式给出。\n
输出格式：\n
1. xxx \n
2. xxx \n
"""


def get_response(content, temperature=0.1, max_tokens=2400):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        temperature=0,
        top_p=0,
        # max_tokens=max_tokens,
        messages=[
            {"role": "system", "content": f"{PROMPT}"},
            {"role": "user", "content": f"{content}"}
        ]
    )
    print(completion)
    return completion.choices[0]['message']['content']


#
res = get_response(
    "这三种在设计、任型运载火箭驮上重返大气层前抛掉。上述文章涵盖的科学术语为：")
print(res)

#
