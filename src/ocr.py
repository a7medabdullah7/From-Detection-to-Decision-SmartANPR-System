
import easyocr

reader = easyocr.Reader(['en'])

def read_plate(image):
    results = reader.readtext(image)
    if results:
        return results[0][1]
    return ""
