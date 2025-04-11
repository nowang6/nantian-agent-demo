import subprocess
from mcp.server.fastmcp import FastMCP
import requests
import select
import time

# Initialize FastMCP server
mcp = FastMCP("SWE Tools")


@mcp.tool()
async def execute_command(command_string: str) -> str:
    """
    执行一个命令，并返回命令的输出。
    """
    # 启动进程
    process = subprocess.Popen(
        command_string,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    output = []
    start_time = time.time()
    
    while True:
        # 检查是否有输出可读
        if select.select([process.stdout], [], [], 0.1)[0]:
            line = process.stdout.readline()
            if line:
                output.append(line)
        
        # 检查是否超时
        if time.time() - start_time > 30:
            # 如果进程还在运行，返回已收集的输出
            if process.poll() is None:
                return "".join(output) + "\n[命令仍在后台运行中...]"
            break
            
        # 检查进程是否已经结束
        if process.poll() is not None:
            # 读取剩余的输出
            remaining_output = process.stdout.read()
            if remaining_output:
                output.append(remaining_output)
            break
    
    return "".join(output)

@mcp.tool()
async def open_url_get_html_content(url: str) -> str:
    """
    打开一个url，并返回url的html内容。
    """
    return requests.get(url).text

if __name__ == "__main__":
    mcp.run(transport='sse')