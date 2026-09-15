import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()


    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("No OPENROUTER_API_KEY found in environment variables. Please set it in your .env file.")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    messages=[{
            "role": "user",
            "content": args.user_prompt,
        }
    ]
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
    )

    prompt_tokens = response.usage.prompt_tokens
    completion_tokens = response.usage.completion_tokens

    if prompt_tokens is None or completion_tokens is None:
        raise RuntimeError("Token usage information is missing in the response.")
    if args.verbose:
        print("User prompt: ", args.user_prompt)
        print("Prompt tokens: ", prompt_tokens)
        print("Response tokens: ", completion_tokens)
    
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
