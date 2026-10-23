
"""
JARVIS AI - YouTube Assistant
Main command center for 11 YouTube skills.
"""

SKILLS = {
    "1": ("Script Writer", "Create engaging video scripts"),
    "2": ("Title and Thumbnail Analyzer", "Improve video packaging"),
    "3": ("Video Editing Assistant", "Create editing suggestions"),
    "4": ("Comment Manager", "Draft comment replies"),
    "5": ("Content Planner", "Plan weekly content"),
    "6": ("Viral Topic Researcher", "Explore video ideas"),
    "7": ("Retention Analyzer", "Analyze audience retention"),
    "8": ("Shorts Finder", "Find Shorts ideas from long videos"),
    "9": ("YouTube SEO", "Suggest titles and keywords"),
    "10": ("Chapter Generator", "Create video chapters"),
    "11": ("Channel Auditor", "Review channel improvement areas"),
}


def show_menu():
    print("\n===== JARVIS AI =====")
    print("Your Personal YouTube Assistant\n")

    for number, (name, description) in SKILLS.items():
        print(f"{number}. {name} - {description}")

    print("0. Exit")


def run_skill(number):
    name, description = SKILLS[number]

    print(f"\nSelected: {name}")
    print(description)
    print("\nTell JARVIS what you want help with.")
    request = input("Your request: ").strip()

    if request:
        print("\nRequest saved for this session:")
        print(request)
        print("\nThis skill menu is ready for its AI integration.")
    else:
        print("No request entered.")


def main():
    while True:
        show_menu()
        choice = input("\nChoose a skill (0-11): ").strip()

        if choice == "0":
            print("JARVIS signing off. Goodbye!")
            break

        if choice in SKILLS:
            run_skill(choice)
        else:
            print("Invalid choice. Select a number from 0 to 11.")


if __name__ == "__main__":
    main()

