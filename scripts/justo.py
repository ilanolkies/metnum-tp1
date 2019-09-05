import sys
import os
import random

# compila tp1.cpp
compile = 'g++ src/tp1.cpp -o bin/tp1'
os.system(compile)



# nombre de archivo .in en carpeta ./input
INPUT = sys.argv[1]
# Numero de programa a correr
NUMERO = sys.argv[2]
#Numero de partidos a agregar por iteracion
PARTIDOS_EXTRA = int(sys.argv[3])

f = open('input/{}.in'.format(INPUT))
data = f.readlines()
f.close()


equipos = data[0].split()[0]





#Fijamos el equipo 0 y agregamos partidos a todos los demas
def partido_azar(cant_equipos):
	L = []
	equipo1= random.randint(2,cant_equipos)
	equipo2 = random.randint(2,cant_equipos)
	while(equipo1 == equipo2):
		equipo2 = random.randint(2,cant_equipos)
	score1 = random.randint(0,1)
	score2 = 0
	if(score2 == score1):
		score2 = 1

	L.append(1)
	L.append(equipo1)
	L.append(score1)
	L.append(equipo2)
	L.append(score2) 
	return L

for j in range(3):
	#Abro el archivo anterior
	if(j > 0):

		f = open('input/{}-{}.in'.format(INPUT,(j-1) ))
		data = f.readlines()
		f.close()

	#Escritura de los partidos anteriores 
	f= open("input/{}-{}.in".format(INPUT,j),"w+")

	for x in data:
		y = x.split()
		if(len(y) != 2):
			f.write(x)
		else:
			partido = (int(y[1])+int(PARTIDOS_EXTRA))
			
			#partidos = int(x[1]) +PARTIDOS_EXTRA
			f.write("{} {}\n".format(equipos, partido))
			

	f.write("\n")

	#Escritura de nuevos partidos
	for i in range(PARTIDOS_EXTRA):

		L = partido_azar(int(equipos))
		f.write("{} {} {} {} {}".format(L[0], L[1], L[2], L[3], L[4]))
		if(i < PARTIDOS_EXTRA-1):
			f.write("\n")
	f.close()



def leer_primera_linea(archivo):
	f = open(archivo)
	h = float(f.readline())
	f.close()
	os.remove(archivo)
	return h



run = "./bin/tp1 {0} input/{1}.in justo/metodo{0}.out".format(NUMERO, INPUT)
os.system(run)

casos = []
casos.append(leer_primera_linea("justo/metodo{0}.out".format(NUMERO)))


for i in range(3):
	##Corre el programa
	run = "./bin/tp1 {0} input/{1}-{2}.in justo/metodo-{2}-{0}.out".format(NUMERO, INPUT, i)
	os.system(run)
	##Lee los resultados de la primera linea
	casos.append(leer_primera_linea("justo/metodo-{1}-{0}.out".format(NUMERO,i)))
	os.remove("input/{0}-{1}.in".format(INPUT, i))


if os.path.exists("justo/Porcentaje{0}-{1}".format(INPUT, NUMERO)):
  os.remove("justo/Porcentaje{0}-{1}".format(INPUT, NUMERO))

for i in range(1,4):
	x = 1-casos[i]/casos[i-1]
	f = open("justo/Porcentaje{0}-{1}".format(INPUT, NUMERO), "a")
	print(x)
	f.write(str(x) + "\n")
	f.close() 

