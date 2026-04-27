import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()


# Function to Generate Answer
def generate_answer(question_text: str) -> str:

    prompt = f"You are helping in answering questions like a cognitive offloader. Keep the answers succint, clear and crisp and in farily simple language. Provide analogy and examples whenever possible. Answer the following question:\n{question_text}"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()


if __name__ == "__main__":

    answer = generate_answer("What is Hawking Radiation?")
    print(answer)