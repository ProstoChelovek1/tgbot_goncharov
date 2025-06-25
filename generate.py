from openai import AsyncOpenAI
from config import AI_TOKEN

# Подключение к боту

client = AsyncOpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=AI_TOKEN,
)

# Отправка боту запроса

async def ai_generate(text: str):
  completion = await client.chat.completions.create(
    model="deepseek/deepseek-r1-0528:free",
    messages=[
      {
        "role": "user",
        "content": text
      }
    ]
  )
  # На случай ошибки
  print(completion)
  # Отправка ответа
  return completion.choices[0].message.content
