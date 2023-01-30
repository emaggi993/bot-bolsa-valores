import pandas as pd
import modulos.funciones as fn
import xlrd
import numpy as np
import traceback
from pandas.api.types import is_string_dtype
from pandas.api.types import is_object_dtype


def get_data(archivo: str, sheet_name: str) -> list:
	try:
		datos = pd.read_excel(archivo, sheet_name=sheet_name, header=None)
		fecha = fn.date_for_filename(archivo)

		datos.dropna(how='all', axis=0, inplace=True)
		datos.dropna(how='all', axis=1, inplace=True)

		datos.reset_index(drop=True, inplace=True)
		datos.columns = range(len(datos.columns))

		index = datos[(datos[0] == "Emisor") | (
			datos[0] == "Tipos Renta Detalle")].index.values

		data = []
		column = [{
			"Emisor": "Emisor",
			"Código Emisor / Emisión": "Emisión",
			"Código Serie": "Serie",
			"N° de Op": "N° de Ope.",
			"Fecha de Op": "Fecha Ope.",
			"Tipo Instrumento": "Tipo Instrumento",
			"Mercado": "Mercado",
			"Fecha Vto": "Fecha Vto.",
			"Moneda": "Moneda",
			"Cant": "Cantidad",
			"Tasa%": "Tasa %",
			"Precio Anterior": "Precio Anterior",
			"Precio": "Precio",
			"Var": "Var.",
			"Tipo de Cambio": "Tipo de Cambio",
			"Volumen Operado": "Volumen Operado",
			"Volumen Negociado en Gs": "Volumen Negociado GS"
		}, {
			"Emisor": "Emisor",
			"Código Emisor / Emisión": "Emisión",
			"Código Serie": "Serie",
			"N° de Op": "N° de Ope.",
			"Fecha de Op": "Fecha Ope.",
			"Tipo Instrumento": "Tipo Instrumento",
			"Mercado": "Mercado",
			"Fecha Vto": "Fecha Vto.",
			"Moneda": "Moneda",
			"Cant": "Cantidad",
			"Tasa%": "Tasa %",
			"Precio Anterior": "Precio Anterior",
			"Precio": "Precio",
			"Var": "Var.",
			"Tipo de Cambio": "Tipo de Cambio",
			"Volumen Operado": "Volumen Operado",
			"Volumen Negociado en Gs": "Volumen Negociado GS"
		},
			{
			"Emisor": "Emisor",
			"Código Emisor / Emisión": "Emisión",
			"Código Serie": "Serie",
			"ID Repos": "ID Repo",
			"Fecha Ope": "Fecha Ope.",
			"Tipo Instrumento": "Tipo Instrumento",
			"Plazo (días)": "Plazo (Días)",
			"Moneda": "Moneda",
			"Cant": "Cantidad",
			"Tasa%": "Tasa %",
			"Precio": "Precio",
			"Tipo Cambio": "Tipo de Cambio",
			"Volumen Negociado en Gs": "Volumen Negociado GS"
		},  {
			"Tipos Renta Detalle": "Tipo de Renta",
				"Volumen Negociado Total": "Volumen Negociado Total"
		}]
		for i in range(len(index)):
			if i == len(index) - 1:
				temp = datos.iloc[index[i]:].copy()
				temp.dropna(thresh=2, inplace=True, axis=0)
				temp.dropna(how='all', axis=1, inplace=True)
				temp.reset_index(drop=True, inplace=True)
				temp.columns = temp.iloc[0]
				temp = temp.iloc[1:]
				temp.reset_index(drop=True, inplace=True)
				temp['fecha'] = str(fecha)
				temp['dia'] = int(fecha.dia)
				temp['mes'] = int(fecha.mes)
				temp['anio'] = int(fecha.anio)

			else:
				temp = datos.iloc[index[i]:index[i+1]].copy()
				temp.dropna(thresh=5, inplace=True)
				temp.dropna(how='all', axis=1, inplace=True)
				temp.reset_index(drop=True, inplace=True)
				temp.columns = temp.iloc[0]
				temp = temp.iloc[1:]
				temp.reset_index(drop=True, inplace=True)
				temp['fecha'] = str(fecha)
				temp['dia'] = int(fecha.dia)
				temp['mes'] = int(fecha.mes)
				temp['anio'] = int(fecha.anio)
			if column[i] != None:
				temp.rename(columns=column[i],  inplace=True)
			if 'Var.' in temp.columns:
				try:
					temp['Var.'] = temp['Var.'].astype(float)
				except:
					temp['Var.'] = temp['Var.'].astype(
						str).str.replace(" ", "")
					temp['Var.'] = temp['Var.'].astype(
						str).str.replace(",", ".")
					temp['Var.'] = temp['Var.'].astype(
						str).str.replace("%", "")
					temp['Var.'] = temp['Var.'].astype(float)
					temp['Var.'] = temp['Var.']/100
				finally:
					print(temp['Var.'].dtype)
				# if is_object_dtype(temp["Var."]):

			data.append(temp)
		return data
	except:
		traceback.print_exc()
		try:
			workbook = xlrd.open_workbook(archivo)
			dataframes = []
			print()
			fecha = fn.date_for_filename(archivo)
			for worksheet in workbook.sheets():
				print(worksheet.name)
				datos = pd.read_excel(
					archivo, sheet_name=worksheet.name, header=None)
				datos.dropna(how='all', inplace=True, axis=1)
				datos.columns = np.arange(len(datos.columns))

				if "RENTA FIJA" in datos[0].to_list():
					# print("RENTA FIJA" in datos[0].to_list(),"RENTA FIJA" )
					index = datos[datos[0] == "RENTA FIJA"].index.values[0]
					rf = datos.iloc[index+1:].copy()
					rf.dropna(thresh=2, axis=0, inplace=True)
					rf.dropna(how='all', axis=1, inplace=True)
					rf.reset_index(drop=True, inplace=True)
					index_na = rf[rf[0].isna()].index.values[0]
					rf = rf.iloc[:index_na]
					rf.columns = rf.iloc[0]

					rf = rf.iloc[1:]
					rf['fecha'] = str(fecha)
					rf['dia'] = int(fecha.dia)
					rf['mes'] = int(fecha.mes)
					rf['anio'] = int(fecha.anio)
					dataframes.append(rf)
					# print(index_na, rf.tail())
				if "RENTA VARIABLE" in datos[0].to_list():

					index = datos[datos[0] == "RENTA VARIABLE"].index.values[0]
					rv = datos.iloc[index+1:].copy()
					rv.dropna(thresh=2, axis=0, inplace=True)
					rv.dropna(how='all', axis=1, inplace=True)
					rv.reset_index(drop=True, inplace=True)
					index_na = rv[rv[0].isna()].index.values[0]
					rv = rv.iloc[:index_na]
					rv.columns = rv.iloc[0]

					rv = rv.iloc[1:]
					# if rv['']
					if is_string_dtype(rv['Volumen Operado']):
						rv['Volumen Operado'] = rv['Volumen Operado'].astype(
							str).str.replace(".", "")
						rv['Volumen Operado'] = rv['Volumen Operado'].astype(
							str).str.replace(",", ".")
					rv['Volumen Operado'] = rv['Volumen Operado'].astype(float)
					rv['fecha'] = str(fecha)
					rv['dia'] = int(fecha.dia)
					rv['mes'] = int(fecha.mes)
					rv['anio'] = int(fecha.anio)
					dataframes.append(rv)
					# print(index_na, rv.tail())
					# print(index_na, rv.tail())
				if "REPOS" in datos[0].to_list():
					index = datos[datos[0] == "REPOS"].index.values[0]
					repos = datos.iloc[index+1:].copy()
					repos.dropna(thresh=2, axis=0)
					repos.dropna(how='all', axis=1, inplace=True)
					repos.reset_index(drop=True, inplace=True)
					index_na = repos[repos[0].isna()].index.values[0]
					repos = repos.iloc[:index_na]
					repos.dropna(how='all', axis=1, inplace=True)
					repos.columns = repos.iloc[0]
					repos = repos.iloc[1:]
					repos['fecha'] = str(fecha)
					repos['dia'] = int(fecha.dia)
					repos['mes'] = int(fecha.mes)
					repos['anio'] = int(fecha.anio)
					dataframes.append(repos)
					# print(index_na, repos.tail())
					# print(index_na, repos.tail())
				if "Tipo de Renta" in datos[0].to_list():
					index = datos[datos[0] == "Tipo de Renta"].index.values[0]
					tipo_renta = datos.iloc[index:].copy()
					tipo_renta.dropna(how='all', axis=1, inplace=True)
					tipo_renta.dropna(thresh=2, axis=0)
					tipo_renta.reset_index(drop=True, inplace=True)
					# index_na = tipo_renta[tipo_renta[0].isna()].index.values[0]
					# tipo_renta = tipo_renta.iloc[:index_na ]
					tipo_renta.columns = tipo_renta.iloc[0]
					tipo_renta = tipo_renta.iloc[1:]
					tipo_renta['fecha'] = str(fecha)
					tipo_renta['dia'] = int(fecha.dia)
					tipo_renta['mes'] = int(fecha.mes)
					tipo_renta['anio'] = int(fecha.anio)
					dataframes.append(tipo_renta)
					# print(index_na, tipo_renta.tail())
			return dataframes
		except:
			traceback.print_exc()
			return None
