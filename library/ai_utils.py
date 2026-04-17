import requests


def call_llm(prompt):
    url = "http://127.0.0.1:1234/v1/responses"

    data = {
        "model": "mistral-7b-instruct-v0.2",
        "input": prompt,
        "temperature": 0.7
    }

    try:
        response = requests.post(url, json=data)
        result = response.json()

        return result["output"][0]["content"][0]["text"].strip()

    except Exception as e:
        return f"LLM Error: {str(e)}"


# 🔥 SUMMARY
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


# 🔥 RECOMMENDATION
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
You are an intelligent AI book assistant.

Instructions:
- Answer clearly and naturally like a human
- If the user asks for a summary → give a concise 2-3 line summary
- If the user asks for recommendations → suggest 2-3 DIFFERENT books
- Give a short reason for each recommendation
- Do NOT repeat the same book
- Do NOT say "based on system analysis"

Context:
{context}

Question:
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