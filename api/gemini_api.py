import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
load_dotenv()

api = os.getenv("GEMINI_APIKEY")
genai.configure(api_key=api)
model = genai.GenerativeModel("gemini-2.5-flash")
image = Image.open("./public/banana.jpg")

response = model.generate_content(
    ["What are the calories, carbs, protein, and fat content of this image? Strictly return a json object with the keys as calories, carbs, protein, and fat and the values as the content of the image", image]
)

print(response.text)
