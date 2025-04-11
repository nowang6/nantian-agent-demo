from dotenv import load_dotenv
import os
load_dotenv()
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerHTTP
from pydantic_ai import Agent, RunContext
import logfire
from dataclasses import dataclass

logfire.configure()
logfire.instrument_pydantic_ai()

@dataclass
class SupportDependencies:  
    task_id: int

server = MCPServerHTTP(url='http://localhost:8000/sse')  

# model = OpenAIModel('deepseek-chat', provider=OpenAIProvider(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url='http://api.deepseek.com/v1'))

# 初始化 deepseek chat 模型的 agent
agent = Agent(
    'deepseek:deepseek-chat',  
    #model=model,
    system_prompt='#角色\n你是南天AI编程助手——一位精通多种编程语言、框架、设计模式及最佳实践的高级软件工程师\n',  # 设置系统提示
    mcp_servers=[server]
)

@agent.system_prompt
def add_objective(ctx: RunContext[SupportDependencies]) -> str:
    return f"""#目标\n
你通过迭代方式完成给定任务，将其拆解为清晰的步骤并系统化执行。
- 分析任务并设定目标：分析用户任务，设定明确、可实现的子目标，并按逻辑顺序确定优先级。
- 逐步执行目标：按顺序完成每个子目标，必要时逐一调用可用工具。每个目标对应问题解决流程中的一个独立步骤。执行过程中，你将实时获知已完成和剩余的工作内容。
- 工具调用原则：你拥有强大的工具调用能力，可灵活运用多种工具实现各项目标。工具需严格遵循预定义的输入规范，其中明确标注必选和可选参数。
"""



async def main():
    async with agent.run_mcp_servers():  
        result = await agent.run("使用前端react框架，生成一个hello world项目, 并且测试是否能正常访问")
    print(result.data)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())