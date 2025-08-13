import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():

    messages = []
    verbose = False

    if len(sys.argv) < 2:
        print("No prompt provided\nUsage: main.py 'prompt' [--verbose]")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Unknown arguments were provided\nUsage: main.py 'prompt' [--verbose]")
        sys.exit(1)
    elif len(sys.argv) == 2:
        messages.append(types.Content(role="user", parts=[types.Part(text=sys.argv[1])]))
    elif len(sys.argv) == 3:
        if sys.argv[2] == "--verbose":
            verbose = True
            messages.append(types.Content(role="user", parts=[types.Part(text=sys.argv[1])]))
        else:
            print("Unknown arguments were provided\nUsage: main.py 'prompt' [--verbose]")
            sys.exit(1)

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
    )

    print(response.text)
    if verbose:
        print("User prompt: " + sys.argv[1])
        print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
        print("Response tokens: " + str(response.usage_metadata.candidates_token_count))


if __name__ == "__main__":
    main()
