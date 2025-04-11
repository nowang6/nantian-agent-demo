from openai import OpenAI
from dotenv import load_dotenv
import os
import json
load_dotenv


# 定义一个函数，用于获取天气信息
def get_weather(location, date):
    """
    获取指定地点和日期的天气信息。
    :param location:要查询天气的地点，例如：北京、上海等
    :param date:要查询天气的日期，格式为YYYY-MM-DD
    :return: 天气信息
    """
    return f"在 {date}，{location} 的天气是晴天。"


# 定义函数描述，用于告知模型函数的参数和功能
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "获取指定地点和日期的天气信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "要查询天气的地点"
                    },
                    "date": {
                        "type": "string",
                        "description": "要查询天气的日期，格式为YYYY - MM - DD"
                    }
                },
                "required": [
                    "location",
                    "date"
                ],
                "additionalProperties": False
            },
            "strict": True
        }
    }
]

client = OpenAI(base_url="https://api.deepseek.com/v1", api_key=os.getenv("DEEPSEEK_API_KEY"))

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": ""},
        {"role": "user", "content": "2025-04-09成都的天气如何？"},
    ],
    tools=tools,
    stream=False
)


# content = response.choices[0].message.content
tool_calls = response.choices[0].message.tool_calls


name = tool_calls[0].function.name
function_arguments = tool_calls[0].function.arguments

arguments = json.loads(function_arguments)
location = arguments["location"]
date = arguments["date"]



if name == "get_weather":
    function = get_weather
    function_result=function(location=location,date=date)
    print (function_result)