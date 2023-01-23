from PySide6.QtWidgets import QWidget

from views.download_window import DownloadWindow
from views.general_custom_ui import GeneralCustomUi
from modulos.Fecha import Fecha
from modulos.funciones import listar_fechas, get_url
from bs4 import BeautifulSoup
import requests
import wget
from controllers.resultados_windows import ResultadoWidget
from datetime import datetime
class DownloadWindowsForm(QWidget, DownloadWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.set_buttons()

    
    def mousePressEvent(self, event) -> None:
        self.ui.mouse_press_event(event)

    def set_buttons(self):
        self.BTNIniciar.clicked.connect( self.iniciar)
    
    def iniciar(self):
        fecha_inicio = Fecha(self.FechaDesde.text())
        fecha_fin = Fecha(self.FechaHasta.text())
        fechas = listar_fechas(fecha_inicio, fecha_fin)
        # print(fechas)
        total = len(fechas)
        resultados=[]
        inicio = datetime.now()
        for index, f in enumerate(fechas):
            try:
                fecha = Fecha(f)
                url = get_url(fecha)
                respuesta = requests.get(url)
                contenido = BeautifulSoup(respuesta.text, "html.parser")
                archivos = contenido.find_all('a', class_="link-dark")
                print(url)
                aux = {"fecha": str(fecha), "cantidad": len(archivos), "pdf": 0, "xls": 0}

                for link in archivos:
                    # print(link['href'])
                    extencion = link['href'][-3:]
                    if extencion== 'pdf':
                        aux['pdf'] += 1
                    if extencion == 'xls':
                        descarga = link['href']
                        print(descarga)
                        local_file = f"datos/BVA-{fecha.anio}-{fecha.mes}-{fecha.dia}.xls"
                        wget.download(descarga, local_file)
                        aux['xls'] += 1
                resultados.append(aux)
                self.PBEstado.setValue( int(((index+1) / total)*100) )
            except Exception as e:
                print("*"*10,"Ha ocurrido un error \n","*"*10,str(e))
        fin = datetime.now()
        dif = fin - inicio
        # tiempo= dif.strftime('%H:%M:%S' )
        self.LabelError.setText(str(dif))
        print(resultados)
        window = ResultadoWidget()
        window.setDataTable(resultados)
        window.show()
    