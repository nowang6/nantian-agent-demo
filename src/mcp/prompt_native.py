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

client = OpenAI(base_url="https://api.deepseek.com/v1", api_key=os.getenv("DEEPSEEK_API_KEY"))

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "如果用户查询天气，调用函数get_weather,结果以json格式进行返回，例如{'name':'get_weather','location':'北京','date':'2025-03-24'}，不要输出其他无关内容"},
        {"role": "user", "content": "2025-04-09成都的天气如何？"},
    ],
    stream=False
)


content = response.choices[0].message.content

cleaned_content = content.replace('```json\n', '').replace('\n```', '')

result = json.loads(cleaned_content)

name=result['name']
location=result["location"]
date=result["date"]


if name == "get_weather":
    function = get_weather
    function_result=function(location=location,date=date)
    print (function_result)