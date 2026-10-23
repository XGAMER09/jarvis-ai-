
"""
JARVIS - YouTube SEO Skill
Creates title, description, and keyword suggestions.
"""

def generate_seo(topic, language="Hindi"):
    topic = topic.strip()

    if not topic:
        return "Please enter a video topic."

    title = f"{topic} | Complete Guide in {language}"

    description = (
        f"In this video, we discuss {topic} in {language}.\n\n"
        "Watch till the end for useful tips and information.\n"
        "Subscribe for more videos!"
    )

    keywords = [
        topic,
        f"{topic} Hindi",
        f"{topic} tutorial",
        f"{topic} tips",
        f"{topic} explained"
    ]

    return {
        "title": title,
        "description": description,
        "keywords": keywords
    }


if __name__ == "__main__":
    result = generate_seo("YouTube Growth Tips")

    print("JARVIS SEO RESULTS")
    print("Title:", result["title"])
    print("\nDescription:", result["description"])
    print("\nKeywords:", ", ".join(result["keywords"]))
  
