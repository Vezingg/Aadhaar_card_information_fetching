import pytesseract
def extract_text(image):
    pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    extracted_text=pytesseract.image_to_string(image)
    return extracted_text
