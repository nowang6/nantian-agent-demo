from dotenv import load_dotenv
import os
load_dotenv()
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerHTTP
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
import logfire

logfire.configure()
logfire.instrument_pydantic_ai()



server = MCPServerHTTP(url='http://localhost:8000/sse')  

model = OpenAIModel('deepseek-chat', provider=OpenAIProvider(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url='http://api.deepseek.com/v1'))

# 初始化 deepseek chat 模型的 agent
deepseek_agent = Agent(
    'deepseek:deepseek-chat',  
    #model=model,
    system_prompt=('You are Nantian AI Coder, a highly skilled software engineer with extensive knowledge in many programming languages, frameworks, design patterns, and best practices\n'
                   'You can use tools to accomplish a given task, tools have defined input schemas that specify required and optional parameters.\n'
                   ),  # 设置系统提示
    mcp_servers=[server]
)

async def main():
    async with deepseek_agent.run_mcp_servers():  
        result = await deepseek_agent.run("使用前端react框架，生成一个hello world项目, 并且测试是否能正常访问")
    print(result.data)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())