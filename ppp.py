import requests
url="https://uselessfacts.jsph.pl/random.json?language=en"
def get_random_technology_fact():
    response=requests.get(url)
    if response.status_code==200:
        fact_data=response.json()
        print(f"Did you know{fact_data['text']}")
    else:
        print("Failed to fetch")
        
while True:
            user_input=input("Press enter to get a random fact technology or type q to quit")
            if user_input.lower()=='q':
              break
            get_random_technology_fact()

