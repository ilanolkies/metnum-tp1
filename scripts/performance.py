import sys
import os

compile = 'g++ src/tp1.cpp -o bin/tp1'
os.system(compile)

# nombre de archivo .in en carpeta ./input
INPUT = sys.argv[1]

# borra la corrida anterior
rm = 'rm -r performance/{0} 2> /dev/null'.format(INPUT)
os.system(rm)
mkdir = 'mkdir performance/{0}'.format(INPUT)
os.system(mkdir)

import time

start = time.time()
run = './bin/tp1 0 input/{0}.in output/{0}.out'.format(INPUT)
end = time.time()
elpasedEG = end - start

start = time.time()
run = './bin/tp1 4 input/{0}.in output/{0}.out'.format(INPUT)
end = time.time()
elpasedChol = end - start


result = '''
\\begin{{center}}
    \\begin{{tabular}}{{|c c|}}
        \\hline
        \multicolumn{{2}}{{|c|}}{{\\textit{{{0}}}}} \\\\
        \\hline
        \\hline
        Con Eliminacion Gaussiana & Con Fact. de Cholesky \\\\
        \\hline
        ${1}$ & ${2}$ \\\\
        \\hline
    \\end{{tabular}}
\\end{{center}}
'''.format(INPUT, elpasedEG, elpasedChol)

f = open('performance/{0}/valores.out'.format(INPUT), 'w')
f.write(result)
f.close()
