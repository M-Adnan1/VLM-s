from image_processor import load_image
from model import load_model, generate_response

vlm_model = load_model()

image_url = input("Enter image Path")
image = load_image(image_url)

question = input("Write a question about the image: ")

response = generate_response(image_path=image, question=question, vlm=vlm_model)
print(response)