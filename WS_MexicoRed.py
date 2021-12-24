# Importar líbrerías.
import unidecode as unidecode
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

website = 'http://agricultura.mexicored.com.mx/'  # Variable para guardar la URL.
path = 'C:/Users/Erick Lozano/Desktop/chromedriver_win32/chromedriver'  # Se obtiene de la ruta donde se aloja en la PC.

driver = webdriver.Chrome(path)  # Se utiliza el driver para abrir Chrome.
driver.get(website)  # Se obtiene la página.

Nombre = []
Direccion = []
Descripcion = []

for a in range(10):  # La página web contiene 10 páginas para poder consultarlas.
    a = a + 1

    empresas = driver.find_elements_by_xpath('//a[@class="truncate"]')  # Con el Xpath se extrae una lista de las empresas.
    Empresas = []
    for empresa in empresas:  # Se recorre la lista de las empresas.
        Empresas.append(empresa.text)  # Se agrega a una lista.

    for i in Empresas:  # Se recorre la lista de las empresas.
        driver.find_element_by_link_text(i).click()  # Se da click al link que contiene el nombre de la empresa.
        time.sleep(4)  # Se espera un tiempo.

        nombre = driver.find_element_by_xpath('//h1[@class="title"]')  # Con el Xpath se extrae el nombre de la empresa.
        Nombre.append(nombre.text)  # Se agrega a una lista.
        direccion = driver.find_element_by_xpath('//span[@class="location"]')  # Con el Xpath se extrae la dirección de la empresa.
        Direccion.append(direccion.text)  # Se agrega a una lista.
        descripcion = driver.find_element_by_xpath('//div[@class="card-block"]')  # Con el Xpath se extrae la descripción de la empresa.
        Descripcion.append(descripcion.text)  # Se agrega a una lista.

        driver.back()  # Se regresa a la anterior página.
        time.sleep(3)  # Se espera un tiempo.

    if a < 10:  # Cuando a sea menor a 10.
        driver.get('http://agricultura.mexicored.com.mx/' + str(a) + '.html')  # Se obtiene la página correspondiente.
        time.sleep(4)  # Se espera un tiempo.

driver.quit()  # Se detiene el driver.

Nombres = []
Direcciones = []
Descripciones = []

# Se realiza la decodificación de toda la información y se guarda en una nueva lista.
for nombres in Nombre:
    Nombres.append(unidecode.unidecode(nombres))

for direcciones in Direccion:
    Direcciones.append(unidecode.unidecode(direcciones))

for descripciones in Descripcion:
    Descripciones.append(unidecode.unidecode(descripciones))

# Se crea un DataFrame con la información decodificada.
df = pd.DataFrame({'Empresa': Nombres,
                   'Direciion': Direcciones,
                   'Descripcion': Descripciones})

df.to_csv('WS_MexicoRed.csv', index=False)  # Se exporta a un archivo CSV.