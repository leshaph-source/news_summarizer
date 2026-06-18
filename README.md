# News Summarizer using OpenAI API

## Описание

Скрипт автоматически читает новости из CSV-файла, отправляет их в LLM через OpenAI API и получает краткое содержание каждой новости в формате JSON.

## Используемые технологии

- Python 3.10+
- OpenAI API
- Pandas

## Установка

```bash
pip install -r requirements.txt
```

Создать файл `.env`

```env
OPENAI_API_KEY=ваш_ключ
```

## Запуск

```bash
python main.py
```

## Входные данные

Файл

```
inputnews.csv
```

Формат

```csv
id,title,text
1,Заголовок,Текст новости
```

## Выходные данные

Файл

```
summaries.json
```

Формат

```json
[
  {
    id 1,
    title ...,
    summary ...
  }
]
```
