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

def topcvTotal(province, jobInput):
    # Topcv
    driver.maximize_window()
    driver.get("https://www.topcv.vn/tim-viec-lam-moi-nhat")
    driver.implicitly_wait(20)

    # Comobox select province
    comboxElement = driver.find_element(By.ID, "select2-city-container")
    comboxElement.click()
    listOptionComboBox = driver.find_elements(By.XPATH, "//li[@class='select2-results__option']")
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

    totalResult = driver.find_element(By.CSS_SELECTOR, ".job-header span")
    # print(totalResult.text)
    return totalResult.text

def recommendJob():
    driver.implicitly_wait(2000)
    driver.find_elements(By.XPATH, "//div[@class='header']//div//button[@class='btn btn-close']")[0].click()
    
    # salaryElements = driver.find_elements(By.XPATH, "//div[@class='filter-job']//div//div")
    # salaryElements[3].click()

    # salaryVn = round(salary * 23 / 1000)

    # listSalaryDropdown = driver.find_elements(By.XPATH, "//ul[@id='select2-salary-advanced-results']//li")
    # if salaryVn < 3:
    #     listSalaryDropdown[1].click()
    # elif salaryVn >= 3 and salaryVn < 5:
    #     listSalaryDropdown[2].click()
    # elif salaryVn >= 5 and salaryVn < 7:
    #     listSalaryDropdown[3].click()
    # elif salaryVn >= 7 and salaryVn < 10:
    #     listSalaryDropdown[4].click()
    # elif salaryVn >= 10 and salaryVn < 12:
    #     listSalaryDropdown[5].click()
    # elif salaryVn >= 12 and salaryVn < 15:
    #     listSalaryDropdown[6].click()
    # elif salaryVn >= 15 and salaryVn < 20:
    #     listSalaryDropdown[7].click()
    # elif salaryVn >= 20 and salaryVn < 25:
    #     listSalaryDropdown[8].click()
    # elif salaryVn >= 25 and salaryVn < 30:
    #     listSalaryDropdown[9].click()
    # elif salaryVn >= 30:
    #     listSalaryDropdown[10].click()
    # else:
    #     listSalaryDropdown[0].click()
    
    listJobs = driver.find_elements(By.XPATH, "//div[@class='content']//div/h3/a")
    for index,job in enumerate(listJobs):
        print(index+1,'-',job.text,'-',job.get_attribute('href'))
        if index == 3:
            break

def getAllJob():
    driver.implicitly_wait(2000)
    driver.find_elements(By.XPATH, "//div[@class='header']//div//button[@class='btn btn-close']")[0].click()

    nextPage = driver.find_element(By.XPATH, "//li//a[@rel='next']")

    listJobs = driver.find_elements(By.XPATH, "//div[@class='content']//div/h3/a")

    for job in listJobs:
        print(job.text)
    nextPage.click()
    for job in listJobs:
        print(job.text)

def recommend4Job(keyword, province):

    province = no_accent_vietnamese(province.lower())
    list = province.split(' ')
    province = "-".join(list)

    kl=""
    if province == "ha-noi": kl = "kl1"
    elif province == "ho-chi-minh": kl = "kl2"
    

    driver.maximize_window()
    driver.get(f"https://www.topcv.vn/tim-viec-lam-{keyword}-tai-{province}-{kl}?sort=top_related")
    driver.implicitly_wait(20)
    
    totalResult = driver.find_element(By.CSS_SELECTOR, ".job-header span")
    count = 0
    dict = {}
    listdata = []
    listIndex = []

    # total page to crawl
    totalPages = math.ceil(int(totalResult.text.split(" ")[2])/25)

    for i in range(totalPages):
        driver.get(f'https://www.topcv.vn/tim-viec-lam-{keyword}-tai-{province}-{kl}?salary=0&exp=0&sort=top_related&page={i+1}')
        time.sleep(2)
        listTitles = driver.find_elements(By.XPATH, "//div[@class='body']//div[@class='content']//div//h3//a")
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

    print("----------Topcv----------")
    for i,index in enumerate(listIndex):
        print(i+1,'-',listdata[index])