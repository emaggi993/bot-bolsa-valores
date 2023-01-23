import modulos.funciones as fn
import modulos.Datos as Datos
import modulos.conexion as conexion
def test_descarga():
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

def test_fecha_archivo():
    
    archivo= "./datos/BVA-2022-01-02.xls"
    print(fn.date_for_filename(archivo))
def test_union():
    carpeta= './datos/'
    archivos = fn.listar_archivos_bva('./datos/')
    # print(archivos)
    for archivo in archivos:
        data = Datos.get_data(carpeta + archivo, "Operaciones")
        for index, datos in enumerate(data):
            if index == 0:
                fn.borrar_registro_fecha(fn.date_for_filename(archivo), "renta_fija")
                fn.respaldar_datos(datos, "renta_fija")
            elif index == 1:
                fn.borrar_registro_fecha(fn.date_for_filename(archivo), "renta_variable")
                fn.respaldar_datos(datos, "renta_variable")
            elif index == 2:
                fn.borrar_registro_fecha(fn.date_for_filename(archivo), "repos")
                fn.respaldar_datos(datos, "repos")
            elif index == 3:
                fn.borrar_registro_fecha(fn.date_for_filename(archivo), "total_renta_detalle")
                fn.respaldar_datos(datos, "total_renta_detalle")
if __name__=="__main__":
    test_union()
    



