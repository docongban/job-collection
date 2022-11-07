from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pytextdist.edit_distance import lcs_similarity
import pandas as pd
import re
import math
import time

def no_accent_vietnamese(s):
    s = re.sub('[áàảãạăắằẳẵặâấầẩẫậ]', 'a', s)
    s = re.sub('[ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬ]', 'A', s)
    s = re.sub('[éèẻẽẹêếềểễệ]', 'e', s)
    s = re.sub('[ÉÈẺẼẸÊẾỀỂỄỆ]', 'E', s)
    s = re.sub('[óòỏõọôốồổỗộơớờởỡợ]', 'o', s)
    s = re.sub('[ÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢ]', 'O', s)
    s = re.sub('[íìỉĩị]', 'i', s)
    s = re.sub('[ÍÌỈĨỊ]', 'I', s)
    s = re.sub('[úùủũụưứừửữự]', 'u', s)
    s = re.sub('[ÚÙỦŨỤƯỨỪỬỮỰ]', 'U', s)
    s = re.sub('[ýỳỷỹỵ]', 'y', s)
    s = re.sub('[ÝỲỶỸỴ]', 'Y', s)
    s = re.sub('đ', 'd', s)
    s = re.sub('Đ', 'D', s)
    return s

driver = webdriver.Chrome(ChromeDriverManager().install())

def careerbuilderTotal(province, jobInput):
    # Careerbuilder
    driver.maximize_window()
    driver.get("https://careerbuilder.vn/viec-lam")
    driver.implicitly_wait(20)

    # If showing pop up advertisement
    # advertisementElement = driver.find_element(By.ID, "iDontCareEventTopDev")
    # if(advertisementElement):
    #     advertisementElement.click()

    # Comobox select province
    comboxElement = driver.find_element(By.ID, "location_chosen")
    comboxElement.click()
    listOptionComboBox = driver.find_elements(By.XPATH, "//ul//li[@class='active-result']")
    # province = input()

    checkSpace=False

    for option in listOptionComboBox:
        if no_accent_vietnamese(province.lower()) in no_accent_vietnamese(option.text.lower()):
            option.click()
            checkSpace=True
            break
        
    if checkSpace == False:
        for option in listOptionComboBox:
            if no_accent_vietnamese(province.lower()) in no_accent_vietnamese(option.text.lower()).replace(" ",""):
                option.click()
                break
        
    # Input search
    # jobInput = input()
    inputElement = driver.find_element(By.ID, "keyword")
    inputElement.send_keys(jobInput)
    inputElement.send_keys(Keys.ENTER)

    totalResult = driver.find_element(By.XPATH, "//div//div//div//div//h1")
    # print(totalResult.text)
    return totalResult.text

def recommend4Job(keyword, province):

    province = no_accent_vietnamese(province.lower())
    list = province.split(' ')
    province = "-".join(list)

    kl=""
    if province == "ha-noi": kl = "kl4"
    elif province == "ho-chi-minh": kl = "kl8"
    

    driver.maximize_window()
    driver.get(f"https://careerbuilder.vn/viec-lam/{keyword}-tai-{province}-{kl}-trang-1-vi.html")
    driver.implicitly_wait(20)
    
    totalResult = driver.find_element(By.XPATH, "//div[@class='job-found']//div[@class='job-found-amout']//h1")
    count = 0
    dict = {}
    listdata = []
    listIndex = []

    # total page to crawl
    totalPages = math.ceil(int(totalResult.text.split(" ")[0])/50)

    for i in range(totalPages):
        driver.get(f'https://careerbuilder.vn/viec-lam/{keyword}-tai-{province}-{kl}-trang-{i+1}-vi.html')
        time.sleep(2)
        listTitles = driver.find_elements(By.XPATH, "//div[@class='figcaption']//div//h2//a")
        for index,title in enumerate(listTitles):
            listdata.append(f"{title.text}---{title.get_attribute('href')}")
  
    for i,data in enumerate(listdata):
        x = data.split('---')[0]
        if no_accent_vietnamese(keyword.lower()) in no_accent_vietnamese(x.lower()):
            dict[i] = lcs_similarity(no_accent_vietnamese(keyword.lower()),no_accent_vietnamese(x.lower()))
    for i in sorted(dict, key=dict.get, reverse=True):
        count+=1
        listIndex.append(int(i))
        if count == 4:
            break

    print("----------Careerbuilder----------")
    for i,index in enumerate(listIndex):
        print(i+1,'-',listdata[index])