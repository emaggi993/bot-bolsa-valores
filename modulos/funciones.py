from modulos.Fecha import Fecha
from datetime import datetime, timedelta
import pandas as pd
from modulos.conexion import conect, cursor_db
from PySide6.QtWidgets import QMessageBox
import json
import traceback

def get_url( fecha : Fecha)-> str:
	URL= f"https://www.bolsadevalores.com.py/informe-diario?date={int(fecha.anio)}-{int(fecha.mes)}-{int(fecha.dia)}"
	return URL
def listar_fechas(fecha_inicio: Fecha, fecha_fin: Fecha):
	inicio = datetime(int(fecha_inicio.anio), int(fecha_inicio.mes), int(fecha_inicio.dia))
	fin = datetime(int(fecha_fin.anio), int(fecha_fin.mes), int(fecha_fin.dia))
	return [(inicio + timedelta(days=d)).strftime("%d/%m/%Y") for d in range((fin - inicio).days + 1)]
def date_for_filename(filename:str ) -> Fecha:
	filename= filename.split("/")[-1]
	aux= filename.replace(".xls", '').replace("BVA-","").split("-")
	return Fecha(f"{aux[2]}/{aux[1]}/{aux[0]}")
def listar_archivos_bva(path: str)-> list:
	import os
	lista = os.listdir(path)
	archivos = []
	for archivo in lista:
		if "BVA-" in archivo and "(" not in archivo:
			archivos.append(archivo)
	return archivos
def respaldar_datos(datos: pd.DataFrame, table: str) -> bool:
	try:
		datos.to_sql(name= table, con= conect(), if_exists="append", index=False)
		
	except:
		print("!"*5,table, "!"*5)
		traceback.print_exc()
		exit(0)
		return False
	else:
		print(f"guardando datos en {table} dentro de la base de datos")
		return True

def borrar_registro_fecha (fecha: Fecha, tabla: str) -> bool:
	try:
		con = cursor_db()
		sql= f"DELETE FROM {tabla} where dia= {int(fecha.dia)} and mes={int(fecha.mes)} and anio={int(fecha.anio)}"
		rs = con.execute(sql)
		
	except:
		return False
	else:
		return True
def mensaje_simple(titulo, texto) -> None:
	dlg = QMessageBox()
	dlg.setWindowTitle(titulo)
	dlg.setText(texto)
	button = dlg.exec()

	if button == QMessageBox.StandardButton.Ok:
		print("OK!")
def data_base_config(url: str = './modulos/datos_conexion.json'):
	try:
		with open(url) as file:
			archivo = json.load(file)
			return archivo
	except:
		return None
def set_data_base_config(data: dict, url: str = './modulos/datos_conexion.json')-> bool:
	try:
		with open(url, 'w') as json_file:
			json.dump(data, json_file)
	except:
		return False
	else:
		return True


