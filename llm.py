from openai import OpenAI
from llm_prompt import META_PROMPT
import requests
import json

client = OpenAI(
    base_url="*****",
    api_key="sk-****"
)


def generate_prompt_openai(task_or_prompt: str):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": META_PROMPT,
            },
            {
                "role": "user",
                "content": "Task, Goal, or Current Prompt:\n" + task_or_prompt,
            },
        ],
    )

    return completion.choices[0].message.content


def post_claude(message, model='claude_sonnet'):

    pass


def generate_prompt_deespseek(task_or_prompt: str):
    instruction = """
    你是一位大模型提示词生成专家，请根据用户的需求编写一个智能助手的提示词，来指导大模型进行内容生成，要求：
    1. 以 Markdown 格式输出
    2. 贴合用户需求，描述智能助手的定位、能力、知识储备
    3. 提示词应清晰、精确、易于理解，在保持质量的同时，尽可能简洁
    4. 只输出提示词，不要输出多余解释
    """
    client = OpenAI(
        api_key="sk-****",
        base_url="****",
    )

    messages = [{"role": "system", "content": instruction},
                {"role": "user", "content": task_or_prompt}]

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        # response_format={
        #     'type': 'json_object'
        # }
    )

    print(response.choices[0].message.content)
    return response.choices[0].message.content