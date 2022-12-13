import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QMessageBox, QFileDialog, QTableWidget, QTableWidgetItem
from views.general_custom_ui import GeneralCustomUi
from views.resultado_windows import Resultados


class ResultadoWidget(QWidget, Resultados):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setupUi(self)
		self.ui = GeneralCustomUi(self)
		self.settings_table()

	def mousePressEvent(self, event) -> None:
		self.ui.mouse_press_event(event)

	def settings_table(self):
		# EStablecer altura de las filas
		self.tabla.verticalHeader().setDefaultSectionSize(20)
		nombreColumnas = ("fecha","xls", "pdf", "estado")

		# Establecer las etiquetas de encabezado horizontal usando etiquetas
		self.tabla.setColumnCount(len(nombreColumnas))
		self.tabla.setHorizontalHeaderLabels(nombreColumnas)
		# Establecer ancho de las columnas
		for indice, ancho in enumerate((150, 80, 80, 200), start=0):
			self.tabla.setColumnWidth(indice, ancho)

		self.tabla.resizeRowsToContents()
	def setDataTable(self, data):
		self.data = data
		row= 0
		for index, item in enumerate( data):
			self.tabla.setRowCount( row + 1)
			self.tabla.setItem(row, 0, QTableWidgetItem(item['fecha']))
			self.tabla.setItem(row, 1, QTableWidgetItem(str(item['xls'])))
			self.tabla.setItem(row, 2, QTableWidgetItem(str(item['pdf'])))
			if item['xls'] > 0 :
				self.tabla.setItem(row, 3, QTableWidgetItem('OK'))
			else:
				self.tabla.setItem(row, 3, QTableWidgetItem('Sin datos'))
			row += 1
