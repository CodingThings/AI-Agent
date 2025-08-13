import os
from dotenv import load_dotenv
from google import genai
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():

    if len(sys.argv) < 2:
        print("No prompt provided\nUsage: main.py 'prompt' ")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Unknown arguments were provided\nUsage: main.py 'prompt'")
        sys.exit(1)
    elif len(sys.argv) == 2:
        response = client.models.generate_content(
            model='gemini-2.0-flash-001', 
            contents=sys.argv[1]
        )

    print(response.text)
    print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
    print("Response tokens: " + str(response.usage_metadata.candidates_token_count))


if __name__ == "__main__":
    main()
