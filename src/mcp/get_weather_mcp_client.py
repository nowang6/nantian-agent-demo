from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerHTTP
from dotenv import load_dotenv
import logfire
load_dotenv

logfire.configure()
logfire.instrument_pydantic_ai()



server = MCPServerHTTP(url='http://localhost:8000/sse')  

# 初始化 deepseek chat 模型的 agent
deepseek_agent = Agent(
    'deepseek:deepseek-chat',  # 使用 deepseek 的 chat 模型
    system_prompt='',  # 设置系统提示
    mcp_servers=[server]
)

async def main():
    async with deepseek_agent.run_mcp_servers():  
        result = await deepseek_agent.run('2025-04-09成都的天气如何？')
    print(result.data)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())