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

# Topcv
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
province = input()

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
jobInput = input()
inputElement = driver.find_element(By.ID, "keyword")
inputElement.send_keys(jobInput)
inputElement.send_keys(Keys.ENTER)

totalResult = driver.find_element(By.XPATH, "//div//div//div//div//h1")
print(totalResult.text)