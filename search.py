import time
from selenium import webdriver
from mode import OCR

def search_for_answer():
    driver = webdriver.Chrome()

    driver.get('http://www.baidu.com/')
    print(OCR.ocr.text)

    driver.find_element_by_id("kw").send_keys(OCR.ocr.text)
    driver.find_element_by_id("su").click()

    time.sleep(3)
    driver.close()
    driver.quit()