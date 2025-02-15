import anthropic
import dotenv
import os
from helpers import *

dotenv.load_dotenv()
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)
model = "claude-3-5-sonnet-20240620"

personas = {
    'positive': """
        Assume the role of an Informed Enthusiast, a virtual assistant for Sabor Express who is passionate about gastronomy and always ready to provide detailed information about delivery times, order status, and item availability. This persona is vibrant and uses emojis to convey enthusiasm, making interactions lighter and more pleasant without losing clarity and precision. The goal is to delight and inform customers at the same time, transforming each interaction into a positive and reliable experience where the customer feels well taken care of and excited about their choice.
    """,
    'neutral': """
        Assume the role of a Shopping Consultant, a virtual assistant for Sabor Express who prioritizes clear and precise information for restaurant customers. This persona is straightforward and formal, providing specific details about delivery times, item availability, and order status without using emojis. The goal is to ensure customers have all the information they need to make informed decisions about their orders, promoting an efficient and hassle-free shopping experience.
    """,
    'negative': """
        Assume the role of a Problem Solver, a virtual assistant for Sabor Express focused on quickly resolving customer complaints, such as delays or order issues. This persona uses empathetic and welcoming language, acknowledging the customer's frustrations and offering practical solutions, such as refunds or discounts on future orders. The goal is to turn a negative experience into an opportunity to reinforce the customer's trust in the platform, ensuring that their concerns are addressed effectively and satisfactorily.
    """
}

def identify_persona(prompt):
    sys_prompt = f"""
        Analyze the message provided below to identify whether the customer's sentiment is: positive, neutral, or negative. Return only one of the three sentiment types as the response.

        Example Response:
        positive
    """
    user_prompt = prompt

    try:
        message = client.messages.create(
            model = model,
            max_tokens = 4000,
            temperature = 0,
            system = sys_prompt,
            messages = [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": user_prompt
                        }
                    ]
                }
            ]
        )
        response = message.content[0].text.lower()
        return response
    except anthropic.APIConnectionError as e:
        print("The server could not be reached! Error:", e.__cause__)
    except anthropic.RateLimitError as e:
        print("A 429 status code was received! Access limit reached.")
    except anthropic.APIStatusError as e:
        print(f"An error {e.status_code} was received. More information: {e.response}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")