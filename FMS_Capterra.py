# Importar librerias.
import pandas as pd
import time
from selenium import webdriver

website = 'https://www.capterra.com/farm-management-software/'  # Variable para guardar la URL.
# website = 'https://www.capterra.com/p/142602/Granular/'  # Variable para guardar la URL.
path = 'C:/Users/Erick Lozano/Desktop/chromedriver_win32/chromedriver'  # Se obtiene de la ruta donde se aloja en la PC.

driver = webdriver.Chrome(path)  # Se utiliza el driver para abrir Chrome.
driver.get(website)  # Se obtiene la página.

Application = []
Description = []
URL = []
Localitation = []

for i in range(11):  # Se hace un corrimiento para cargar todos los datos.
    siguiente = driver.find_element_by_xpath('//button/div[@class="Button__CenteredText-sc-2779at-4 eJUWuq"]').click()  # Se da clic en el botón para cargar más datos.
    time.sleep(1)  # Se espera un tiempo.

Links = []
LinksUnicos = []

for a in driver.find_elements_by_class_name('nb-button'):  # Recorrer los elemntos de la clase.
    Links.append(a.get_attribute('href'))  # Extraer los Links y guardarlos en una lista.

# LinksUnicos.append(pd.unique(Links))
# LinksUnicos.append(set(Links))

for link in Links:  # Se recorren los Links.
    if link not in LinksUnicos:  # Se crea un filtro para no aceptar repetidos.
        LinksUnicos.append(link)  # Se agrega a una nueva lista.

LinksLimpios = list(filter(None, LinksUnicos))  # Se quitan los valores None.

for linklimpio in LinksLimpios:  # Se recorren los links.
    driver.execute_script("window.open('');")  # Se abre una nueva pestaña.
    driver.switch_to.window(driver.window_handles[1])  # Se coloca sobre la nueva pestaña.
    driver.get(linklimpio)  # Se abren el link en la nueva pestaña.

    application = driver.find_element_by_xpath('//div/h1[@data-test-id="ProductHeader__Nimbus_ProductHeading"]')
    Application.append(application.text)

    description = driver.find_element_by_xpath('//div[@id="LoadableProductSummary"]/div/div/div/div/div')
    Description.append(description.text)

    url = driver.find_element_by_xpath('//*[@id="LoadableProductSummary"]/div/div[2]/div/div[4]/ul/li[4]/span')
    URL.append(url.text)

    localitation = driver.find_element_by_xpath('//*[@id="LoadableProductSummary"]/div/div[2]/div/div[4]/ul/li[2]/span')
    Localitation.append(localitation.text)


    driver.close()  # Se cierra la pestaña.

    driver.switch_to.window(driver.window_handles[0])  # Se coloca sobre la pestaña principal.

driver.quit()  # Se cierra el driver.

df = pd.DataFrame({'Application': Application,
                   'Description': Description,
                   'URL': URL,
                   'Localitation': Localitation})

df.to_csv('FMS_Capterra.csv', index=False)