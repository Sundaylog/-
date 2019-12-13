import os
from PIL import Image

def screen_shot():
    adb_screenshot = "adb shell /system/bin/screencap -p /storage/emulated/0/Pictures/new/screen.png"
    adb_copy="adb pull /storage/emulated/0/Pictures/new/screen.png C://Users/sunday/Desktop/答题器/mode/pic/screen.png"
    os.system(adb_screenshot)
    os.system(adb_copy)
def deal_picture():
    img = Image.open("C:/Users/sunday/Desktop/答题器/mode/pic/screen.png")
    cropped = img.crop((80, 650, 1000, 900))
    cropped.save("C:/Users/sunday/Desktop/答题器/mode/pic/screen_dealed.png")