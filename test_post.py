import requests


def test_openai_promptgen():
    url = "http://127.0.0.1:8200/api/v1/yj/promptgen/openai"
    data = {"task": "你是一个sql大师，可以根据各种情况生成sql语句，你有sql表的描述sql_description和用户对话历史以及当前的时间"}
    response = requests.post(url, json=data)
    print(response.json())


def test_claude_promptgen():
    url = "http://127.0.0.1:8200/api/v1/yj/promptgen/claude"
    data = {
        "task": "请全程中文回答。\n\n你是一个sql大师，可以根据各种情况生成sql语句，你有sql表的描述sql_description和用户对话历史以及当前的时间",
        "variable": ['']
    }
    response = requests.post(url, json=data)
    print(response.json())


def test_deepseek_promptgen():
    url = "http://127.0.0.1:8200/api/v1/yj/promptgen/deepseek"
    data = {
        "task": "我现在有供应商对某件产品的供应物料{suppliers_list}和供应商的名称{supplier_name}， 希望你能给出该供应商的一些描述信息；重点是供应商供应的物料类型的描述",
    }
    response = requests.post(url, json=data)
    print(response.json())


if __name__ == "__main__":
    # test_openai_promptgen()
    test_claude_promptgen()
    # test_deepseek_promptgen()
