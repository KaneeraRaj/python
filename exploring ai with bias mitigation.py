import cohere
import config
import time

co=cohere.Client(config.COHERE_API_KEY)

def generate_response(prompt,temperature=0.3,max_tokens=400):
    """Generate Ai using Response"""
    try:
        response=co.chat(
            model="c4ai-aya-expanse-8b",
            message=prompt,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.text.strip()

    except Exception as e:
        return f"Error:{e}"

def bias_mitigation_activity():
    print("\n----Bias mitigation activity----")

    prompt=input("Enter a prompt(e.g. Describe the ideal doctor):").strip()
    if not prompt:
        print("Prompt cannot be empty")
        return

    initial=generate_response(prompt)
    print("\nInitial Ai response\n",initial)

    neutral=input("\nRewrite prompt in neutral form:").strip()

    if neutral:
        improved=generate_response(neutral)
        print("\nNeutral ai response\n",improved)
    else:
        print("No neutral prompt entered.")

def token_limit_activity():
    print("\n===TOKEN LIMIT ACTIVITY===")

    long_prompt=input("Enter a long prompt:").strip()

    if long_prompt:
        long_result=generate_response(long_prompt,max_tokens=800)
        preview=long_result[:500]+"..." if len(long_result)>500 else long_result
        print("\nLong prompt Response(Preview):\n",preview)
    else:
        print("Skipped long prompt")
    short_prompt=input("Enter condensed prompt:").strip()

    if short_prompt:
        short_result=generate_response(short_prompt,max_tokens=250)
        print("\nCondensed Prompt Response\n",short_result)
    else:
        print("Skipped condensed prompt")

def main():
    while True:
        print("\n--Ai prompt Engineering project--")
        print("1. Bias nitifigation")
        print("2.Token limit test")
        print("3.Exit")

        choice=input("Chose(1-3):").strip()

        if choice=="1":
            bias_mitigation_activity()

        elif choice=="2":
            token_limit_activity()

        elif choice=="3":
            print("Exiting program")
            break

        else:
            print("Invalid choice.Try again")

if __name__=="__main__":
    main()