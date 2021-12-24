# Importar líbrerías.
import unidecode as unidecode
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

website = 'https://www.sistemab.org/directorio-b/'  # Variable para guardar la URL.
path = 'C:/Users/Erick Lozano/Desktop/chromedriver_win32/chromedriver'  # Se obtiene de la ruta donde se aloja en la PC.

driver = webdriver.Chrome(path)  # Se utiliza el driver para abrir Chrome.
driver.get(website)  # Se obtiene la página.

Empresa = []
Descripcion = []
Industria = []
Origen = []
Presencia = []

for j in range(35):  # Se realiza un corrimiento.
    j = j + 1
    if j == 36:  # Es la excepción para la última página.
        for a in range(1):  # Como solamente tiene 1 registro, se recorren esas veces.
            a = a + 1
            industria = driver.find_element_by_xpath('//*[@id="list-b"]/li[' + str(a) + ']/div/h3[2]')  # Con el Xpath se guarda a que industria pertenece.
            if industria.text == 'Agricultura':  # Si la industria es de Agricultura.
                empresa = driver.find_element_by_xpath('//*[@id="list-b"]/li[' + str(a) + ']/div/h2/a')  # Con el Xpath se extrae el nombre de la empresa.
                Empresa.append(empresa.text)  # Se agrega a una lista.
                descripcion = driver.find_element_by_xpath('//*[@id="list-b"]/li[' + str(a) + ']/div/div[1]')  # Con el Xpath se extrae la descripción de la empresa.
                Descripcion.append(descripcion.text)  # Se agrega a una lista.
                Industria.append(industria.text)  # Se agrega a una lista.
                origen = driver.find_element_by_xpath('//*[@id="list-b"]/li[' + str(a) + ']/div/h3[3]')  # Con el Xpath se extrae la ubicación de la empresa.
                Origen.append(origen.text)  # Se agrega a una lista.
                presencia = driver.find_element_by_xpath('//*[@id="list-b"]/li[' + str(a) + ']/div/h3[4]')  # Con el Xpath se extrae donde tiene presencia la empresa.
                Presencia.append(presencia.text)  # Se agrega a una lista.
    else:
        for i in range(20):  # Se recorren las 20 empresas que se muestran por página.
            i = i + 1
            industria = driver.find_element_by_xpath('//*[@id="list-b"]/li[' + str(i) + ']/div/h3[2]')  # Con el Xpath se guarda a que industria pertenece.
            if industria.text == 'Agricultura':  # Si la industria es de Agricultura.
                empresa = driver.find_element_by_xpath('//*[@id="list-b"]/li[' + str(i) + ']/div/h2/a')  # Con el Xpath se extrae el nombre de la empresa.
                Empresa.append(empresa.text)  # Se agrega a una lista.
                descripcion = driver.find_element_by_xpath('//*[@id="list-b"]/li[' + str(i) + ']/div/div[1]')  # Con el Xpath se extrae la descripción de la empresa.
                Descripcion.append(descripcion.text)  # Se agrega a una lista.
                Industria.append(industria.text)  # Se agrega a una lista.
                origen = driver.find_element_by_xpath('//*[@id="list-b"]/li[' + str(i) + ']/div/h3[3]')  # Con el Xpath se extrae la ubicación de la empresa.
                Origen.append(origen.text)  # Se agrega a una lista.
                presencia = driver.find_element_by_xpath('//*[@id="list-b"]/li[' + str(i) + ']/div/h3[4]')  # Con el Xpath se extrae donde tiene presencia la empresa.
                Presencia.append(presencia.text)  # Se agrega a una lista.
        siguiente = driver.find_element_by_css_selector('#container > div > div > section > div > div > div > div > div > div > div > div > div > div > section.elementor-section.elementor-top-section.elementor-element.elementor-element-c41ce0e.elementor-section-full_width.elementor-section-height-default.elementor-section-height-default > div > div > div > div > div > div.elementor-element.elementor-element-e089d50.elementor-widget.elementor-widget-shortcode > div > div.text-center.wp-pages > a.next.page-numbers')  # Se selecciona el botón de siguente.
        siguiente.click()  # Se da click sobre el botón "siguiente".
        time.sleep(5)  # Se espera 5 seg.

driver.quit()  # Se detiene el driver.

Empresas = []
Descripciones = []
Industrias = []
Origenes = []
Presencias = []


# Se realiza la decodificación de toda la información y se guarda en una nueva lista.
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

# Se crea un DataFrame con la información decodificada.
df = pd.DataFrame({'Empresa': Empresas,
                   'Descripcion': Descripciones,
                   'Industria': Industrias,
                   'Origen': Origenes,
                   'Con presencia en:': Presencias})

df.to_csv('WS_SistemaB.csv', index=False)  # Se exporta a un archivo CSV.

print(df)