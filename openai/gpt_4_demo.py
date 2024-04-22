# 转发key的使用
import datetime
import os

from openai import OpenAI
client = OpenAI(
    base_url=os.environ.get('OPEN_AI_BASE_URL'), # 重点改这个
    api_key=os.environ.get('OPEN_AI_GPT4_API_KEY')
)

print(datetime.datetime.now())

response = client.chat.completions.create(
  model="gpt-4-1106-preview",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "你好"}
  ]
)

print(response.choices[0].message.content)

print(datetime.datetime.now())
