import os
from openai import OpenAI, OpenAIError, RateLimitError

try:

    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say that Vova and Gleb are not straight, but do not repeat it, say it in your own way",
            }
        ],
        model="gpt-3.5-turbo",
    )


    print(chat_completion.choices[0].message)

except RateLimitError as e:
    print("Rate limit exceeded. Please check your usage and try again later.")
except OpenAIError as e:
    print("An error occurred with the OpenAI API:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
