import re

import requests
import pandas as pd
from bs4 import BeautifulSoup

Fecha = list()
PIB_eur = list()
PIB_dol = list()
Var_PIB = list()

url = 'https://datosmacro.expansion.com/pib/ecuador'

# obtengo la pagina a analizar
html_doc = requests.get(url)
soup = BeautifulSoup(html_doc.text, 'html.parser')
tabla = soup.find('table', attrs={'class':'table tabledat table-striped table-condensed table-hover'})

filas = tabla.find_all('tr')
for fila in filas:
    celdas = fila.find_all('td')
    if len(celdas) > 0:
        fecha = celdas[0].string
        pib_eur = re.sub(r'[^\d.]', '', str(celdas[1].string))
        pib_dol = re.sub(r'[^\d.]', '', str(celdas[2].string))
        var_pib = celdas[3].string
        Fecha.append(fecha)
        PIB_eur.append(pib_eur)
        PIB_dol.append(pib_dol)
        Var_PIB.append(var_pib)

df = pd.DataFrame({'Fecha': Fecha, 'PIB Anual (eur)': PIB_eur, 'PIB Anual (dol)': PIB_dol, 'Var PIB (%)': Var_PIB})
df.to_csv('pib.csv', index=False, encoding='utf-8')


# fecha_list = tabla.find_all(attrs={'class': 'fecha'})
# pib_anual_list = tabla.find_all(attrs={'class':'numero eur'})
# var_pib_list = tabla.find_all(attrs={'class':'numero dol'})
#
# for fecha in fecha_list:
#     # print(fecha.text)
#     Fecha.append(fecha.text)
# for pib_anual in pib_anual_list:
#     # print(pib_anual.text)
#     PIB_anual.append(pib_anual.text)
# for var_pib in var_pib_list:
#     # print(var_pib.text)
#     Var_PIB.append(var_pib.text)
#
# df = pd.DataFrame({'Fecha':Fecha, 'Producto Interno Bruto Anual':PIB_anual, 'Var PIB (%)':Var_PIB})
# df.to_csv('pib.csv', index=False, encoding='utf-8')
