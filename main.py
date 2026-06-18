import os
import json
import pandas as pd

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

news = pd.read_csv("input/news.csv")

results = []

for index, row in news.iterrows():

    prompt = f"""
Сделай краткое содержание новости(до 3 предложений).

Заголовок:
{row['title']}

Текст:
{row['text']}

Верни только JSON:

{{
  "summary": "..."
}}
"""

    response = client.chat.completions.create(
        model="openrouter/auto",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    answer = response.choices[0].message.content

    try:
        summary = json.loads(answer)["summary"]
    except:
        summary = answer

    results.append({
        "id": index + 1,
        "title": row["title"],
        "summary": summary
    })

with open(
    "output/summaries.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        results,
        f,
        ensure_ascii=False,
        indent=4
    )

print("Готово!")