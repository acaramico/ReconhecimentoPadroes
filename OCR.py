import pytesseract
from PIL import Image

def perform_ocr(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text


image_path = "korean_phrases.png"
print("Gerando OCR...")
ocr_text = perform_ocr(image_path)