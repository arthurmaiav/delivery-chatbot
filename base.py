import anthropic
import dotenv
import os
from helpers import *

dotenv.load_dotenv()
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)
model = "claude-3-5-sonnet-20240620"

def function():
    sys_prompt = f"""

    """
    user_prompt = f""""""

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
        response = message.content[0].text
        return response
    except anthropic.APIConnectionError as e:
        print("The server could not be reached! Error:", e.__cause__)
    except anthropic.RateLimitError as e:
        print("A 429 status code was received! Access limit reached.")
    except anthropic.APIStatusError as e:
        print(f"An error {e.status_code} was received. More information: {e.response}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")