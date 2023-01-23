import sqlalchemy
import json

with open("./modulos/datos_conexion.json") as file:
	archivo = json.load(file)
	# BD = archivo["PROD"]
	BD = archivo["PROD"]

# BD = {
# 	"host": "192.168.0.15",
# 	"user": "mfinversiones",
# 	"password": "Mf_1nv3rs10n3s",
# 	"database": "bolban_mndev"
# }
def conect(database: str = None):
	import traceback
	try:
		host= BD['host']
		user= BD['user']
		password= BD['password']
		if database == None:
			database= BD['database']
		port= str(3306)
		# print(BD)
		return sqlalchemy.create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')
	except:
		traceback.print_exc()
		return None
def cursor_db(database: str = None):
	try:
		return conect(database).connect()
	except:
		return None