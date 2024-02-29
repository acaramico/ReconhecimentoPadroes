#https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
import pytesseract
from PIL import Image

def perform_ocr(imagem_path):
    imagem = Image.open(imagem_path)
    text = pytesseract.image_to_string(imagem, lang='kor')
    return text


imagem_path = "korean_phrases.png"
print("Gerando OCR...")
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Aluno\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
ocr_text = perform_ocr(imagem_path)
print(ocr_text)
