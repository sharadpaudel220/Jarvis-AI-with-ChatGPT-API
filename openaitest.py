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

