from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pytextdist.edit_distance import lcs_similarity
import pandas as pd
import re
import math

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

def itviecTotal(province, jobInput):
    # ITViec
    driver.maximize_window()
    driver.get("https://itviec.com/?job_selected=c-net-angular-developer-upto-2000-usol-vietnam-4410")
    driver.implicitly_wait(20)

    # Comobox select province
    comboxElement = driver.find_element(By.ID, "city-ts-control")
    comboxElement.click()
    listOptionComboBox = driver.find_elements(By.XPATH, "//div[@class='option']")
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
    inputElement = driver.find_element(By.ID, "query")
    inputElement.send_keys(jobInput)
    inputElement.send_keys(Keys.ENTER)

    totalResult = driver.find_element(By.CSS_SELECTOR, "#jobs h1")
    # print(totalResult.text)
    return totalResult.text

def recommendJob():
    driver.implicitly_wait(2000)
    
    # salaryElements = driver.find_elements(By.XPATH, "//div[@class='pe-3']")
    # salaryElements[1].click()

    # listSalaryDropdown = driver.find_elements(By.XPATH, "//div[@class='input-group-prepend']")
    
    # if salary >= 500 and salary < 1000:
    #     listSalaryDropdown[4].click()
    # elif salary >= 1000 and salary < 2000:
    #     listSalaryDropdown[5].click()
    # elif salary >= 2000 and salary < 2500:
    #     listSalaryDropdown[6].click()
    # elif salary >= 2500:
    #     listSalaryDropdown[7].click()
    # salaryElements[3].click()

    listJobs = driver.find_elements(By.XPATH, "//div[@class='details']//h3//a")
    for index,job in enumerate(listJobs):
        print(index+1,'-',job.text,'-',job.get_attribute('href'))
        if index == 3:
            break

def recommend4Job(keyword, province):

    province = no_accent_vietnamese(province.lower())
    list = province.split(' ')
    province = "-".join(list)

    driver.maximize_window()
    driver.get(f"https://itviec.com/it-jobs/{keyword}/{province}?source=search_job")
    driver.implicitly_wait(20)
    totalResult = driver.find_element(By.CSS_SELECTOR, "#jobs h1")
    count = 0
    dict = {}
    listdata = []
    listIndex = []

    # total page to crawl
    totalPages = math.ceil(int(totalResult.text.split(" ")[0])/20)

    for i in range(totalPages):
        driver.get(f'https://itviec.com/it-jobs/{keyword}/{province}?page={i+1}&source=search_job')
        driver.implicitly_wait(20)
        listTitles = driver.find_elements(By.XPATH, "//div[@class='details']//h3//a")
        for index,title in enumerate(listTitles):
            listdata.append(f"{title.text}---{title.get_attribute('href')}")
        driver.implicitly_wait(20)
  
    for i,data in enumerate(listdata):
        x = data.split('---')[0]
        if no_accent_vietnamese(keyword.lower()) in no_accent_vietnamese(x.lower()):
            dict[i] = lcs_similarity(no_accent_vietnamese(keyword.lower()),no_accent_vietnamese(x.lower()))
    for i in sorted(dict, key=dict.get, reverse=True):
        count+=1
        listIndex.append(int(i))
        if count == 4:
            break

    print("----------ITViec----------")
    for i,index in enumerate(listIndex):
        print(i+1,'-',listdata[index])
