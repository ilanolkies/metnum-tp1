import sys
import os

# compila tp1.cpp
compile = 'g++ src/tp1.cpp -o bin/tp1'
os.system(compile)

# nombre de archivo .in en carpeta ./input
INPUT = sys.argv[1]

# borra la corrida anterior
rm = 'rm -r 5equipos 2> /dev/null'
os.system(rm)
mkdir = 'mkdir 5equipos'.format(INPUT)
os.system(mkdir)


inputs = [
  '5equipos05',
  '5equipos14',
  '5equipos23',
  '5equipos32',
  '5equipos41',
  '5equipos50'
]

# retorna el orden por equipo de un ranking dado
def rankingPonderado(input, method):
  f = open('5equipos/{}metodo{}.out'.format(input, method), 'r')
  ranking = [float(r) for r in f.read().splitlines()]
  f.close()

  ranking.sort()

  rankingMin = ranking[0]
  if rankingMin < 0:
    ranking = [r + abs(rankingMin) for r in ranking]

  t = sum(ranking)
  return [r/t for r in ranking]

results = [
  [],
  [],
  [],
  []
]


data1 = [r[0] for r in results[0]]
data2 = [r[1] for r in results[0]]
data3 = [r[2] for r in results[0]]
data = [data1, data2, data3]

for input in inputs:
  # corre los 4 metodos y el outpu en distancias/INPUT/metodo-x.out
  for i in range(4):
    run = "./bin/tp1 {0} input/{1}.in 5equipos/{1}metodo{0}.out".format(i, input)
    os.system(run)

    results[i].append(rankingPonderado(input, i))

import matplotlib.pyplot as plt
import numpy as np

N = 6
K = 5

ind = np.arange(N)

width = 0.5
plt.bar(ind, input, width=1)
plt.xticks(ind + 1/2, data)
plt.xticks(ind + 1/2, data)
plt.show()
