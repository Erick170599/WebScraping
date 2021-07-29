import unidecode as unidecode
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

website = 'https://www.latmeco.com/?ls=agricultura&location='
path = 'C:/Users/Erick Lozano/Desktop/chromedriver_win32/chromedriver'

driver = webdriver.Chrome(path)
driver.get(website)

#empresas = driver.find_elements_by_tag_name('h2')
#hola = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/article[1]')

#empresas = driver.find_elements_by_xpath('//article')

for i in range(11):
    i = i + 2
    empresas = driver.find_element_by_xpath('//article[' + str(i) + ']')
    nombre = empresas.find_element_by_xpath('.//p[@class="listing-cat"]')
    print(nombre.text)

#Nombre = []
#for empresa in empresas:
 #   print(empresa.text)
  #  hola = empresa.find_element_by_xpath('.//h2')
   # print(hola.text)

#//*[@id="post-423"]
#/html/body/div[6]/div/div/div[1]/article[2]

#print(hola.text)

