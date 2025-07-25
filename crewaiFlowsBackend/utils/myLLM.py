# 导入标准库
import os
# 导入第三方库
from crewai import LLM
from dotenv import load_dotenv

load_dotenv()

# 模型全局参数配置  根据自己的实际情况进行调整
# openai模型相关配置 根据自己的实际情况进行调整
OPENAI_API_BASE = "https://api.openai.com/v1"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_CHAT_MODEL = "gpt-4o-mini"
# 非gpt大模型相关配置(oneapi方案 通义千问为例) 根据自己的实际情况进行调整
ONEAPI_API_BASE = "http://139.224.72.218:3000/v1"
ONEAPI_CHAT_API_KEY = "sk-0FxX9ncd0yXjTQF877Cc9dB6B2F44aD08d62805715821b85"
ONEAPI_CHAT_MODEL = "qwen-max"
# 本地大模型相关配置(Ollama方案 llama3.1:latest为例) 根据自己的实际情况进行调整
OLLAMA_API_BASE = "http://localhost:11434/v1"
OLLAMA_CHAT_API_KEY = "ollama"
OLLAMA_CHAT_MODEL = "llama3.1:latest"

# 定函数 模型初始化
def my_llm(llmType):
    if llmType == "oneapi":
        # 实例化一个oneapi客户端对象
        llm = LLM(
            base_url=ONEAPI_API_BASE,
            api_key=ONEAPI_CHAT_API_KEY,
            model=ONEAPI_CHAT_MODEL,  # 本次使用的模型
            temperature=0.7,  # 发散的程度
            # timeout=None,# 服务请求超时
            # max_retries=2,# 失败重试最大次数
        )
    elif llmType == "ollama":
        # 实例化一个LLM客户端对象
        os.environ["OPENAI_API_KEY"] = "NA"
        llm = LLM(
            base_url=OLLAMA_API_BASE,  # 请求的API服务地址
            api_key=OLLAMA_CHAT_API_KEY,  # API Key
            model=OLLAMA_CHAT_MODEL,  # 本次使用的模型
            temperature=0.7,  # 发散的程度
            # timeout=None,# 服务请求超时
            # max_retries=2,# 失败重试最大次数
        )
    else:
        # 实例化一个LLM客户端对象
        llm = LLM(
            base_url=OPENAI_API_BASE,  # 请求的API服务地址
            api_key=OPENAI_API_KEY,  # API Key
            model=OPENAI_CHAT_MODEL,  # 本次使用的模型
            # temperature=0.7,# 发散的程度，一般为0
            # timeout=None,# 服务请求超时
            # max_retries=2,# 失败重试最大次数
        )
    return llm
