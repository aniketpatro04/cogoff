import os
from google import genai
from dotenv import load_dotenv
from app.utils.logger import logger
from app.utils.retry import retry_llm
from app.config.settings import MODEL_NAME

load_dotenv()

client = genai.Client()


# Function to Generate Answer

@retry_llm
def generate_answer(question_text: str) -> str:

    prompt = f"You are helping in answering questions like a cognitive offloader. Keep the answers succint, clear and crisp and in farily simple language. Provide analogy and examples whenever possible. Answer the following question:\n{question_text}"

    # response = client.models.generate_content(
    #     model="gemini-2.5-flash",
    #     contents=prompt
    # )

    try:
        response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt)

        if not response.text:
            raise ValueError("Empty response from LLM") 
        
        return response.text.strip()

    except Exception as e:
        logger.error(f"LLM failed for question: {question_text} | Error: {e}")
        raise


if __name__ == "__main__":

    answer = generate_answer("What is Stochastic Gradient Descent?")
    print(answer)