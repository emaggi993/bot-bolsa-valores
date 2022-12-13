import requests
from bs4 import BeautifulSoup
from modulos.Fecha import Fecha
from modulos.funciones import get_url, listar_fechas
import wget


fecha = Fecha("11/09/2022")
fin = Fecha("15/10/2022")
print(listar_fechas(fecha, fin))

url = get_url(fecha)
respuesta = requests.get(url)
contenido = BeautifulSoup(respuesta.text, "html.parser")
archivos = contenido.find_all('a', class_="link-dark")
print(url)
for link in archivos:
    print(link['href'])
    extencion = link['href'][-3:]
    if extencion == 'xls':
        descarga = link['href']
        local_file = f"BV-{fecha.anio}-{fecha.mes}-{fecha.dia}.xls"
        wget.download(descarga, local_file)

