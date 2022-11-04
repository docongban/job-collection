from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

def itviecTotal():
    # ITViec
    driver.maximize_window()
    driver.get("https://itviec.com/it-jobs?page=1&query=&source=search_job")
    driver.implicitly_wait(20)
    totalResult = driver.find_element(By.CSS_SELECTOR, "#jobs h1")
    count = 0
    data = []

    # total page to crawl
    listPaginations =driver.find_elements(By.XPATH, "//ul[@class='pagination']//li")
    totalPages = int(listPaginations[3].text)

    for i in range(totalPages):
        driver.get(f'https://itviec.com/it-jobs?page={i+1}&query=&source=search_job')
        driver.implicitly_wait(20)
        listTitles = driver.find_elements(By.XPATH, "//div[@class='details']//h3//a")
        listTags = driver.find_elements(By.XPATH, "//div[@class='job-bottom']//div[@class='tag-list']")
        listCitys = driver.find_elements(By.XPATH, "//div[@class='job_content']//div//div[@class='city']//div[@class='address']")
        listLogoes = driver.find_elements(By.XPATH, "//div[@class='logo']//div//a//picture//img")
        # print(listTags[1].text)
        for index,title in enumerate(listTitles):
            count+=1
            print(count,'-',title.text,'-',title.get_attribute('href'))
            data.append(['itviec', title.text, listCitys[index].text, listTags[index].text, title.get_attribute('href'), listLogoes[index].get_attribute('data-src')])
        driver.implicitly_wait(20)
  
    # Create DataFrame
    df = pd.DataFrame(data, columns=['Page', 'Title','City', 'Tag', 'Link', 'Logo'])
    df.to_csv("F:\\Hoc truc tuyen K7\\NM KHDL\\BTL\\JOB1\\itviec.csv")

    return totalResult.text

print(itviecTotal())