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
# contamos con la cantidad de equipos que jeugan al menos
# una vez
enfrentamientos = input[2:]

seEnfrento = {}

for e in enfrentamientos:
  row = e.split(' ')
  seEnfrento[row[1]] = True
  seEnfrento[row[3]] = True

input[0] = str(len(seEnfrento))

# escribir los resultados en un archivo valido como input
f = open('atp/input_recortado.in', 'w')
f.writelines(line + '\n' for line in input)
f.close()

#################################

# correr atp
#print os.system('./bin/tp1 0 atp/input_recortado.in atp/input_recortado.out')

# correr cmm

# imprimir tabla de comparacion de puestos

# estaria bueno usar los nombres del csv en la tabla
