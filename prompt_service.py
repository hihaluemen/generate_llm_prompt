from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from llm import generate_prompt_openai, generate_prompt_deespseek
from claude_utils import get_prompt_claude

app = FastAPI()

# 添加CORS支持
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PromptGenRequest(BaseModel):
    task: str
    variable: list = ['']


# 注意：API路由需要在静态文件挂载之前定义
@app.post("/api/v1/yj/promptgen/openai")
async def gen_openai_prompt(inputData: PromptGenRequest):
    gen_prompt = generate_prompt_openai(inputData.task)
    return {"prompt": gen_prompt}


@app.post("/api/v1/yj/promptgen/claude")
async def gen_claude_prompt(inputData: PromptGenRequest):
    gen_prompt = get_prompt_claude(task=inputData.task, varibable=inputData.variable)
    return {"prompt": gen_prompt[0]}


@app.post("/api/v1/yj/promptgen/deepseek")
async def gen_openai_prompt(inputData: PromptGenRequest):
    gen_prompt = generate_prompt_deespseek(inputData.task)
    return {"prompt": gen_prompt}


# 静态文件挂载放在最后
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run("prompt_service:app", host="0.0.0.0", port=8200, workers=1, log_level="info")
