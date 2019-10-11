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
cantPartidos = input[1]

enfrentamientos = input[2:]

seEnfrento = {}

jugadores = {}

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
for i, e in enumerate(enfrentamientos):
	i = i+2
	#print(e)
	row = e.split(' ')
	row[1] = seEnfrento[row[1]]
	row[3] = seEnfrento[row[3]]
	jugadores[row[1]] =' {} {} '.format(row[5], row[6])
	jugadores[row[3]]=' {} {} '.format(row[7], row[8])
	
	input[i] = row[:5]



# Function to convert   
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  

input[0] = str(len(seEnfrento)) + ' ' + str(cantPartidos) + '\n'




# escribir los resultados en un archivo valido como input
f = open('input/input_recortado.in', 'w')
f.writelines(input[0])
f.writelines(listToString(line)+ '\n' for line in input[2:])
f.close()




##Leer ranking original
f = open('dataset/atp_results')
lectura_ranking = f.read().splitlines()
f.close()

atpP = []
atp = {}
##Lectura y conversion
j = 1
for e in lectura_ranking:
	row = e.split(',')
	
	if(row[2] in seEnfrento):
		jugador = seEnfrento[row[2]]
		atp[int(jugador)] = j;
		atpP.append(jugador)
		j+= 1


	#else:
	#	atp[int(row[2])] = int(row[1]) 
	#	atpP.append(' {} '.format(row[2]))

while len(atpP) < len(seEnfrento.keys())+1:
	atpP.append(' 1 ')



#######Comparacion modificado ########


INPUT = 'input_recortado'

# borra la comparcio anterior
rm = 'rm -r comparacion/{0} 2> /dev/null'.format(INPUT)
os.system(rm)
mkdir = 'mkdir comparacion/{0}'.format(INPUT)
os.system(mkdir)

# corre los 4 metodos y el output en comparacion/INPUT/metodo-x.out
for i in range(4):
  run = "./bin/tp1 {0} input/{1}.in comparacion/{1}/metodo-{0}.out".format(i, INPUT)

  os.system(run)

out_dir = 'comparacion/{}'.format(INPUT)
# retorna el orden por equipo de un ranking dado
def rankingOrdenado(method):
  f = open('{}/metodo-{}.out'.format(out_dir, method), 'r')
  ranking = f.read().splitlines()
  f.close()
  rankingConEquipo = [(i, float(ranking[i])) for i in range(len(ranking))]
  rankingConEquipo.sort(key = lambda val : val[1], reverse=True)
  return [ranking[0] for ranking in rankingConEquipo]

# ordenar los 4 rankings
cmm = rankingOrdenado(0)
wp = rankingOrdenado(1)
ahp = rankingOrdenado(2)
odi = rankingOrdenado(3)

def diferenciaConATP(ranking):
	res = []
	for i,r in enumerate(ranking):
		if(r+1 in atp.keys()):
			res.append((r+1, str(i-atp[int(r)+1]+1)))
		else:
			res.append((r+1, '-'))

	return res
#  return [(r, i-atp[int(r)]) for i,r in enumerate(ranking)]

def getArrow(n):
	if n == '-':
		return '-'
	if int(n) < 0:
		return '\\textcolor{green}{$\\uparrow$}'
	if int(n) > 0: 
		return '\\textcolor{red}{$\\downarrow$}'
	return ''

def getDiff(n):
  if n == '-' or n == 0:
    return '-'
  return str(abs(int(n)))




cmmComparado = diferenciaConATP(cmm)
wpComparado = diferenciaConATP(wp)
ahpComparado = diferenciaConATP(ahp)
odiComparado = diferenciaConATP(odi)



# formato de tabla para latex comparando rankings
out = '''\\begin{center}
  \\begin{tabular}{| c || c | c || c | c || c | c || c | c |}
    \\hline
    ATP & \multicolumn{2}{c ||}{CMM} & \multicolumn{2}{c ||}{WP} & \multicolumn{2}{c ||}{AHP} & \multicolumn{2}{c |}{ODI} \\\\
    \hline\hline'''




for i in range(len(cmm)):
  out += '''
    {} & {} & {} {} & {} & {} {} & {} & {} {} & {} & {} {}\\\\'''.format(
    atpP[i],
    cmmComparado[i][0],
    getArrow(cmmComparado[i][1]),
    getDiff(cmmComparado[i][1]),
    wpComparado[i][0],
    getArrow(wpComparado[i][1]),
    getDiff(wpComparado[i][1]),
    ahpComparado[i][0],
    getArrow(ahpComparado[i][1]),
    getDiff(ahpComparado[i][1]),
    odiComparado[i][0],
    getArrow(odiComparado[i][1]),
    getDiff(odiComparado[i][1]),
  )

out += '''
  \\hline
  \end{tabular}
\end{center}'''




f = open('{}/resultado_latex.out'.format(out_dir), 'w')
f.write(out)
f.close()




###Asignacion de nombres de jugador

f = open('comparacion/input_recortado/resultado_latex.out')
input = f.read().splitlines()
f.close()



for i,e in enumerate(input[5:435]):
	row = e.split(' ')

	#print row
	if((' {} '.format(int(row[5]))) in jugadores.keys()):	
		row[5] = jugadores[' {} '.format(int(row[5]))]

	#print row[8]
	if((' {} '.format(int(row[8]))) in jugadores.keys()):	
		row[8] = jugadores[' {} '.format(int(row[8]))]

	#print row[13]
	if((' {} '.format(int(row[13]))) in jugadores.keys()):	
		row[13] = jugadores[' {} '.format(int(row[13]))]

	#print row[18]
	if((' {} '.format(int(row[18]))) in jugadores.keys()):	
		row[18] = jugadores[' {} '.format(int(row[18]))]

	#print row[23]
	if((' {} '.format(int(row[23]))) in jugadores.keys()):	
		row[23] = jugadores[' {} '.format(int(row[23]))]

	input[i+5] = row
#20
f = open('comparacion/input_recortado/resultado_latex.out', 'w')
f.writelines(listToString(line) + '\n' for line in input[0:20])
f.writelines(listToString(line) + '\n' for line in input[435:])
f.close()
