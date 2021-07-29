import unidecode as unidecode
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

website = 'https://mx.kompass.com/s/agricultura-y-alimentacion/01/'
path = 'C:/Users/Erick Lozano/Desktop/chromedriver_win32/chromedriver'

driver = webdriver.Chrome(path)
driver.get(website)

Nombre = []
Estado = []
Descripcion = []
cont = 0
for i in range(40):
    i = i + 2

    nombres = driver.find_elements_by_xpath('//span[@class="titleSpan"]')
    estados = driver.find_elements_by_xpath('//a/span[@class="flagWorld"]')
    descripciones = driver.find_elements_by_class_name('details')
    cont = cont + 1

    for nombre in nombres:
        Nombre.append(nombre.text)

    for estado in estados:
        Estado.append(estado.text)

    for descripcion in descripciones:
        if descripcion.text != '':
            Descripcion.append(descripcion.text)

    print("Prueba: ", cont)
    print("Nombre: ", len(nombres))
    print("Estados: ", len(estados))
    print("Descripciones: ", len(descripciones))
    print("///////////////////////////////////")

    if i < 41:
        driver.get('https://mx.kompass.com/s/agricultura-y-alimentacion/01/page-' + str(i) + '/')
        time.sleep(3)


driver.quit()

print(len(Nombre))
print(len(Estado))
print(len(Descripcion))

Nombres = []
Estados = []
Descripciones = []

for nombres in Nombre:
    Nombres.append(unidecode.unidecode(nombres))

for estados in Estado:
    Estados.append(unidecode.unidecode(estados))

for descripciones in Descripcion:
    Descripciones.append(unidecode.unidecode(descripciones))

df = pd.DataFrame({'Empresa': Nombres,
                   'Estado': Estados,
                   'Descripcion': Descripciones})

df.to_csv('WS_Kompass.csv', index=False)