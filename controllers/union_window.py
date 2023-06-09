from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QFileDialog, QMessageBox

from views.union_window import UnionWindow
from views.general_custom_ui import GeneralCustomUi
import modulos.funciones as fn
import modulos.Datos as Datos
import traceback
import xlrd
import numpy as np

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
		from modulos.Fecha import Fecha
		try:
			self.PBEstado.setValue(0)
			ubicacion = self.LESeleccionarCarpeta.text() + "/"
			archivos = fn.listar_archivos_bva(ubicacion)
			# rango = Fecha.range(self.fecha_desde.text(), self.fecha_hasta.text())
			for index_archivo, archivo in enumerate(archivos):

				self.LabelError.setText(archivo)
				data = Datos.get_data(ubicacion + archivo, "Operaciones")
				# print("$$$$$"*10)
				print(archivo)
				print(len(data))
				if data == None:
					print("None")
					break

				for index, datos_raw in enumerate(data):
					test = True
					if index == 0 and  test:
						fn.borrar_registro_fecha(fn.date_for_filename(archivo), "renta_fija")
						datos = Datos.validar_tipos_datos(datos_raw, "renta_fija")
						if fn.respaldar_datos(datos, "renta_fija"):
							print("respaldado")
						else:
							print(f"no guardo -> {archivo}")
							# print(datos.head())
							print("---"*10)
					elif index == 1 and  test:
						fn.borrar_registro_fecha(fn.date_for_filename(archivo), "renta_variable")
						datos = Datos.validar_tipos_datos(datos_raw, "renta_variable")
						if fn.respaldar_datos(datos, "renta_variable"):
							print("respaldado")
						else:
							print(f"no guardo -> {archivo}")
							# print(datos.head())
							print("---"*10)
					elif index == 2 and  test:
						fn.borrar_registro_fecha(fn.date_for_filename(archivo), "repos")
						datos = Datos.validar_tipos_datos(datos_raw, "repos")
						fn.respaldar_datos(datos, "repos")
					elif index == 3 and  test:
						fn.borrar_registro_fecha(fn.date_for_filename(archivo), "total_renta_detalle")
						datos = Datos.validar_tipos_datos(datos_raw, "total_renta_detalle")
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