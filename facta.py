import requests

url="https://uselessfacts.jsph.pl/random.json?language=en"

def get_fact(category):
    try:
        url=url.format(category)
        response=requests.get(url)

        if response.status_code==200:
            data=response.json()
            print("{data['text]}")

        else:
            print("Category not found")

    except:
        print("Failed to fetch fact")

    categories=["Techonology","Science","Poetry","History","Random"]

    print("Uselesss fact explorer")
    print("Select categiry or type q to exirt")

    for i, c in enumerate(categories,1):
        print(f"{i},{c}")

while True:
    choice=input("\n Enter category number:")

    if choice.lower()=="q":
        print("Goodbye")
        break

    if choice.isdigit()and 1<=int(choice)<= len(caategories):
        selected=categories[int(choice)-1]
        print(f"\n Fetching{selected} fact...")
        get_fact(selected)

    else:
            print("Invalid choice.Try again")