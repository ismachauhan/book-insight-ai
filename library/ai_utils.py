import requests


def call_llm(prompt):
    url = "http://127.0.0.1:1234/v1/responses"

    data = {
        "model": "mistral-7b-instruct-v0.2",
        "input": prompt,
        "temperature": 0.5
    }

    try:
        response = requests.post(url, json=data, timeout=120)
        result = response.json()

        if "output" in result and len(result["output"]) > 0:
            content = result["output"][0]["content"]

            for item in content:
                if item.get("type") == "output_text":
                    return item.get("text", "").strip()

        return "LLM Error: No valid text found"

    except Exception as e:
        return f"LLM Error: {str(e)}"
 


def generate_summary(description):
    if not description:
        return "No description available"

    prompt = f"""
Summarize the following book description in 2-3 clear and simple lines.

Do not add extra information.

Description:
{description}
"""
    return call_llm(prompt)


def recommend_book(title, description):
    prompt = f"""
A user likes this book:

Title: {title}
Description: {description}

Suggest 2 DIFFERENT books (not the same book).

Rules:
- Do NOT repeat the same book
- Give only book suggestions with short reason
- Keep answer short
"""
    return call_llm(prompt)


def generate_answer(query, context):
    prompt = f"""
You are a helpful assistant for a book recommendation website.

Your job:
- Recommend books from the given context
- Try your best to match the user's intent
- Even if it's not exact, suggest the closest books

Rules:
- Do NOT say "I cannot recommend"
- Always suggest 2 books from context
- Keep it simple and friendly

Format:

Book 1:
Title: ...
Why you might like it: ...

Book 2:
Title: ...
Why you might like it: ...

Context:
{context}

User query:
{query}

Answer:
"""
    return call_llm(prompt)

def classify_genre(title, description):
    prompt = f"""
Identify the genre of this book.

Title: {title}
Description: {description}

Rules:
- Return ONLY ONE word genre
- Examples: Fiction, Romance, Mystery, Sci-Fi, History

Genre:
"""
    return call_llm(prompt)