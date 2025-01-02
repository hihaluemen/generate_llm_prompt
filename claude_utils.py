#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/12/30 16:22
# @Author  : hihaluemen
# @File    : claude_utils.py
# @Description :
import re
from llm_prompt import CLAUDE_META_PROMPT
import time, os
from llm import post_claude


# def extract_between_tags(tag: str, string: str, strip: bool = False) -> list[str]:
#     ext_list = re.findall(f"<{tag}>(.+?)</{tag}>", string, re.DOTALL)
#     if strip:
#         ext_list = [e.strip() for e in ext_list]
#     print("extract_between_tags...")
#     print("\n\n")
#     print(ext_list)
#     return ext_list


def extract_between_tags(tag: str, string: str, strip: bool = False) -> list[str]:
    # 如果在接近结尾处没有找到结束标签，就添加一个
    last_start = string.rfind(f"<{tag}>")
    if last_start != -1:
        last_end = string.rfind(f"</{tag}>")
        # 如果没有找到结束标签，或者结束标签在开始标签之前
        if last_end == -1 or last_end < last_start:
            string = string + f"</{tag}>"
    
    ext_list = re.findall(f"<{tag}>(.+?)</{tag}>", string, re.DOTALL)
    if strip:
        ext_list = [e.strip() for e in ext_list]
    
    return ext_list



def remove_empty_tags(text):
    return re.sub(r'<(\w+)></\1>$', '', text)


def extract_prompt(metaprompt_response):
    between_tags = extract_between_tags("Instructions", metaprompt_response)[0]
    return remove_empty_tags(remove_empty_tags(between_tags).strip()).strip()


def extract_variables(prompt):
    pattern = r'{([^}]+)}'
    variables = re.findall(pattern, prompt)
    return set(variables)


def pretty_print(message):
    print('\n\n'.join('\n'.join(line.strip() for line in re.findall(r'.{1,100}(?:\s+|$)', paragraph.strip('\n'))) for paragraph in re.split(r'\n\n+', message)))
    return '\n\n'.join('\n'.join(line.strip() for line in re.findall(r'.{1,100}(?:\s+|$)', paragraph.strip('\n'))) for paragraph in re.split(r'\n\n+', message))


def get_prompt_claude(task, varibable: list=[]):
    prompt = CLAUDE_META_PROMPT.replace("{{TASK}}", task)
    assistant_partial = "<Inputs>"

    variable_string = ""
    for variable in varibable:
        variable_string += "\n{" + variable.upper() + "}"

    if variable_string:
        assistant_partial += variable_string + "\n</Inputs><Instructions Structure>"

    messages_list = [
        {
            "role": "user",
            "content": prompt
        },
        {
            "role": "assistant",
            "content": assistant_partial
        }
    ]

    message = post_claude(message=messages_list)

    print(message)

    extracted_prompt_template = extract_prompt(message)
    variables = extract_variables(message)

    return pretty_print(extracted_prompt_template), str(variables)