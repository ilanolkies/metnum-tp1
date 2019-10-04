import os

# compilar tp1
os.system('g++ src/tp1.cpp -o bin/tp1')

# limpiar corrida anterior
os.system('rm -r atp 2> /dev/null')

# inicializar carpeta
os.system('mkdir atp')
os.system('touch atp/input_recortado.in')

# importar ranking atp
f = open('input/atp_matches_2015.in')
input = f.read().splitlines()
f.close()

#################################
# recortar datos que no aportan #
#################################

# vamos a contar los equipos que verdaderamente juegan para
# que nuestra matriz no sea innecesariamente grande
# contamos con la cantidad de equipos que juegan al menos
# una vez



enfrentamientos = input[1:]

seEnfrento = {}

for e in enfrentamientos:
  row = e.split(' ')
  seEnfrento[row[1]] = True
  seEnfrento[row[3]] = True


##Asignamos numero de menor a mayor
j = 1
for i in sorted(seEnfrento.keys()):
	seEnfrento[i] = " {} ".format(str(j))
	j = j+1

##Reemplazamos los valores usando el diccionario
for i, e in enumerate(input[1:]):
	i = i+1
	row = e.split(' ')
	row[1] = seEnfrento[row[1]]
	row[3] = seEnfrento[row[3]]
	input[i] = row



# Function to convert   
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  

cantPartidos = input[0].split(' ')[1]
input[0] = str(len(seEnfrento)) + ' ' +str(cantPartidos)

# escribir los resultados en un archivo valido como input
f = open('atp/input_recortado.in', 'w')
f.writelines(listToString(line)+ '\n' for line in input)
f.close()


# correr atp
os.system('./bin/tp1 0 atp/input_recortado.in atp/input_recortado.out')



# imprimir tabla de comparacion de puestos


# estaria bueno usar los nombres del csv en la tabla
