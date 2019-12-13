import os
from PIL import Image
import pytesseract
'''
    1、用adb截取屏幕并将其发送至电脑处理截图
    #phone_ID = "6SJNW18621033264"
    adb_screenshot = "adb shell /system/bin/screencap -p /storage/emulated/0/Pictures/new/screen.png"
    adb_copy="adb pull /storage/emulated/0/Pictures/new/screen.png C://Users/sunday/Desktop/答题器/mode/pic/screen.png"
    os.system(adb_screenshot)
    os.system(adb_copy)
    img = Image.open("pic/screen.png")
    #print(img.size) #(1080, 2280)
    cropped = img.crop((80, 650, 1000, 900)) #(left,up,right,down)
    cropped.save("pic/screen_dealed.png")

'''
'''
    2、ocr识别图中文字

    pytesseract.pytesseract.tesseract_cmd = 'C://Program Files (x86)/Tesseract-OCR/tesseract.exe'
    text = pytesseract.image_to_string(Image.open('pic/screen_dealed.png'),lang='chi_sim')
    text.replace(" ","")
    print(text)
    print(len(text))

'''













'''
    3、使用百度搜索这些文字
'''