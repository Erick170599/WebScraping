import pandas as pd
import time
import unidecode as unidecode

# file = pd.read_csv("WEB_SCRAPING_GENERAL.csv")  # Se lee el archivo.
#
# ubicacion = file.iloc[:, 2]  # Se obtiene la fila "Ubicacion".
#
# Ubicacion = []
#
# for ubi in ubicacion:  # Se recorren las ubicaciones existentes.
#     if 'D.C.' in ubi:  # Si se encuentra la cadena entonces...
#         palabras = ubi.split(",")  # Se separan las palabras a partir de las comas.
#         Ubicacion.append(palabras[0])  # Se agrega la 1era palabra de la ubicacion.
#     else:
#         Ubicacion.append(ubi)  # Se agrega la ubicacion tal y como estaba.
#
#
# Ubicacion2 = []
# for Ubi in Ubicacion:  # Se recorren las ubicaciones resultantes.
#     guion = Ubi.split("-")  # Se separan las palabras a partir del guion medio.
#     if len(guion) == 2:  # Si se encuentran 2 elementos entonces...
#         Ubicacion2.append(guion[0]+","+guion[1])  # Se agrega la ubicacion pero separada por coma.
#     else:
#         Ubicacion2.append(Ubi)  # Se agrega la ubicacion tal y como estaba.
#
#
# UbicacionCompleta = []
# for i in range(len(file)):  # for dependiendp al número de filas.
#     if Ubicacion2[i].endswith(file.iloc[i, 5]):  # Si la ubicación tiene el país al final entonces...
#         UbicacionCompleta.append(Ubicacion2[i])  # Se agrega la ubicación normal.
#     else:
#         UbicacionCompleta.append(Ubicacion2[i] + ', ' + file.iloc[i, 5])  # Se agrega la ubicación con el país.
#
#
# Nombres = file.iloc[:, 0]  # Nombres de las empresas.
# Areas = file.iloc[:, 1]  # Areas a que se dedican.
# Descripciones = file.iloc[:, 3]  # Descripciones de las empresas.
# Origenes = file.iloc[:, 4]  # Link de donde proviene.
# Paises = file.iloc[:, 5]  # País de origen.
#
#
# Ubicaciones = []
# for ubicacionx in UbicacionCompleta:
#     Ubicaciones.append(unidecode.unidecode(ubicacionx))

# df = pd.DataFrame({'Empresa': Nombres,
#                    'Area': Areas,
#                    'Ubicacion': Ubicaciones,
#                    'Descripcion': Descripciones,
#                    'Origen': Origenes,
#                    'Pais': Paises})
#
# df.to_csv('Resolución_Ubicacion.csv', index=False)

#########################################################

linkedlin = pd.read_csv("_new folder (3).csv")  # Se lee el archivo.

Nombres1 = linkedlin.iloc[:, 2]  # Nombres de las empresas.
Areas1 = linkedlin.iloc[:, 4]  # Areas a que se dedican.
Ubicaciones1 = linkedlin.iloc[:, 6]  # Ubicación de la empresa.
Descripciones1 = linkedlin.iloc[:, 3]  # Descripciones de las empresas.
Origenes1 = linkedlin.iloc[:, 1]  # Link de donde proviene.

Paises1 = []
for ubicaciones in Ubicaciones1:  # Se recorren las ubicaciones.
    pais = ubicaciones.split(",")  # Se separan con referencia a la coma.
    Paises1.append(pais[-1])  # Se agrega el último objeto de la lista.


# Nombres2 = []
# Areas2 = []
# Ubicaciones2 = []
# Descripciones2 = []
# Origenes2 = []
# Paises2 = []
#
# for nombresx in Nombres1:
#     Nombres2.append(unidecode.unidecode(nombresx))
# for areasx in Areas1:
#     Areas2.append(unidecode.unidecode(areasx))
# for ubicacionesx in Ubicaciones1:
#     Ubicaciones2.append(unidecode.unidecode(ubicacionesx))
# for descripcionesx in Descripciones1:
#     Descripciones2.append(unidecode.unidecode(descripcionesx))
# for origenesx in Origenes1:
#     Origenes2.append(unidecode.unidecode(origenesx))
# for paisesx in Paises1:
#     Paises2.append(unidecode.unidecode(paisesx))

df1 = pd.DataFrame({'Empresa': Nombres1,
                   'Area': Areas1,
                   'Ubicacion': Ubicaciones1,
                   'Descripcion': Descripciones1,
                   'Origen': Origenes1,
                   'Pais': Paises1})

df1.to_csv('Resolución_Ubicacion1.csv', index=False)