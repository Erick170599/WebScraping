import pandas as pd

# cadenas = ['hola lola', 'hola lo la, que tal', 'Bienvenidos HOLA', 'maholalola', 'Como estas']
# palabras = ['hola', 'hola lola']
#
# for i in cadenas:
#     minusculas = i.lower()
#     for j in palabras:
#         Resultado = minusculas.find(j)
#         if Resultado > -1:
#             print(i)
#         print(Resultado)


data = pd.read_csv("DB CurrentUsedTechs by Paisajes Andinos  - Complete.csv")  # Se lee el archivo.
dataaudio = pd.read_csv("FMS_AlternativeTo_Audio.csv")  # Se lee el archivo.
dataecommerce = pd.read_csv("FMS_AlternativeTo_E-commerce.csv")  # Se lee el archivo.
datafarm = pd.read_csv("FMS_AlternativeTo_Farm.csv")  # Se lee el archivo.
datapayment = pd.read_csv("FMS_AlternativeTo_Payment.csv")  # Se lee el archivo.
dataphoto = pd.read_csv("FMS_AlternativeTo_Photo.csv")  # Se lee el archivo.
datavideo = pd.read_csv("FMS_AlternativeTo_Video.csv")  # Se lee el archivo.
datawebsite = pd.read_csv("FMS_AlternativeTo_Website.csv")  # Se lee el archivo.

ApplicationOrigin = data['Application']
NombreAudio = dataaudio['Application']

Checar = []

for i in NombreAudio:
    cont = 0
    minusculas = i.__str__().lower()
    for j in ApplicationOrigin:
        minusculasAPP = j.__str__().lower()
        Resultado = minusculas.find(minusculasAPP)
        if Resultado == -1:
            cont = cont + 1
    if cont < len(ApplicationOrigin):
        Checar.append(i)
    else:
        Checar.append("")


df = pd.DataFrame({'Original': NombreAudio,
                   'Checar': Checar})

df.to_csv('Prueba.csv')