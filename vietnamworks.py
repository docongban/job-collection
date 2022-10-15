from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re

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

def vietnamworksTotal(province, jobInput):
    # Vietnamworks
    driver.maximize_window()
    driver.get("https://www.vietnamworks.com/")
    driver.implicitly_wait(20)

    # If showing pop up advertisement
    # advertisementElement = driver.find_element(By.ID, "iDontCareEventTopDev")
    # if(advertisementElement):
    #     advertisementElement.click()

    # Comobox select province
    comboxElement = driver.find_element(By.XPATH, "//div[@data-id='multiple-select-search-bar']")
    comboxElement.click()
    listOptionComboBox = driver.find_elements(By.XPATH, "//div//div//div//label")
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
    inputElement = driver.find_element(By.XPATH, "//input[@placeholder='Tìm kiếm việc làm, công ty, kỹ năng']")
    inputElement.send_keys(jobInput)
    inputElement.send_keys(Keys.ENTER)

    totalResult = driver.find_element(By.XPATH, "//div//div//div//div//div//div//div//div//div//div//div//div//div//h1")
    # print(totalResult.text)
    return totalResult.text

def recommendJob(salary):
    driver.implicitly_wait(2000)
    
    addElement = driver.find_element(By.XPATH, "//div[@class='left-bar']/span")
    addElement.click()

    salaryElement = driver.find_element(By.XPATH, "//div[@class='dropdown-container active']//div[@class='dropdown-row']//div//div")
    salaryElement.click()

    listSalaryDropdown = driver.find_elements(By.XPATH, "//fieldset[@id='Level']//ul//li")
    
    if salary <= 500:
        listSalaryDropdown[1].click()
    elif salary > 500 and salary < 1000:
        listSalaryDropdown[2].click()
    elif salary >= 1000 and salary < 1500:
        listSalaryDropdown[3].click()
    elif salary >= 1500 and salary < 2000:
        listSalaryDropdown[4].click()
    elif salary >= 2000 and salary < 3000:
        listSalaryDropdown[5].click()
    elif salary >= 3000:
        listSalaryDropdown[6].click()

    searchElement = driver.find_elements(By.XPATH, "//div[@class='dropdown-container active']//div//button")
    searchElement[1].click()

    listJobs = driver.find_elements(By.XPATH, "//div[@class='job-info-wrapper ']//div//div//a[@class='job-title ']")
    for index,job in enumerate(listJobs):
        print(job.get_attribute('href'))
        if index == 2:
            break