from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QFileDialog, QMessageBox

from views.config_windows import ConfigWindow
from views.general_custom_ui import GeneralCustomUi
import modulos.funciones as fn
import traceback
import sqlalchemy
import pymysql


class ConfigWindow(QWidget, ConfigWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.ui = GeneralCustomUi(self)
		self.set_buttons()
		self.set_data()

	def mousePressEvent(self, event) -> None:
		self.ui.mouse_press_event(event)

	def set_buttons(self):
		self.BTNIniciar.clicked.connect(self.guardar)
		self.BTNTest.clicked.connect(self.test)

	def test(self):
		host = self.LEHost.text()
		user = self.LEUser.text()
		password = self.LEPass.text()
		database = self.LEDataBase.text()
		port = self.LEPort.text()
		print(host, user, password, database, port)
		try:
			conexion = sqlalchemy.create_engine(
				f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')

			print(conexion.connect())
			if conexion == None:
				raise Exception("No se ha establecido la conexion")
		except:
			fn.mensaje_simple(
				"Error", "No se ha podido establecer la conexión")
		else:
			fn.mensaje_simple(
				"", "Se ha establecido la conexión con la base de datos")

	def set_data(self):
		self.BD = fn.data_base_config()
		self.LEHost.setText(self.BD['host'])
		self.LEUser.setText(self.BD['user'])
		self.LEDataBase.setText(self.BD['database'])
		self.LEPort.setText(str(self.BD['port']))

	def guardar(self):
		host = self.LEHost.text()
		user = self.LEUser.text()
		password = self.LEPass.text()
		database = self.LEDataBase.text()
		port = self.LEPort.text()
		if password == '':
			password = self.BD['password']
		self.BD = {
			"host": host,
			"user": user,
			"password": password,
			"database": database,
			"port": port
		}
		resultado = fn.set_data_base_config(self.BD)
		if resultado:
			fn.mensaje_simple("", "Se ha guardado la configuración con éxito..!")
		else:
			fn.mensaje_simple("Error", "No se ha podido guardar la configuración")
		
