from io import BytesIO
import requests
from PIL import Image,ImageEnhance,ImageFilter

def generate_image(prompt):
    url=f" https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}"
    print("Fetching image from pollination...")

    response=requests.get(url)
    img=Image.open(BytesIO(response.content))
    return img

def post_process(image):
    image=ImageEnhance.Brightness(image).enhance(1.2)
    image=ImageEnhance.Contrast(image).enhance(1.3)
    image=image.filter(ImageFilter.GaussianBlur(1.5))
    return image

def main():
    print("Pollination AI image generator+Post Processing")

while True:
    prompt=input("Enter prompt(or 'exit'):")
    if prompt.lower()=="exit":
        break

    img=generate_image(prompt)

    processed=post_process(img)

    processed.show()

    save=input("Save image?(Yes/No):").lower()
    if save=="yes":
        name=input("File name:").strip()
        processed.save(f"{name}.png")
        print(f"Image saves as {name}.png")

if __name__=="__main__":
    main()