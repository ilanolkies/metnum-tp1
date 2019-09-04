import sys
import os

# compila tp1.cpp
compile = 'g++ src/tp1.cpp -o bin/tp1'
os.system(compile)

# nombre de archivo .in en carpeta ./input
INPUT = sys.argv[1]

# compila tp1.cpp
compile = 'g++ src/tp1.cpp -o bin/tp1'
os.system(compile)

# nombre de archivo .in en carpeta ./input
INPUT = sys.argv[1]

# borra la comparcio anterior
rm = 'rm -r equiposordenados/{0} 2> /dev/null'.format(INPUT)
os.system(rm)
mkdir = 'mkdir equiposordenados/{0}'.format(INPUT)
os.system(mkdir)

# corre los 4 metodos y el outpu en comparacion/INPUT/metodo-x.out
for i in range(4):
  run = "./bin/tp1 {0} input/{1}.in equiposordenados/{1}/metodo-{0}.out".format(i, INPUT)
  os.system(run)

out_dir = 'equiposordenados/{}'.format(INPUT)
# retorna el orden por equipo de un ranking dado
def rankingOrdenado(method):
  f = open('{}/metodo-{}.out'.format(out_dir, method), 'r')
  ranking = f.read().splitlines()
  f.close()
  rankingConEquipo = [(i + 1, float(ranking[i])) for i in range(len(ranking))]
  rankingConEquipo.sort(key = lambda val : val[1], reverse=True)
  return rankingConEquipo

# ordenar los 4 rankings
cmm = rankingOrdenado(0)
wp = rankingOrdenado(1)
ahp = rankingOrdenado(2)
odi = rankingOrdenado(3)

out = '''\\begin{center}
  \\begin{tabular}{|| c | c | c || c | c | c || c | c | c || c | c | c ||}
    \\hline
    \\multicolumn{3}{||c||}{\\textit{cmm}} &
    \\multicolumn{3}{|c||}{\\textit{wp}} &
    \\multicolumn{3}{|c||}{\\textit{ahp}} &
    \\multicolumn{3}{|c||}{\\textit{odi}} \\\\
    \\hline
    \\hline'''

for i in range(len(cmm)):
  out += '''
    {} &  & {} & {} &  & {} & {} &  & {} & {} &  & {} \\\\
'''.format(
    cmm[i][0],
    cmm[i][1],
    wp[i][0],
    wp[i][1],
    ahp[i][0],
    ahp[i][1],
    odi[i][0],
    odi[i][1],
  )

out += '''
  \\hline
  \end{tabular}
\end{center}'''

f = open('{}/resultado_latex.out'.format(out_dir), 'w')
f.write(out)
f.close()
