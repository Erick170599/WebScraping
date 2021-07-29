import unidecode as unidecode
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

website = 'http://agricultura.mexicored.com.mx/'
path = 'C:/Users/Erick Lozano/Desktop/chromedriver_win32/chromedriver'

driver = webdriver.Chrome(path)
driver.get(website)

Nombre = []
Direccion = []
Descripcion = []

for a in range(10):
    a = a + 1

    empresas = driver.find_elements_by_xpath('//a[@class="truncate"]')
    Empresas = []
    for empresa in empresas:
        Empresas.append(empresa.text)

    for i in Empresas:
        driver.find_element_by_link_text(i).click()
        time.sleep(4)

        nombre = driver.find_element_by_xpath('//h1[@class="title"]')
        Nombre.append(nombre.text)
        direccion = driver.find_element_by_xpath('//span[@class="location"]')
        Direccion.append(direccion.text)
        descripcion = driver.find_element_by_xpath('//div[@class="card-block"]')
        Descripcion.append(descripcion.text)

        driver.back()
        time.sleep(3)

    if a < 10:
        driver.get('http://agricultura.mexicored.com.mx/' + str(a) + '.html')
        time.sleep(4)

driver.quit()

Nombres = []
Direcciones = []
Descripciones = []

for nombres in Nombre:
    Nombres.append(unidecode.unidecode(nombres))

for direcciones in Direccion:
    Direcciones.append(unidecode.unidecode(direcciones))

for descripciones in Descripcion:
    Descripciones.append(unidecode.unidecode(descripciones))

df = pd.DataFrame({'Empresa': Nombres,
                   'Direciion': Direcciones,
                   'Descripcion': Descripciones})

df.to_csv('WS_MexicoRed.csv', index=False)