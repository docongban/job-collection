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
    driver.get("https://careerbuilder.vn/viec-lam/cntt-phan-mem-c1-vi.html")
    driver.implicitly_wait(20)
    count = 0
    data = []

    # total page to crawl
    totalResult = driver.find_element(By.XPATH, "//div[@class='job-found']//div[@class='job-found-amout']//h1")
    totalPages = math.ceil(int(totalResult.text.split(" ")[0])/50)

    for i in range(totalPages):
        driver.get(f'https://careerbuilder.vn/viec-lam/cntt-phan-mem-c1-trang-{i+1}-vi.html')
        time.sleep(2)
        listTitles = driver.find_elements(By.XPATH, "//div[@class='figcaption']//div//h2//a")
        listTags = listTitles
        listCitys = driver.find_elements(By.XPATH, "//div[@class='caption']//div[@class='location']//ul")
        listLogoes = driver.find_elements(By.XPATH, "//div[@class='figure']//div//a//img")
        for index,title in enumerate(listTitles):
            count+=1
            print(count,'-',title.text,'-',title.get_attribute('href'))
            data.append(['itviec', title.text, listCitys[index].text, listTags[index].text, title.get_attribute('href'), listLogoes[index].get_attribute('src')])
        # time.sleep(2)
  
    # Create DataFrame
    df = pd.DataFrame(data, columns=['Page', 'Title','City', 'Tag', 'Link', 'Logo'])
    df.to_csv("F:\\Hoc truc tuyen K7\\NM KHDL\\BTL\\JOB1\\careerbuilder.csv")

    return totalPages

print(itviecTotal())