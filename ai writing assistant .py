import cohere
import config

co=cohere.Client(config.COHERE_API_KEY)

def generate_response(prompt,temperature=0.3):
    try:
        response=co.chat(
            model="c4ai-aya-expanse-8b",
            message=prompt,
            temperature=temperature,
            max_tokens=500
        )
        return response.text.strip()
    except Exception as e:
        return f"Error:{e}"

def get_essay_details():
    print("\n==== AI Writing Assistant===\n")

    topic=input("Topic:").strip()
    essay_type=input("Essay topic:").strip()
    length=input("Word count:(e.g.300 words)").strip()
    audience=input("Target audience:").strip()

    return topic,essay_type,length,audience

def generate_esssay(topic,essay_type,length,audience):
    try:
        temp=float(input("Temperature(0.1-0.7)")).strip(())
    except:
        temp=0.3
    sections={
        "Introduction": f"Write an introduction for a {essay_type} essay about{topic}in {length}.Audience{audience}",
        "Body":f"Write the body of a {essay_type} essay about{topic} for {audience}",
        "Conclusion":f"Write a strong conclusion for a {essay_type} essay about {topic} for {audience}"
    }
    for title,prompt in sections.items():
        print(f"\n==={title}===\n")
        print(generate_response(prompt,temp))
def main():
    print("Welcome to AI writing assistant")
    topic,essay_type,length,audience=get_essay_details()

    if topic and essay_type:
        generate_esssay(topic,essay_type,length,audience)
    else:
        print("Topic and essay type are required")

if __name__=="__main__":
    main()