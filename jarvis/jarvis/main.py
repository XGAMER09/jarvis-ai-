
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

SKILLS = {
    "1": "Write an engaging YouTube video script with a strong hook.",
    "2": "Analyze and improve YouTube titles and thumbnail concepts.",
    "3": "Create a video editing plan from a transcript or brief.",
    "4": "Draft helpful YouTube comment replies.",
    "5": "Create a practical YouTube content calendar.",
    "6": "Suggest niche ideas and explain how to research outlier videos.",
    "7": "Analyze audience retention data provided by the user.",
    "8": "Turn a long-video transcript into YouTube Shorts ideas.",
    "9": "Suggest YouTube SEO titles, descriptions and keywords.",
    "10": "Generate YouTube chapters from a timestamped transcript.",
    "11": "Audit a channel using the information provided by the user.",
}


def main():
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    if not api_key:
        print("OPENAI_API_KEY is not configured.")
        print("Set it securely in your runtime environment.")
        return

    client = OpenAI(api_key=api_key)

    while True:
        print("\n===== JARVIS AI =====")
        for number, skill in SKILLS.items():
            print(f"{number}. {skill}")
        print("0. Exit")

        choice = input("\nChoose a skill (0-11): ").strip()

        if choice == "0":
            print("JARVIS signing off.")
            break

        if choice not in SKILLS:
            print("Please choose a number from 0 to 11.")
            continue

        request = input("Enter your topic or request: ").strip()
        if not request:
            print("Please enter a request.")
            continue

        prompt = (
            "You are JARVIS, a helpful YouTube growth assistant. "
            "Answer clearly and practically. Do not invent channel analytics. "
            f"\nSelected skill: {SKILLS[choice]}"
            f"\nUser request: {request}"
        )

        try:
            response = client.responses.create(
                model=model,
                input=prompt
            )
            print("\n===== JARVIS RESPONSE =====\n")
            print(response.output_text)
        except Exception as error:
            print(f"AI request failed: {error}")


if __name__ == "__main__":
    main()
    
