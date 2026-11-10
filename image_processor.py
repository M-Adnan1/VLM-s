from pathlib import Path
from PIL import Image

def load_image(image_path):

    image_path = Path(image_path).expanduser()
    if not image_path.is_file():
        raise FileNotFoundError(f"Image not found: {image_path}")

    try:
        image = Image.open(image_path)
        image.verify()
        image = Image.open(image_path).convert("RGB")
        return image

    except Exception as e:
        raise ValueError(f"Invalid Image: {e}")
    