from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QFileDialog, QMessageBox

from views.union_window import UnionWindow
from views.general_custom_ui import GeneralCustomUi
import modulos.funciones as fn
import modulos.Datos as Datos
import traceback

class UnionWindow(QWidget, UnionWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.ui = GeneralCustomUi(self)
		self.set_buttons()

	
	def mousePressEvent(self, event) -> None:
		self.ui.mouse_press_event(event)

	def set_buttons(self):
		self.BTNIniciar.clicked.connect( self.iniciar)
		self.BTNSeleccionar.clicked.connect(self.seleccionar_carpeta)
	
	def iniciar(self):
		print("inicio")
		try:
			self.PBEstado.setValue(0)
			ubicacion = self.LESeleccionarCarpeta.text() + "/"
			archivos = fn.listar_archivos_bva(ubicacion)
			for index_archivo, archivo in enumerate(archivos):
				data = Datos.get_data(ubicacion + archivo, "Operaciones")
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
				self.PBEstado.setValue(int(((index_archivo +1)/len(archivos))*100))
			fn.mensaje_simple("Enhorabuena", "Se cargaron con éxito los datos")

		except:
			traceback.print_exc()
			fn.mensaje_simple( "Error..", "Ha ocurrido un error, revisar el log")
	def seleccionar_carpeta(self):
		editText = self.LESeleccionarCarpeta
		editText.setText(None)
		fname= QFileDialog.getExistingDirectory(
				self,
				"Open a folder",
				None,
				QFileDialog.ShowDirsOnly
				)
		editText.setText(fname)