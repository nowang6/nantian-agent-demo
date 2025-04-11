from transformers import AutoTokenizer

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "2025-04-09成都的天气如何?"},
    {
        "role": "assistant",
        "content": "",
        "tool_calls": [
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "arguments": '{ "location": "成都", "date":"2025-04-09" }'
                }
            }
        ]
    },
    {
        "role": "tool",
        "content": '{ "在 2025-04-09，成都的天气是晴天。" }',
        "tool_call_id": "call_1"
    },
    {
        "role": "assistant",
        "content": "成都的天气是晴天"
    }
]

tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-V3-0324")
print(tokenizer.apply_chat_template(messages, tokenize=False))