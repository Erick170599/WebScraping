# Importar librerías.
import pandas as pd
import unidecode as unidecode
import time
from selenium import webdriver

website = 'https://universidadesdemexico.mx/Universidades/'  # Variable para guardar la URL (Payment gateways).
# website = 'https://universidadesdemexico.mx/universidades/multiversidad-mundo-real-edgar-morin'  # Variable para guardar la URL (Payment gateways).
path = 'C:/Users/Erick Lozano/Desktop/chromedriver_win32/chromedriver'  # Se obtiene de la ruta donde se aloja en la PC.

driver = webdriver.Chrome(path)  # Se utiliza el driver para abrir Chrome.
driver.get(website)  # Se obtiene la página.

Nombre = []
Ubicacion = []
Privacidad = []
OEducativa = []
Servicios = []
Links = []
Links2 = []

for Link in driver.find_elements_by_xpath('//div[@class="logo"]/div/a'):  # Se recorren los elementos.
    Links.append(Link.get_attribute('href'))  # Se obtienen los links y se agregan a una lista.

for link in Links:  # Se recorren los links extraídos.
    driver.get(link)  # Se ingresa al link.

    nombre = driver.find_element_by_xpath('//div[@class="col-md-7"]/h1')  # Se obtiene el nombre de la Universidad.
    try:
        ubicacion1 = driver.find_element_by_xpath('//tr[2]/td[2]').text  # Se obtiene la dirección.
    except:
        ubicacion1 = 'Error'
    try:
        ubicacion2 = driver.find_element_by_xpath('//tr[3]/td[2]').text  # Se obtiene la ciudad.
    except:
        ubicacion2 = 'Error'
    ubicacion3 = ubicacion1 + ", " + ubicacion2 + ", Mexico."  # Se junta la ubicación completa.
    privacidad = driver.find_element_by_xpath('//tr[1]/td[2]')  # Se obtiene el tipo de Universidad.

    oeducativa = []
    for oEducativa in driver.find_elements_by_xpath('//ul[@class="list-listings"]/li/div/div/h2/a/h2'):  # Se recorren los elementos.
        oeducativa.append(oEducativa.text)  # Se agregan cada una de las Ofertas educativas.

    if len(oeducativa) > 0:  # Si la lista tiene elementos.
        ofertaEdu = set(oeducativa)  # Se eliminan duplicados.
        for ofertaedu in ofertaEdu:  # Se recorren las Ofertas Educativas.
            Nombre.append(nombre.text)  # Se agrega el Nombre.
            Ubicacion.append(ubicacion3)  # Se agrega la Ubicación.
            Privacidad.append(privacidad.text)  # Se agrega la Privacidad.
            OEducativa.append(ofertaedu)  # Se agrega cada Oferta Educativa.
            Links2.append(link)  # Se agrega el Link.
    else:
        Nombre.append(nombre.text)  # Se agrega el Nombre.
        Ubicacion.append(ubicacion3)  # Se agrega la Ubicación.
        Privacidad.append(privacidad.text)  # Se agrega la Privacidad.
        OEducativa.append("")  # Se agrega cada Oferta Educativa.
        Links2.append(link)  # Se agrega el Link.

driver.quit()  # Se cierra el driver.


NombreX = []
UbicacionX = []
PrivacidadX = []
OEducativaX = []

# Se realiza la decodificación de toda la información y se guarda en una nueva lista.
for nombrex in Nombre:
    NombreX.append(unidecode.unidecode(nombrex))

for ubicacionx in Ubicacion:
    UbicacionX.append(unidecode.unidecode(ubicacionx))

for privacidadx in Privacidad:
    PrivacidadX.append(unidecode.unidecode(privacidadx))

for oeducativax in OEducativa:
    OEducativaX.append(unidecode.unidecode(oeducativax))

# Se crea un DataFrame con la información decodificada.
df = pd.DataFrame({'Nombre': NombreX,
                   'Ubicacion': UbicacionX,
                   'Privacidad': PrivacidadX,
                   'Oferta Educativa': OEducativaX,
                   'Origen': Links2})

df.to_csv('UM_Universidades_Mexico.csv', index=False)  # Se exporta a un archivo CSV.