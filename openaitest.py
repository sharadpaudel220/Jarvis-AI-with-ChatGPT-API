import openai
import os
from config import apikey

openai.api_key = apikey
message=[
        {"role": "user", "content": "Hello, how are you?"}
    ]

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  # messages=[],
  messages=message,
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)

'''
{{
  "id": "chatcmpl-7g2zeSUdlhpJrZJiWWD3OUuQmh5E3",
  "object": "chat.completion",
  "created": 1690255638,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! I'm an AI, so I don't have feelings, but I'm here to help you. How can I assist you today?"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 13,
    "completion_tokens": 29,
    "total_tokens": 42
  }
}
'''