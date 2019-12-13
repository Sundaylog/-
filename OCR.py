from PIL import Image
import pytesseract
class ocr:
    pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)/Tesseract-OCR/tesseract.exe'
    text = pytesseract.image_to_string(Image.open('C:/Users/sunday/Desktop/答题器/mode/pic/screen_dealed.png'),lang='chi_sim')