import sys, os
import json
from datetime import *

with open('input.json') as file:
  input_json = json.loads(file.read())

appsID = []
appsLastConfig = []
rango = 24 #default

counter=0
while counter < len(input_json["apps"]): #se guardan todos las id y los lastconfigchangeat en su respectiva array

	# $id de la aplicación
	x = (input_json["apps"][counter]["id"])
	appsID.append(x)
	# última modificación de $id
	j = (input_json["apps"][counter]["versionInfo"]["lastConfigChangeAt"])
	appsLastConfig.append(j)

	counter = counter+1 #aguante C viejo

command = str(sys.argv) #se chequea si hay argumentos
argument = command.find('-') #se busca - para señalizar un comando

if argument != -1:

	x = command.find("-")
	command = command[x+1:]
	x = command.find("'")
	command2 = command[:x] #separa el argumento y lo pasa a command2
	if command2.isnumeric(): #checkea si el command2 es numerico y lo guarda en el rango
		rango = int(command2)
	elif command2 == 'h': #checkea si el command2 es h y escribe la ayuda
		print("Escriba -num. para aclarar el rango de hs. que desea ver. Ejemplo: -48")
	else: #si no es niguna de las anteriores, es invalido
		print("Argumento invalido")
		exit()

day = [] #se declaran varias arrays
time = []
año = []
mes = []
dia = []
hora = []
minuto = []
segundo = []
fechas = []
fechasOld = []

for j in appsLastConfig: #se separa la fecha del horario
	x = j.find("T")
	day.append(j[:x])
	z = j.find("Z")
	time.append(j[x+1:z])

def timeDivisor(j, f, id): #se dividen todos los valores en su respectiva array

	str(j)
	x = j.find(":")
	hora.append(int(j[:x]))
	j = j[x+1:]
	x = j.find(":")
	minuto.append(int(j[:x]))
	j = j[x+1:]
	x = j.find(".")
	segundo.append(int(j[:x]))

	str(f)
	x = f.find("-")
	año.append(int(f[:x]))
	f = f[x+1:]
	x = f.find("-")
	mes.append(f[:x])
	f = f[x+1:]
	dia.append(int(f[:x]))


def timeComparator(): #se comparan los tiempos
	
	now = datetime.now()
	year = now.strftime("%y")
	year = int(year)+2000
	fechaActual = datetime.today() #se copnsigue la fecha actual
	
	for idx, a in enumerate(año):
		d = datetime(a,int(mes[idx]),int(dia[idx]),int(hora[idx]),int(minuto[idx]),int(segundo[idx]))
		fechasOld.append(d)
		fechas.append(d) #se guarda cada fecha del json en 2 arrays

	fechasOld.append(d + timedelta(days = 25))
	fechas.append(d + timedelta(days = 25))
	fechas.sort(reverse=True) #se ordena fechas de mayor a menor

	for d in fechas:
		fechaPasada = fechaActual - timedelta(hours = rango) #se le restan las hs aclaradas en rango
		if d >= fechaPasada:
			x = fechasOld.index(d) #se busca la fecha en la array sin ordenar
			print("id:",appsID[x])
			print("lastConfigChangeAt:", d,"\n") #se imprime la fecha y la id de la app

counter = 0
while counter < len(time):
	timeDivisor(time[counter], day[counter],counter) #se divide el tiempo
	counter = counter+1 #nana este python una falta de respeto

timeComparator() #se compara y se imprime el tiempo