# JARVIS - 11 YouTube Skills

SKILLS = {
    "1": "Script Writing",
    "2": "Title and Thumbnail Ideas",
    "3": "Video Editing Plan",
    "4": "Comment Replies",
    "5": "Weekly Content Planning",
    "6": "Viral Video Research",
    "7": "Audience Retention Analysis",
    "8": "YouTube Shorts Ideas",
    "9": "YouTube SEO",
    "10": "Video Chapters",
    "11": "YouTube Channel Audit",
}


def run_jarvis():
    print("Welcome to JARVIS YouTube AI!")
    print("Choose a skill:\n")

    for number, skill in SKILLS.items():
        print(f"{number}. {skill}")

    choice = input("\nEnter skill number (1-11): ")

    if choice in SKILLS:
        print(f"\nSelected skill: {SKILLS[choice]}")
        print("This skill framework is ready for further development.")
    else:
        print("Invalid choice. Please enter a number from 1 to 11.")


if __name__ == "__main__":
    run_jarvis()
