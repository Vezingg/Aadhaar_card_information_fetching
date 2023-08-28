import re
def parse_aadhaar_info(extracted_text):
    aadhaar_number_match=re.search(r'\d{4} \d{4} \d{4}',extracted_text)
    if aadhaar_number_match:
        aadhaar_number=aadhaar_number_match.group()
        aadhaar_info={
            'aadhaar_number': aadhaar_number,
        }
        return aadhaar_info
    else:
        return None 