import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main(args):
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    #prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    if not api_key:
        raise Exception("API Key not found")
    client = genai.Client(api_key=api_key)

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    response = client.models.generate_content(
            model='gemini-2.5-flash', contents=messages
        )
    usage = response.usage_metadata
    if not usage:
        raise Exception("No Usage Metadata present! API ERROR!")
    #print(f"Usage {usage}")
    #print(f"Usage metadata {response.usage_metadata}")
    print(args, args.verbose,args.user_prompt)
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {usage.prompt_token_count}")
        print(f"Response tokens: {usage.candidates_token_count}")
    print(response.text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Agent Vinod")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    main(args)
