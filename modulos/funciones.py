from modulos.Fecha import Fecha
from datetime import datetime, timedelta

def get_url( fecha : Fecha)-> str:
    URL= f"https://www.bolsadevalores.com.py/informe-diario?date={int(fecha.anio)}-{int(fecha.mes)}-{int(fecha.dia)}"
    return URL
def listar_fechas(fecha_inicio: Fecha, fecha_fin: Fecha):
    inicio = datetime(int(fecha_inicio.anio), int(fecha_inicio.mes), int(fecha_inicio.dia))
    fin = datetime(int(fecha_fin.anio), int(fecha_fin.mes), int(fecha_fin.dia))
    return [(inicio + timedelta(days=d)).strftime("%d/%m/%Y") for d in range((fin - inicio).days + 1)]
