import requests
def get_random_joke():
 """Fetch a random joke from the official joke APL"""
 url="https://official-joke-api.appspot.com/random_joke"
 response= requests.get(url)

 if response.status_code==200:
    print (f"Full JSON response: {response.json()}")
    joke_data=response.json()
    return f"{joke_data['setup']}-{joke_data['punchline']}"
 else:
        return "Failed to retrive joke"
def main():
 print("Random Joke Generator")

 while True:
    user_input=input("Press Enter to get a new joke or press q to exit").strip().lower()
    if user_input in ("q","exit"):
     print("GoodBye")
     break

    joke=get_random_joke()
    print(joke)

if __name__=="__main__":
 main()

