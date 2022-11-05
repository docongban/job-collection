from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import time
import math
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

def itviecTotal():
    # driver.maximize_window()
    driver.get("https://www.topcv.vn/tim-viec-lam-it-phan-mem-c10026?sort=top_related")
    driver.implicitly_wait(20)
    count = 0
    data = []

    # total page to crawl
    totalResult = driver.find_element(By.XPATH, "//div[@class='list-job']//div[@class='job-header']//span")
    # totalPages = math.ceil(int(totalResult.text.split(" ")[0])/25)

    for i in range(197):
        driver.get(f'https://www.topcv.vn/tim-viec-lam-it-phan-mem-c10026?salary=0&exp=0&sort=top_related&page={i+1}')
        time.sleep(2)
        listTitles = driver.find_elements(By.XPATH, "//div[@class='body']//div[@class='content']//div//h3//a")
        listTags = listTitles
        listCitys = driver.find_elements(By.XPATH, "//div[@class='body']//div[@class='d-flex']//div/label[@class='address']")
        listLogoes = driver.find_elements(By.XPATH, "//div[@class='avatar']//a//img")
        for index,title in enumerate(listTitles):
            count+=1
            print(count,'-',title.text,'-',title.get_attribute('href'))
            data.append(['topcv', title.text, listCitys[index].text, listTags[index].text, title.get_attribute('href'), listLogoes[index].get_attribute('src')])
        # time.sleep(2)
  
    # Create DataFrame
    df = pd.DataFrame(data, columns=['Page', 'Title','City', 'Tag', 'Link', 'Logo'])
    df.to_csv("F:\\Hoc truc tuyen K7\\NM KHDL\\BTL\\JOB1\\topcv.csv")

    return totalResult.text

print(itviecTotal())