# 5-4 openai 이미지

from openai import OpenAI

client = OpenAI()

prompt = input("Prompt: ")

response = client.images.geserate(
    model = "dall-e-3",
    prompt = prompt,
    size = "1024x1024",
    quality = "hd",
    n=1
)

image_url = response.data[0].url
print(image_url)