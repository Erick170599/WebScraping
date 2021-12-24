# Importar líbrerías.
import unidecode as unidecode
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import random
import time

website = 'https://www.informacolombia.com/directorio-empresas/actividad/A_AGRICULTURA-GANADERIA-CAZA-SILVICULTURA-Y-PESCA'  # Variable para guardar la URL.
path = 'C:/Users/Erick Lozano/Desktop/chromedriver_win32/chromedriver'  # Se obtiene de la ruta donde se aloja en la PC.

driver = webdriver.Chrome(path)  # Se utiliza el driver para abrir Chrome.
driver.get(website)  # Se obtiene la página.

Nombre = []
Ciudad = []
Departamento = []
Telefono = []
Direccion = []
Actividad = []

# for i in range(10):
#     i = i + 2
#     nombre = driver.find_element_by_xpath('/html/body/div[1]/div[1]/table/tbody/tr[' + str(i) + ']/td[1]')
#     Nombre.append(nombre.text)
#     localidad = driver.find_element_by_xpath('/html/body/div[1]/div[1]/table/tbody/tr[' + str(i) + ']/td[2]')
#     Localidad.append(localidad.text)
#     departamento = driver.find_element_by_xpath('/html/body/div[1]/div[1]/table/tbody/tr[' + str(i) + ']/td[3]')
#     Departamento.append(departamento.text)
#     telefono = driver.find_element_by_xpath('/html/body/div[1]/div[1]/table/tbody/tr[' + str(i) + ']/td[4]')
#     Telefono.append(telefono.text)
#
# for a in range(5): #199
#     a = a + 2
#     driver.get('https://www.informacolombia.com/directorio-empresas/actividad/A_AGRICULTURA-GANADERIA-CAZA-SILVICULTURA-Y-PESCA?qPg=' + str(a))
#     time.sleep(5)
#
# for z in Nombre:
#     driver.find_element_by_link_text(z).click()
#     time.sleep(4)
#     driver.back()
#     time.sleep(5)

for i in range(10):  # 199  Es para ver todas las páginas.
    # i = i + 2

    i = i + 31
    driver.get('https://www.informacolombia.com/directorio-empresas/actividad/A_AGRICULTURA-GANADERIA-CAZA-SILVICULTURA-Y-PESCA?qPg=' + str(i))  # Se obtiene una nueva página dependiendo al cantador.
    time.sleep(random.randint(4, 6))  # Se espera entre 4 a 6 seg.

    IdenNombre = []
    for a in range(10):  # Es para recorrer la tabla.
        a = a + 2
        idenNombre = driver.find_element_by_xpath('/html/body/div[1]/div[1]/table/tbody/tr[' + str(a) + ']/td[1]')  # Con el Xpath se guarda el nombre de la empresa.
        IdenNombre.append(idenNombre.text)  # Se agrega a una lista.

    for j in IdenNombre:  # Se usa para recorrer la lista de los nombres de las empresas.
        driver.find_element_by_link_text(j).click()  # Da click sobre el nombre de la empresa.
        time.sleep(random.randint(4, 6))  # Se espera un tiempo.

        nombre = driver.find_element_by_xpath('//*[@id="ficha"]/div[2]/table/tbody/tr[1]/td')  # Con el Xpath se extrae el nombre de la empresa.
        Nombre.append(nombre.text)  # Se agrega a una lista.
        ciudad = driver.find_element_by_xpath('//*[@id="ficha"]/div[2]/table/tbody/tr[3]/td')  # Con el Xpath se extrae la ubicación de la empresa.
        Ciudad.append(ciudad.text)  # Se agrega a una lista.
        departamento = driver.find_element_by_xpath('//*[@id="ficha"]/div[2]/table/tbody/tr[4]/td')  # Con el Xpath se extrae el departamento al que pertenece.
        Departamento.append(departamento.text)  # Se agrega a una lista.
        telefono = driver.find_element_by_xpath('//*[@id="ficha"]/div[2]/table/tbody/tr[2]/td')  # Con el Xpath se extrae el telefono de la empresa.
        Telefono.append(telefono.text)  # Se agrega a una lista.
        direccion = driver.find_element_by_xpath('//*[@id="ficha"]/div[2]/table/tbody/tr[5]/td')  # Con el Xpath se extrae la dirección de la empresa.
        Direccion.append(direccion.text)  # Se agrega a una lista.
        actividad = driver.find_element_by_xpath('//*[@id="ficha"]/div[2]/table/tbody/tr[7]/td')  # Con el Xpath se extrae la actividad que hace la empresa.
        Actividad.append(actividad.text)  # Se agrega a una lista.

        driver.back()  # Se regresa a la anterior página.
        time.sleep(random.randint(4, 6))  # Se espera un tiempo.

    # if i <= 199:
    #     driver.get('https://www.informacolombia.com/directorio-empresas/actividad/A_AGRICULTURA-GANADERIA-CAZA-SILVICULTURA-Y-PESCA?qPg=' + str(i))
    #     time.sleep(random.randint(4, 6))
    # else:
    #     break
driver.quit()  # Se detiene el driver.

Nombres = []
Ciudades = []
Departamentos = []
Telefonos = []
Direcciones = []
Actividades = []

# Se realiza la decodificación de toda la información y se guarda en una nueva lista.
for nombresx in Nombre:
    Nombres.append(unidecode.unidecode(nombresx))

for ciudadesx in Ciudad:
    Ciudades.append(unidecode.unidecode(ciudadesx))

for departamentosx in Departamento:
    Departamentos.append(unidecode.unidecode(departamentosx))

for telefonosx in Telefono:
    Telefonos.append(unidecode.unidecode(telefonosx))

for direccionesx in Direccion:
    Direcciones.append(unidecode.unidecode(direccionesx))

for actividadesx in Actividad:
    Actividades.append(unidecode.unidecode(actividadesx))

# Se crea un DataFrame con la información decodificada.
df = pd.DataFrame({'Empresa': Nombres,
                    'Ciudad': Ciudades,
                    'Departamento': Departamentos,
                    'Telefono': Telefonos,
                    'Direccion': Direcciones,
                    'Actividad': Actividades})

df.to_csv('WS_InformaColombia1.csv', index=False)  # Se exporta a un archivo CSV.