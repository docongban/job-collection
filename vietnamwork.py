from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import time
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

def itviecTotal():
    driver.maximize_window()
    driver.get("https://www.vietnamworks.com/viec-lam-it-phan-mem-i35-vn?filtered=true")
    driver.implicitly_wait(20)
    count = 0
    data = []

    # total page to crawl
    totalResult = driver.find_element(By.XPATH, "//div//div//div//div//div//div//div//div//div//div//div//div//div//h1")
    totalPages = int(totalResult.text.split(" ")[0])

    for i in range(1):
        driver.get(f'https://www.vietnamworks.com/viec-lam-it-phan-mem-i35-vn?filtered=true&page={i+1}')
        time.sleep(4)
        listTitles = driver.find_elements(By.XPATH, "//div[@class='job-item-container']//div//div//div//div//div//div//a[@rel='noreferrer']")
        listTags = driver.find_elements(By.XPATH, "//div[@class='skill-tags_item']//ul")
        listCitys = driver.find_elements(By.XPATH, "//div[@class='job-item-container']//div//div//div//div//div[@class='location']")
        listLogoes = driver.find_elements(By.XPATH, "//div[@class='job-item-container']//div//div//div[@class='col-3 col-md-3 pr-0 pl-0']//div//a")
        # print(listTags[1].text)
        for index,title in enumerate(listTitles):
            count+=1
            print(count,'-',title.text,'-',title.get_attribute('href'))
            data.append(['itviec', title.text, listCitys[index].text, listTags[index].text, title.get_attribute('href'), listLogoes[index].get_attribute('data-src')])
        time.sleep(4)
  
    # Create DataFrame
    df = pd.DataFrame(data, columns=['Page', 'Title','City', 'Tag', 'Link', 'Logo'])
    # df.to_csv("F:\\Hoc truc tuyen K7\\NM KHDL\\BTL\\JOB1\\vietnamwork.csv")

    return totalResult.text

print(itviecTotal())