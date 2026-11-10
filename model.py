from transformers import pipeline

MODEL_ID = "HuggingFaceTB/SmolVLM-256M-Instruct"

def load_model():
    vlm = pipeline(
        task = "image-text-to-text",
        model = MODEL_ID
    )
    return vlm


def generate_response(vlm, image_path, question):

    if not image_path and question:
        return False
    
    message = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "path": (image_path)
                },
                {
                    "type": "text",
                    "text": question
                }
            ]
        }
    ]

    result= vlm(text= message, max_new_tokens= 80)
    response = result[0]["generated_text"][-1]["content"]
    
    
    return response

