import requests
from requests.auth import HTTPBasicAuth

API_Key="acc_e8f289c36d8c8c9"
API_SECRET="4c683e8aa9430ab41a13f335857b88c0"

def caption_single_image(image_path):
    url="https://api.imagga.com/v2/tags"

    with open(image_path,"rb")as img:
        response=requests.post(
            url,
            auth=HTTPBasicAuth(API_Key,API_SECRET),
            files={"image":img}
        )

    data=response.json()
    tags=data["result"]["tags"][:5]

    caption=",".join(tag["tag"]["en"]for tag in tags)

    print("image:",image_path)
    print("Caption(generated from tags)",caption)

def main():
            image_path=input("Enter image path:")
            caption_single_image(image_path)

if __name__=="__main__":
            main()