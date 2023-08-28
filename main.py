from image_processing import preprocess_image
from text_extraction import extract_text
from text_parsing import parse_aadhaar_info
def main():
    image=preprocess_image('Pratham.jpg')
    extracted_text=extract_text(image)
    aadhaar_info=parse_aadhaar_info(extracted_text)
    if aadhaar_info:
        print("Aadhaar Information:")
        print("Aadhaar Number:",aadhaar_info['aadhaar_number'])
    else:
        print("Aadhaar number not found in the extracted text.")
if __name__ == '__main__':
    main()
