from llm import generate_prompt_openai


def test1():
    task = "你是一个sql大师，可以根据各种情况生成sql语句，你有sql表的描述sql_description和用户对话历史以及当前的时间"
    new_prompt = generate_prompt_openai(task)
    print(new_prompt)


if __name__ == '__main__':
    test1()