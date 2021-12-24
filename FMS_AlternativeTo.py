# Importar librerías.
import pandas as pd
import time
from selenium import webdriver

# website = 'https://alternativeto.net/browse/search?q=Farm+Management+Software'  # Variable para guardar la URL (Farm Management Software).
# website = 'https://alternativeto.net/browse/search?q=Photo+editing'  # Variable para guardar la URL (Photo editing).
# website = 'https://alternativeto.net/browse/search?q=Video+editing'  # Variable para guardar la URL (Video editing).
# website = 'https://alternativeto.net/browse/search?q=Audio+editing'  # Variable para guardar la URL (Audio editing).
# website = 'https://alternativeto.net/browse/search?q=E-commerce+site+builders'  # Variable para guardar la URL (E-commerce site builders).
# website = 'https://alternativeto.net/browse/search?q=Website+builders'  # Variable para guardar la URL (Website builders).
website = 'https://alternativeto.net/browse/search?q=Payment+gateways'  # Variable para guardar la URL (Payment gateways).
path = 'C:/Users/Erick Lozano/Desktop/chromedriver_win32/chromedriver'  # Se obtiene de la ruta donde se aloja en la PC.

driver = webdriver.Chrome(path)  # Se utiliza el driver para abrir Chrome.
driver.get(website)  # Se obtiene la página.

Application = []
Description = []
URL = []
Links = []

# for i in range(5):  # Se recorren (Farm Management Software).
# for i in range(16):  # Se recorren (Photo editing).
# for i in range(22):  # Se recorren (Video editing).
# for i in range(15):  # Se recorren (Audio editing).
# for i in range(1):  # Se recorren (E-commerce site builders).
# for i in range(14):  # Se recorren (Website builders).
for i in range(8):  # Se recorren (Payment gateways).
    for link in driver.find_elements_by_xpath('//h3/a[@data-link-action="Search"]'):  # Se recorren los elementos.
        Links.append(link.get_attribute('href'))  # Se obtienen los links y se agrega a una lista.

    # if i < 5:  # Para (Farm Management Software).
    # if i < 16:  # Para (Photo editing).
    # if i < 22:  # Para (Video editing).
    # if i < 15:  # Para (Audio editing).
    # if i < 1:  # Para (E-commerce site builders).
    # if i < 14:  # Para (Website builders).
    if i < 8:  # Para (Payment gateways).
        driver.find_element_by_link_text('Next').click()  # Da click en Next.


for Link in Links:  # Se recorren los links extraídos.
    driver.get(Link)  # Se ingresa al link.

    driver.find_element_by_xpath('//nav[@data-testid="tab-bar"]/a[1]').click()  # Se da click para ver la info de la herramienta.
    time.sleep(5)

    application = driver.find_element_by_xpath('//h1[@class="Heading_h1__3q_I-"]')  # Se obtiene el nombre de la herramienta.
    Application.append(application.text)  # Se agrega a una lista.

    try:
        description = driver.find_element_by_xpath('//div[3]/div[1]/div[1]/div[2]/span')  # Se obtiene la descripción de la herramienta.
        Description.append(description.text)  # Se agrega a una lista.
    except:
        Description.append("")

    url = driver.find_element_by_xpath('//a[@target="_blank"]')  # Se obtiene la URL oficial de la herramienta.
    URL.append(url.get_attribute('href'))  # Se agrega a una lista.

driver.quit()  # Se cierra el driver.

# Se crea un DataFrame con la información.
df = pd.DataFrame({'Application': Application,
                   'Description': Description,
                   'URL': URL,
                   'Origin': Links})

# df.to_csv('FMS_AlternativeTo_Farm.csv', index=False)  # Se exporta a un archivo CSV (Farm Management Software).
# df.to_csv('FMS_AlternativeTo_Photo.csv', index=False)  # Se exporta a un archivo CSV (Photo editing).
# df.to_csv('FMS_AlternativeTo_Video.csv', index=False)  # Se exporta a un archivo CSV (Video editing).
# df.to_csv('FMS_AlternativeTo_Audio.csv', index=False)  # Se exporta a un archivo CSV (Audio editing).
# df.to_csv('FMS_AlternativeTo_E-commerce.csv', index=False)  # Se exporta a un archivo CSV (E-commerce site builders).
# df.to_csv('FMS_AlternativeTo_Website.csv', index=False)  # Se exporta a un archivo CSV (Website builders).
df.to_csv('FMS_AlternativeTo_Payment.csv', index=False)  # Se exporta a un archivo CSV (Payment gateways).
