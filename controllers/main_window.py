from PySide6.QtWidgets import QWidget

from views.main_window import MainWindow
from views.general_custom_ui import GeneralCustomUi
from controllers.dowload_window import DownloadWindowsForm
from controllers.union_window import UnionWindow
from bs4 import BeautifulSoup
import requests
import wget
from controllers.resultados_windows import ResultadoWidget
from datetime import datetime
class MainWidowsForm(QWidget, MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.set_buttons()

    
    def mousePressEvent(self, event) -> None:
        self.ui.mouse_press_event(event)

    def set_buttons(self):
        self.BTNDescarga.clicked.connect( self.descargar)
        self.BTNUnir.clicked.connect( self.union)
    
    def descargar(self):
        window = DownloadWindowsForm()
        # window.setDataTable(resultados)
        window.show()
    def union(self):
        window = UnionWindow()
        # window.setDataTable(resultados)
        window.show()