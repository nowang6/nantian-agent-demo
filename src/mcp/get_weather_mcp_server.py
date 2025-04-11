from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("weather")

@mcp.tool()
async def get_weather(location, date):
    """
    获取指定地点和日期的天气信息。
    :param location:要查询天气的地点，例如：北京、上海等
    :param date:要查询天气的日期，格式为YYYY-MM-DD
    :return: 天气信息
    """
    return f"在 {date}，{location} 的天气是晴天。"

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='sse')