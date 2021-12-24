# Importar librerías.
import pandas as pd

data = pd.read_csv("UM_Universidades_Mexico.csv")

# --------------------------------------------------------------

# Carreras = data['Oferta Educativa']
#
# OfertaEdu = set(Carreras)
# OfertaEdu.pop()
#
# OfertaEDU = []
# for i in OfertaEdu:
#     OfertaEDU.append(i)
#
# df = pd.DataFrame({'Oferta Educativa': OfertaEDU})
#
# df.to_csv('UM_Extaer_Carreras.csv', index=False)  # Se exporta a un archivo CSV.

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



df = data.groupby(by = ["Nombre"]).apply(','.join).reset_index()

df.to_csv('UM_Extraer_Universidades1.csv', index=False)