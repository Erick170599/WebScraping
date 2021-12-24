# Importar líbrerías.
import unidecode as unidecode
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

website = 'https://mx.kompass.com/s/agricultura-y-alimentacion/01/'  # Variable para guardar la URL.
path = 'C:/Users/Erick Lozano/Desktop/chromedriver_win32/chromedriver'  # Se obtiene de la ruta donde se aloja en la PC.

driver = webdriver.Chrome(path)  # Se utiliza el driver para abrir Chrome.
driver.get(website)  # Se obtiene la página.

Nombre = []
Estado = []
Descripcion = []
cont = 0
for i in range(40):  # Se realiza un corriemiento dependiendo a las páginas que tiene esa web.
    i = i + 2

    nombres = driver.find_elements_by_xpath('//span[@class="titleSpan"]')  # Con el Xpath se extrae una lista de los nombres de las empresas.
    estados = driver.find_elements_by_xpath('//a/span[@class="flagWorld"]')  # Con el Xpath se extrae una lista de las ubicaciones de las empresas.
    descripciones = driver.find_elements_by_class_name('details')  # Con el nombre de una clase se extrae una lista de las descripciones de las empresas.
    cont = cont + 1

    for nombre in nombres:  # Se recorren los nombres de las empresas.
        Nombre.append(nombre.text)  # Se agrega a una lista.

    for estado in estados:  # Se recorren las ubicaciones de las empresas.
        Estado.append(estado.text)  # Se agrega a una lista.

    for descripcion in descripciones:  # Se recorren las descripciones de las empresas.
        if descripcion.text != '':  # Sólo si es distinto a nulo.
            Descripcion.append(descripcion.text)  # Se agrega a una lista.

    # print("Prueba: ", cont)
    # print("Nombre: ", len(nombres))
    # print("Estados: ", len(estados))
    # print("Descripciones: ", len(descripciones))
    # print("///////////////////////////////////")

    if i < 41:  # Si i es menor a 41.
        driver.get('https://mx.kompass.com/s/agricultura-y-alimentacion/01/page-' + str(i) + '/')  # Se obtiene la siguiente página.
        time.sleep(3)  # Se espera un tiempo.


driver.quit()  # Se detiene el driver.

# print(len(Nombre))
# print(len(Estado))
# print(len(Descripcion))

Nombres = []
Estados = []
Descripciones = []

# Se realiza la decodificación de toda la información y se guarda en una nueva lista.
for nombres in Nombre:
    Nombres.append(unidecode.unidecode(nombres))

for estados in Estado:
    Estados.append(unidecode.unidecode(estados))

for descripciones in Descripcion:
    Descripciones.append(unidecode.unidecode(descripciones))

# Se crea un DataFrame con la información decodificada.
df = pd.DataFrame({'Empresa': Nombres,
                   'Estado': Estados,
                   'Descripcion': Descripciones})

df.to_csv('WS_Kompass.csv', index=False)  # Se exporta a un archivo CSV.