import pandas as pd
import modulos.funciones as fn

def get_data( archivo: str, sheet_name: str) -> list:
    datos = pd.read_excel(archivo, sheet_name=sheet_name, header=None)
    fecha = fn.date_for_filename(archivo)

    datos.dropna(how='all', axis=0, inplace=True)
    datos.dropna(how='all', axis=1, inplace=True)

    datos.reset_index(drop=True, inplace=True)

    index = datos[(datos[0]=="Emisor") | (datos[0]=="Tipos Renta Detalle")].index.values

    data = []
    for i in range(len(index)):
        if i ==len(index) -1:
            temp = datos.iloc[index[i]:].copy()
            temp.dropna( thresh=2, inplace=True, axis=0)
            temp.dropna(how='all', axis=1, inplace=True)
            temp.reset_index(drop=True, inplace=True)
            temp.columns = temp.iloc[0]
            temp = temp.iloc[1:]
            temp.reset_index(drop=True, inplace=True)
            temp['fecha']= str(fecha)
            temp['dia']= int(fecha.dia)
            temp['mes']= int(fecha.mes)
            temp['anio']= int(fecha.anio)
            data.append(temp)
        else:
            temp = datos.iloc[index[i]:index[i+1]].copy()
            temp.dropna( thresh=5, inplace=True)
            temp.dropna(how='all', axis=1, inplace=True)
            temp.reset_index(drop=True, inplace=True)
            temp.columns = temp.iloc[0]
            temp = temp.iloc[1:]
            temp.reset_index(drop=True, inplace=True)
            temp['fecha']= str(fecha)
            temp['dia']= int(fecha.dia)
            temp['mes']= int(fecha.mes)
            temp['anio']= int(fecha.anio)
            data.append(temp)
    return data