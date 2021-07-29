import unidecode as unidecode
from selenium import webdriver
import pandas as pd
import time

website = 'https://www.computrabajo.com.ec/empresas/empresas-de-agricultura-y-pesca-y-ganaderia'  # Variable para guardar la URL.
path = 'C:/Users/Erick Lozano/Desktop/chromedriver_win32/chromedriver'  # Se obtiene de la ruta donde se aloja en la PC.

driver = webdriver.Chrome(path)  # Se utiliza el driver para abrir Chrome.
driver.get(website)  # Se obtiene la página.

Empresa = []
Area = []
Ubicacion = []
Descripcion = []

for i in range(38):

    empresas = driver.find_elements_by_xpath('//a[@class="js-o-link"]')  # Se obtienen los nombres de las empresas.
    areas = driver.find_elements_by_tag_name('h3')  # Se obtienen el area donde se desarrolla la empresa.
    ubicaciones = driver.find_elements_by_xpath('//article/div/div[2]/ul/li[2]')  # Se obtienen las ubicaciones de las empresas.

    for empresa in empresas:  # Se recorren los nombres.
        Empresa.append(empresa.text)  # Se agrega a una lista.

    for area in areas:  # Se recorren las areas.
        Area.append(area.text)  # Se agrega a una lista.

    for ubicacion in ubicaciones:  # Se recorren las ubicaciones.
        if ubicacion.text != '':  # Pasa si es distinto a vacio.
            Ubicacion.append(ubicacion.text)  # Se agrega a una lista.
        else:
            Ubicacion.append('---')  # Se agrega a una lista.

    Links = []
    for a in driver.find_elements_by_xpath('//a[@class="js-o-link"]'):  # Se recorre los elementos de la clase.
        Links.append(a.get_attribute('href'))  # Se obtienen los links y se agrega a una lista.

    for link in Links:  # Se recorren los links.
        driver.execute_script("window.open('');")  # Se abre una nueva pestaña.
        driver.switch_to.window(driver.window_handles[1])  # Se coloca sobre la nueva pestaña.
        driver.get(link)  # Se abren el link en la nueva pestaña.
        #time.sleep(3)  # Esperar 3 seg.

        try:
            driver.find_element_by_xpath('//a[@title="La empresa"]').click()  # Se da click sobre "La empresa".
            time.sleep(1)  # Esperar 2 seg.

            DesParcial = []
            descripciones = driver.find_elements_by_tag_name('p')  # Se extraen los elementos "p".
            for descripcion in descripciones:  # Se recorren los elemntos obtenidos.
                DesParcial.append(descripcion.text)  # Se agrega a una lista.
            Descripcion.append(DesParcial[12])  # Se obtiene y se agrega el elemento en la posicion 12.

        except:
            Descripcion.append('---')

        driver.close()  # Se cierra la pestaña.

        driver.switch_to.window(driver.window_handles[0])  # Se coloca sobre la pestaña principal.
        #time.sleep(3)  # Esperar 3 seg.

    if i < 37:
        driver.find_element_by_xpath('//a[@rel="next"]').click()  # Dar click para pasar a la siguiente pagina.

driver.quit()  # Se cierra el driver.


Empresas = []
Areas = []
Ubicaciones = []
Descripciones = []

for empresasx in Empresa:
    Empresas.append(unidecode.unidecode(empresasx))

for areasx in Area:
    Areas.append(unidecode.unidecode(areasx))

for ubicacionesx in Ubicacion:
    Ubicaciones.append(unidecode.unidecode(ubicacionesx))

for descripcionesx in Descripcion:
    Descripciones.append(unidecode.unidecode(descripcionesx))

df = pd.DataFrame({'Empresa': Empresas,
                   'Area': Areas,
                   'Ubicacion': Ubicaciones,
                   'Descripcion': Descripciones})

df.to_csv('WS_CompuTrabajoECU.csv', index=False)