from image_processing import preprocess_image
from text_extraction import extract_text
from text_parsing import parse_aadhaar_info
def main():
    image=preprocess_image('pratham.jpg')
    extracted_text=extract_text(image)
    aadhaar_info=parse_aadhaar_info(extracted_text)
    if aadhaar_info:
        print("Aadhaar Information:")
        print("Aadhaar Number:",aadhaar_info['aadhaar_number'])
        print("Birthdate:",aadhaar_info["birthdate"])
    else:
        print("Aadhaar information not found in the extracted text.")
if __name__ == '__main__':
    main()
