import sys
import os

# compila tp1.cpp
compile = 'g++ src/tp1.cpp -o bin/tp1'
os.system(compile)

# nombre de archivo .in en carpeta ./input
INPUT = sys.argv[1]

# borra la comparcio anterior
rm = 'rm -r comparacion/{0} 2> /dev/null'.format(INPUT)
os.system(rm)
mkdir = 'mkdir comparacion/{0}'.format(INPUT)
os.system(mkdir)

# corre los 4 metodos y el outpu en comparacion/INPUT/metodo-x.out
for i in range(4):
  run = "./bin/tp1 {0} input/{1}.in comparacion/{1}/metodo-{0}.out".format(i, INPUT)
  os.system(run)

out_dir = 'comparacion/{}'.format(INPUT)
# retorna el orden por equipo de un ranking dado
def rankingOrdenado(method):
  ranking = open('{}/metodo-{}.out'.format(out_dir, method), 'r').read().splitlines()
  rankingConEquipo = [(i, float(ranking[i])) for i in range(len(ranking))]
  rankingConEquipo.sort(key = lambda val : val[1])
  return [ranking[0] for ranking in rankingConEquipo]

# ordenar los 4 rankings
cmm = rankingOrdenado(0)
wp = rankingOrdenado(1)
ahp = rankingOrdenado(2)
odi = rankingOrdenado(3)

def diferenciaConCMM(ranking):
  return [(r, i-cmm.index(r)) for i,r in enumerate(ranking)]

wpComparado = diferenciaConCMM(wp)
ahpComparado = diferenciaConCMM(ahp)
odiComparado = diferenciaConCMM(odi)

# formato de tabla para latex comparando rankings
out = '''\\begin{center}
  \\begin{tabular}{| c || c | c || c | c || c | c |}
    \\hline
    CMM & \multicolumn{2}{c ||}{WP} & \multicolumn{2}{c ||}{AHP} & \multicolumn{2}{c |}{ODI} \\\\
    \hline\hline'''

def getArrow(n):
  if n > 0:
    return '\\textcolor{green}{$\\uparrow$}'
  if n < 0:
    return '\\textcolor{red}{$\\downarrow$}'
  return ''

def getDiff(n):
  if n == 0:
    return '-'
  return abs(n)

for i in range(len(cmm)):
  out += '''
    {} & {} & {} {} & {} & {} {} & {} & {} {}\\\\'''.format(
    cmm[i],
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
