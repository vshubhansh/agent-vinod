import os,sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt
from functions.call_functions import available_functions, call_function

def main(args):
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    #prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    if not api_key:
        raise Exception("API Key not found")
    client = genai.Client(api_key=api_key)

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    response = None
    final_response_text = None
    for _ in range(20):
        response = client.models.generate_content(
                model='gemini-2.5-flash', contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions],system_instruction=system_prompt)
            )
        candidates = response.candidates
        if candidates:
            for candidate in candidates:
                messages.append(candidate.content)
        usage = response.usage_metadata
        function_calls = response.function_calls

        if not usage:
            raise Exception("No Usage Metadata present! API ERROR!")
        #print(f"Usage {usage}")
        #print(f"Usage metadata {response.usage_metadata}")
        print(args, args.verbose,args.user_prompt)
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {usage.prompt_token_count}")
            print(f"Response tokens: {usage.candidates_token_count}")
        function_results = []
        if function_calls:
            for function_call in function_calls:
                #print(f"Calling function: {function_call.name}({function_call.args})")
                function_call_result = call_function(function_call,args.verbose)
                if len(function_call_result.parts) == 0:
                    raise Exception("Function Call failure, no parts in content response.")
                if not function_call_result.parts[0].function_response:
                    raise Exception("Function response is NoneType")
                if not function_call_result.parts[0].function_response.response:
                    raise Exception("Function call response is NoneType")
                function_results.append(function_call_result.parts[0])
                if args.verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
            messages.append(types.Content(role="user", parts=function_results))
        else:
            if response.text:
                print(response.text)
                final_response_text = response.text
            else:
                print(f"Model did not generate a function call or response")
            break
                
            
    if not final_response_text:
        sys.exit(1)
        
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Agent Vinod")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    main(args)
