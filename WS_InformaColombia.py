import unidecode as unidecode
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import random
import time

website = 'https://www.informacolombia.com/directorio-empresas/actividad/A_AGRICULTURA-GANADERIA-CAZA-SILVICULTURA-Y-PESCA'
path = 'C:/Users/Erick Lozano/Desktop/chromedriver_win32/chromedriver'

driver = webdriver.Chrome(path)
driver.get(website)

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
    driver.get('https://www.informacolombia.com/directorio-empresas/actividad/A_AGRICULTURA-GANADERIA-CAZA-SILVICULTURA-Y-PESCA?qPg=' + str(i))
    time.sleep(random.randint(4, 6))

    IdenNombre = []
    for a in range(10):  # Es para recorrer la tabla.
        a = a + 2
        idenNombre = driver.find_element_by_xpath('/html/body/div[1]/div[1]/table/tbody/tr[' + str(a) + ']/td[1]')
        IdenNombre.append(idenNombre.text)

    for j in IdenNombre:  # Se usa para recorrer la lista de los nombres de las empresas.
        driver.find_element_by_link_text(j).click()
        time.sleep(random.randint(4, 6))

        nombre = driver.find_element_by_xpath('//*[@id="ficha"]/div[2]/table/tbody/tr[1]/td')
        Nombre.append(nombre.text)
        ciudad = driver.find_element_by_xpath('//*[@id="ficha"]/div[2]/table/tbody/tr[3]/td')
        Ciudad.append(ciudad.text)
        departamento = driver.find_element_by_xpath('//*[@id="ficha"]/div[2]/table/tbody/tr[4]/td')
        Departamento.append(departamento.text)
        telefono = driver.find_element_by_xpath('//*[@id="ficha"]/div[2]/table/tbody/tr[2]/td')
        Telefono.append(telefono.text)
        direccion = driver.find_element_by_xpath('//*[@id="ficha"]/div[2]/table/tbody/tr[5]/td')
        Direccion.append(direccion.text)
        actividad = driver.find_element_by_xpath('//*[@id="ficha"]/div[2]/table/tbody/tr[7]/td')
        Actividad.append(actividad.text)

        driver.back()
        time.sleep(random.randint(4, 6))

    # if i <= 199:
    #     driver.get('https://www.informacolombia.com/directorio-empresas/actividad/A_AGRICULTURA-GANADERIA-CAZA-SILVICULTURA-Y-PESCA?qPg=' + str(i))
    #     time.sleep(random.randint(4, 6))
    # else:
    #     break
driver.quit()

Nombres = []
Ciudades = []
Departamentos = []
Telefonos = []
Direcciones = []
Actividades = []

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

df = pd.DataFrame({'Empresa': Nombres,
                    'Ciudad': Ciudades,
                    'Departamento': Departamentos,
                    'Telefono': Telefonos,
                    'Direccion': Direcciones,
                    'Actividad': Actividades})

df.to_csv('WS_InformaColombia1.csv', index=False)