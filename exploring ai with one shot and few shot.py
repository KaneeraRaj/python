import cohere
from config import COHERE_API_KEY

if not COHERE_API_KEY:
    print("API key missing in config.py")
    exit()

co=cohere.Client(COHERE_API_KEY)

def generate_response(prompt,temperature=0.5):

    response=co.chat(
        model="c4ai-aya-expanse-8b",
        message=prompt,
        temperature=temperature,
        max_tokens=300
    )

    return text.strip()

def run_activity():
    print("Zero-shot,One-shot and few-shot learning")

    category=input(
        "Enter a category(e.g. animal,science,language etc.)"
    ).strip()

    item=input(
        f"Enter a specific{category}"
    ).strip()

    if not category or not item:
        print("Please fill both the fields")
        return

    zero_shot=f"Is {item} a {category} ? Answer yes or no"

    print("\n---Zero shot learning---")
    print("Response:", generate_response(one_shot,temperature=0.3))

    one_shot=f"""
Example:
Category:Fruit
Item:Apple
Answer:Yes,apple is a fruit.

You try:
Category:{category}
Item:{item}
Answer:
"""

    print("\n ----One shot learning---")
    print("Response:",generate_response(one_shot,temperature=0.3))

    few_shot=f"""

Example 1:
Category:Fruit
Item:Apple
Answer:Yes,apple is a fruit.

Example 2:
Category:animal
Item:dog
Answer:Yes,dog is an animal

You try:
Category:{category}
Item:{item}
Answer:
"""

    print("\n Few shot learning")
    print("Response:",generate_response(few_shot,temperature=0.7))

if __name__=="__main__":
    run_activity()