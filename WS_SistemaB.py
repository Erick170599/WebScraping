import unidecode as unidecode
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

website = 'https://www.sistemab.org/directorio-b/'
path = 'C:/Users/Erick Lozano/Desktop/chromedriver_win32/chromedriver'

driver = webdriver.Chrome(path)
driver.get(website)

Empresa = []
Descripcion = []
Industria = []
Origen = []
Presencia = []

for j in range(35):
    j = j + 1
    if j == 36:
        for a in range(1):
            a = a + 1
            industria = driver.find_element_by_xpath('//*[@id="list-b"]/li[' + str(a) + ']/div/h3[2]')
            if industria.text == 'Agricultura':
                empresa = driver.find_element_by_xpath('//*[@id="list-b"]/li[' + str(a) + ']/div/h2/a')
                Empresa.append(empresa.text)
                descripcion = driver.find_element_by_xpath('//*[@id="list-b"]/li[' + str(a) + ']/div/div[1]')
                Descripcion.append(descripcion.text)
                Industria.append(industria.text)
                origen = driver.find_element_by_xpath('//*[@id="list-b"]/li[' + str(a) + ']/div/h3[3]')
                Origen.append(origen.text)
                presencia = driver.find_element_by_xpath('//*[@id="list-b"]/li[' + str(a) + ']/div/h3[4]')
                Presencia.append(presencia.text)
    else:
        for i in range(20):
            i = i + 1
            industria = driver.find_element_by_xpath('//*[@id="list-b"]/li[' + str(i) + ']/div/h3[2]')
            if industria.text == 'Agricultura':
                empresa = driver.find_element_by_xpath('//*[@id="list-b"]/li[' + str(i) + ']/div/h2/a')
                Empresa.append(empresa.text)
                descripcion = driver.find_element_by_xpath('//*[@id="list-b"]/li[' + str(i) + ']/div/div[1]')
                Descripcion.append(descripcion.text)
                Industria.append(industria.text)
                origen = driver.find_element_by_xpath('//*[@id="list-b"]/li[' + str(i) + ']/div/h3[3]')
                Origen.append(origen.text)
                presencia = driver.find_element_by_xpath('//*[@id="list-b"]/li[' + str(i) + ']/div/h3[4]')
                Presencia.append(presencia.text)
        siguiente = driver.find_element_by_css_selector('#container > div > div > section > div > div > div > div > div > div > div > div > div > div > section.elementor-section.elementor-top-section.elementor-element.elementor-element-c41ce0e.elementor-section-full_width.elementor-section-height-default.elementor-section-height-default > div > div > div > div > div > div.elementor-element.elementor-element-e089d50.elementor-widget.elementor-widget-shortcode > div > div.text-center.wp-pages > a.next.page-numbers')
        siguiente.click()
        time.sleep(5)

driver.quit()

Empresas = []
Descripciones = []
Industrias = []
Origenes = []
Presencias = []

for empresas in Empresa:
    Empresas.append(unidecode.unidecode(empresas))

for descripciones in Descripcion:
    Descripciones.append(unidecode.unidecode(descripciones))

for industrias in Industria:
    Industrias.append(unidecode.unidecode(industrias))

for origenes in Origen:
    Origenes.append(unidecode.unidecode(origenes))

for presencias in Presencia:
    Presencias.append(unidecode.unidecode(presencias))

df = pd.DataFrame({'Empresa': Empresas,
                   'Descripcion': Descripciones,
                   'Industria': Industrias,
                   'Origen': Origenes,
                   'Con presencia en:': Presencias})

df.to_csv('WS_SistemaB.csv', index=False)

print(df)