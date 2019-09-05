import sys
import os

compile = 'g++ src/tp1.cpp -o bin/tp1'
os.system(compile)

# nombre de archivo .in en carpeta ./input
archivos = [
  'test-prob-1',
  'test-prob-2',
  'test1',
  'test2',
  'test_completo_10_1',
  'test_completo_100_4',
  'test_completo_100_8',
  'test_completo_1000_2',
  'test_completo_1000_8'
]

result = ''

for INPUT in archivos:
    # borra la corrida anterior
    rm = 'rm -r performance/{0} 2> /dev/null'.format(INPUT)
    os.system(rm)
    mkdir = 'mkdir performance/{0}'.format(INPUT)
    os.system(mkdir)

    import time

    start = time.time()
    run = './bin/tp1 0 input/{}.in output/{}.out'.format(INPUT, INPUT)
    os.system(run)
    end = time.time()
    elpasedEG = end - start

    start = time.time()
    run = './bin/tp1 4 input/{}.in output/{}.out'.format(INPUT, INPUT)
    os.system(run)
    end = time.time()
    elpasedChol = end - start


    result += '''
\\begin{{center}}
    \\begin{{tabular}}{{|c c|}}
        \\hline
        Timepo de ejecucion (s) & \\textit{{{0}}} \\\\
        \\hline
        \\hline
        Con Eliminacion Gaussiana & Con Fact. de Cholesky \\\\
        \\hline
        ${1}$ & ${2}$ \\\\
        \\hline
    \\end{{tabular}}
\\end{{center}}
'''.format(INPUT, elpasedEG, elpasedChol)

f = open('performance/valores.out'.format(INPUT), 'w')
f.write(result)
f.close()
