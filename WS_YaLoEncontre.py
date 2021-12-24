# Importar líbrerías.
import unidecode as unidecode
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

website = 'http://www.yaloencontre.mx/resultado_negocios.php?var=agricultura&estado=&municipio='  # Variable para guardar la URL.
path = 'C:/Users/Erick Lozano/Desktop/chromedriver_win32/chromedriver'  # Se obtiene de la ruta donde se aloja en la PC.

driver = webdriver.Chrome(path)  # Se utiliza el driver para abrir Chrome.
driver.get(website)  # Se obtiene la página.

Nombre = []
Descripcion = []
Estado = []
Telefono = []

for i in range(3):  # Se realiza el corriemiento dependiendo a las páginas que se tenga.
    empresas = driver.find_elements_by_xpath('//div[@class="info-resultado-gratis"]')  # Con el Xpath se genera una lista de las empresas encontradas.
    for empresa in empresas:  # Se recorren las empresas.
        nombre = empresa.find_element_by_xpath('.//h3')  # Con el Xpath se extrae el nombre de la empresa.
        Nombre.append(nombre.text)  # Se agrega a una lista.
        descripcion = empresa.find_element_by_xpath('.//font')  # Con el Xpath se extrae la descripción de la empresa.
        Descripcion.append(descripcion.text)  # Se agrega a una lista.
        estado = empresa.find_element_by_xpath('.//p[2]')  # Con el Xpath se extrae la ubicación de la empresa.
        Estado.append(estado.text)  # Se agrega a una lista.
        telefono = empresa.find_element_by_xpath('.//p[3]')  # Con el Xpath se extrae el telefono de la empresa.
        Telefono.append(telefono.text)  # Se agrega a una lista.

    if i <= 1:
        siguiente = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[13]/ul/li[2]/a')  # Se selecciona el botón de siguente.
        siguiente.click()  # Se da click sobre el botón "siguiente".
        time.sleep(5)  # Se espera un tiempo.

driver.quit()  # Se detiene el driver.

Nombres = []
Descripciones = []
Estados = []
Telefonos = []

# Se realiza la decodificación de toda la información y se guarda en una nueva lista.
for nombres in Nombre:
    Nombres.append(unidecode.unidecode(nombres))

for descripciones in Descripcion:
    Descripciones.append(unidecode.unidecode(descripciones))

for estados in Estado:
    Estados.append(unidecode.unidecode(estados))

for telefonos in Telefono:
    Telefonos.append(unidecode.unidecode(telefonos))

# Se crea un DataFrame con la información decodificada.
df = pd.DataFrame({'Empresa': Nombres,
                   'Descripcion': Descripciones,
                   'Direccion': Estados,
                   'Telefono': Telefonos})

df.to_csv('WS_YLEncontre.csv', index=False)  # Se exporta a un archivo CSV.