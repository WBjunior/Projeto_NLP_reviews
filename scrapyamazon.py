# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 22:52:45 2023

@author: Wellington Junior, Otavio Linhares
"""

import time 
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


DRIVER_PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

asin_list =[]
title_list =[]

# Encontrar todos os asins do resultado de pesquisa amazon
urls =[f'https://www.amazon.com/s?k=Kindle&page={i}&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1682723260&ref=sr_pg_{i}' for i in range (1,4)]
for url in urls:  
    driver.get(url)
    product_asins = driver.find_elements(By.XPATH,'//*[@data-asin]')
    product_titles = driver.find_elements(By.XPATH,"//span[@class='a-size-base-plus a-color-base a-text-normal']")
    for product_asin in product_asins:
        asin = product_asin.get_attribute("data-asin")
        if asin !="" and asin not in asin_list :
            tag = driver.find_element(By.XPATH,"//div[@data-asin='"+asin+"']")  
            title =product_asin.find_element(By.XPATH,"//div[@data-asin='"+asin+"']//span[@class='a-size-base-plus a-color-base a-text-normal']").text
            #print(title.text)
            #print(asin)
            asin_list.append(asin)
            title_list.append(title)
print(asin_list)       
list_review = []
list_rating = []
list_asin = []

for asin in asin_list:
#gerar uma lista de urls para cada pagina do produto
    product_review_url_list = [f'https://www.amazon.com/product-reviews/{asin}/ref=cm_cr_arp_d_paging_btm_next_{i}?pageNumber={i}' for i in range (1,100)]
    for product_review_url in product_review_url_list:
        try:
            driver.get(product_review_url)
            # encontrar todos os elementos de revisão
            review_elements = driver.find_elements(By.CSS_SELECTOR,'div[data-hook="review"]')
            # iterar sobre os elementos e extrair as informações necessárias
            for review_element in review_elements:
                review_text = review_element.find_element(By.CSS_SELECTOR,'span[data-hook="review-body"]').text.strip()
                rating_text = review_element.find_element(By.XPATH,'//i[@data-hook="review-star-rating"]//span[contains(@class, "a-icon-alt")]')
                rating = rating_text.get_attribute('innerHTML').split()[0]
                list_review.append(review_text)
                list_rating.append(rating)
                list_asin.append(asin)
        except Exception as e:
            print("Error", e)

product_dict ={'title': title_list,'asin': asin_list}
review_dict = {'text':list_review,'rating':list_rating,'asin' : list_asin}
#print(review_dict)
review_data = pd.DataFrame.from_dict(review_dict)
product_data = pd.DataFrame.from_dict(product_dict)
print(review_data.shape)
review_data.to_csv('Scraping reviews.csv')
product_data.to_csv('Scraping products.csv')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
driver.save_screenshot("screenshot.png")

driver.quit()