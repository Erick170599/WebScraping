# Importar librerías.
import pandas as pd

data = pd.read_csv("UM_Universidades_Mexico.csv")

# --------------------------------------------------------------

Carreras = data['Oferta Educativa']

CarrerasUnicas = []

for i in range(len(Carreras)):
    if Carreras[i] not in CarrerasUnicas:
        CarrerasUnicas.append(Carreras[i])

df = pd.DataFrame({'Oferta Educativa': CarrerasUnicas})

df.to_csv('UM_Extaer_Carreras.csv', index=False)  # Se exporta a un archivo CSV.

# --------------------------------------------------------------

# Universidades = data['Nombre']
# Carreras = data['Oferta Educativa']
# Privacidad = data['Privacidad']
# Ubicaciones = data['Ubicacion']
# Origenes = data['Origen']
#
# df = pd.DataFrame({'Nombre': Universidades,
#                    'Ubicacion': Ubicaciones,
#                    'Privacidad': Privacidad,
#                    'Oferta Educativa': Carreras,
#                    'Origen': Origenes})
#
#
# TotalUni = []
#
# for i in Universidades:
#     if i not in TotalUni:
#         TotalUni.append(i)
#
# LisOfeEdu = []
# OfPriv = []
# for Uni in TotalUni:
#     OfeEdu = []
#     Priv = []
#     for j in range(len(Universidades)):
#         if Uni == Universidades[j]:
#             OfeEdu.append(Carreras[j])
#             Priv.append(Privacidad[j])
#     LisOfeEdu.append(OfeEdu)
#     lista = set(Priv)
#     OfPriv.append(lista)
#
#
# df = pd.DataFrame({'Universidad': TotalUni,
#                    'Privacidad': OfPriv,
#                    'Oferta Educativa': LisOfeEdu})
#
# df.to_csv('UM_Extraer_Universidades.csv', index=False)

# ----------------------------------------------------------------------

# df = data.groupby(by = ["Nombre"]).apply(','.join).reset_index()
#
# df.to_csv('UM_Extraer_Universidades1.csv', index=False)

# ----------------------------------------------------------------------

# print(data.iloc[0][0])  # Nombre
# print(data.iloc[0][1])  # Ubicacion
# print(data.iloc[0][2])  # Privacidad
# print(data.iloc[0][4])  # Origen
#
# Nombres = []
# Ubicaciones = []
# Privacidad = []
# Origenes = []
#
# for i in range(len(data)):
#     if data.iloc[i][0] not in Nombres:
#         Nombres.append(data.iloc[i][0])
#         Ubicaciones.append(data.iloc[i][1])
#         Privacidad.append(data.iloc[i][2])
#         Origenes.append(data.iloc[i][4])
#
# df = pd.DataFrame({'Nombre': Nombres,
#                    'Ubicacion': Ubicaciones,
#                    'Privacidad': Privacidad,
#                    'Origen': Origenes})
#
# df.to_csv('UM_Datos_Completos.csv', index=False)