class Fecha:
	def __init__(self, fecha):
		self.__fecha = fecha
		self.dia = fecha.split("/")[0]
		self.mes = fecha.split("/")[1]
		self.anio = fecha.split("/")[2]
	def dia(self):
		return self.__fecha.split("/")[0]
	def mes(self):
		return self.__fecha.split("/")[1]
	def anio(self):
		return self.__fecha.split("/")[2]
	def __str__(self) -> str:
		return self.__fecha
	def es_bisiesto(año):
		return not año % 4 and (año % 100 or not año % 400)
	
	def range(fecha_inicio, fecha_fin):
		fecha_inicio = Fecha(fecha_inicio)
		fecha_fin = Fecha(fecha_fin)
		fechas = []
		dia_max = {1:[31], 2:[28,29], 3:[31], 4:[30], 5:[31], 6:[30], 7:[31], 8:[31], 9:[30], 10:[31], 11:[30], 12:[31]}
		for anio in range(int(fecha_inicio.anio), int(fecha_fin.anio)+1):
			
			for mes in range(1, 13):
				if Fecha.es_bisiesto(anio):
					limite = dia_max[mes][1]
				else:
					limite = dia_max[mes][0]
				
				for dia in range(1, limite):
					try:
						fechas.append(Fecha(f"{dia}/{mes}/{anio}"))
					except:
						pass
		return fechas