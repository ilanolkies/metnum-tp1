import os
import numpy as np

compile = 'g++ src/tp1.cpp -o bin/tp1'
os.system(compile)

rm = 'rm -r cuantitativo 2> /dev/null'
os.system(rm)
mkdir = 'mkdir cuantitativo'
os.system(mkdir)

archivos = ['test-prob-1', 'test-prob-2', 'test1', 'test2']

for archivo in archivos:
  run = './bin/tp1 0 input/{0}.in cuantitativo/{0}.out'.format(archivo)
  os.system(run)
  expected = np.fromfile('expected/{0}.expected'.format(archivo), count=-1, dtype=float, sep='\n')
  actual = np.fromfile('cuantitativo/{0}.out'.format(archivo), count=-1, dtype=float, sep='\n')
  error = np.linalg.norm(actual - expected)

  result = '''
    \\begin{{center}}
        \\begin{{tabular}}{{|c c|}}
            \\hline
            \multicolumn{{2}}{{|c|}}{{\\textit{{{0}}}}} \\\\
            \\hline
            \\hline
            Esperado & ${1}$ \\\\
            \\hline
            Obtenido & ${2}$ \\\\
            \\hline
            \\hline
            Error & ${3}$ \\\\
            \\hline
        \\end{{tabular}}
    \\end{{center}}
  '''.format(archivo, repr(expected), repr(actual), error)
  print(result)
