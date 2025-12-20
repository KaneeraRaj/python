import requests

url="https://sentim-api.onrender.com/api/v1/"

headers={
    "Accept":"application/json",
    "Content-Type":"application/json"
}

test_sentences={
    "Positive":"I love doing coding",
    "Negative":"I hate errors in my coding",
    "Neutral":"I am doing coding"
}

print("Sentiment Analysis Testing")

for expected,text in test_sentences.items():
    data={"text":text}

    try:
        response=requests.post(url,headers=headers,json=data)
        result=response.json()

        sentiment=result["result"]["type"]
        polaroty=result["result"]["polarity"]

        print(f"Input text:{text}")
        print(f"Expected type:{expected}")
        print(f"Predicted type:{sentiment}")
        print(f"Polarity type:{polarity}")
        print("-"*50)

    except Exception as e:
        print("Error occured",e)