from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv

client = OpenAI(base_url="https://api.deepseek.com/v1", api_key=os.getenv("DEEPSEEK_API_KEY"))

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)