import unidecode as unidecode
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

website = 'http://www.yaloencontre.mx/resultado_negocios.php?var=agricultura&estado=&municipio='
path = 'C:/Users/Erick Lozano/Desktop/chromedriver_win32/chromedriver'

driver = webdriver.Chrome(path)
driver.get(website)

Nombre = []
Descripcion = []
Estado = []
Telefono = []

for i in range(3):
    empresas = driver.find_elements_by_xpath('//div[@class="info-resultado-gratis"]')
    for empresa in empresas:
        nombre = empresa.find_element_by_xpath('.//h3')
        Nombre.append(nombre.text)
        descripcion = empresa.find_element_by_xpath('.//font')
        Descripcion.append(descripcion.text)
        estado = empresa.find_element_by_xpath('.//p[2]')
        Estado.append(estado.text)
        telefono = empresa.find_element_by_xpath('.//p[3]')
        Telefono.append(telefono.text)

    if i <= 1:
        siguiente = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[13]/ul/li[2]/a')
        siguiente.click()
        time.sleep(5)

driver.quit()

Nombres = []
Descripciones = []
Estados = []
Telefonos = []

for nombres in Nombre:
    Nombres.append(unidecode.unidecode(nombres))

for descripciones in Descripcion:
    Descripciones.append(unidecode.unidecode(descripciones))

for estados in Estado:
    Estados.append(unidecode.unidecode(estados))

for telefonos in Telefono:
    Telefonos.append(unidecode.unidecode(telefonos))

df = pd.DataFrame({'Empresa': Nombres,
                   'Descripcion': Descripciones,
                   'Direccion': Estados,
                   'Telefono': Telefonos})

df.to_csv('WS_YLEncontre.csv', index=False)