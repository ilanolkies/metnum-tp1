import sys
import os
import random
import time
import matplotlib.pyplot as plt
import numpy as np

# compila tp1.cpp
compile = 'g++ src/tp1.cpp -o bin/tp1'
os.system(compile)

# borra la corrida anterior
rm = 'rm -r conformista 2> /dev/null'
os.system(rm)
mkdir = 'mkdir conformista'
os.system(mkdir)

def rankingPonderado(output):
  f = open(output, 'r')
  ranking = [float(r) for r in f.read().splitlines()]
  f.close()

  rankingMin = min(ranking)
  if rankingMin < 0:
    ranking = [r + abs(rankingMin) for r in ranking]

  t = sum(ranking)
  return [r/t for r in ranking]

input = 'input/conformista_contra_b.in'
output = 'conformista/conformista_contra_b.out'

run = './bin/tp1 0 {} {}'.format(input, output)
os.system(run)
cmm = rankingPonderado(output)

run = './bin/tp1 1 {} {}'.format(input, output)
os.system(run)
wp = rankingPonderado(output)

run = './bin/tp1 2 {} {}'.format(input, output)
os.system(run)
ahp = rankingPonderado(output)

run = './bin/tp1 3 {} {}'.format(input, output)
os.system(run)
odi = rankingPonderado(output)

objects = ('a', 'b', 'c')
y_pos = np.arange(len(objects))

def guardarGrafico(ranking, ylabel, out):
  plt.bar(y_pos, ranking, align='center', alpha=0.5)
  plt.xticks(y_pos, objects)
  plt.xlabel('Equipo')
  plt.ylabel('Puesto ponderado')
  plt.title(ylabel)
  plt.savefig(out)
  plt.clf()

guardarGrafico(cmm, 'CMM', 'conformista/conformistacmmb.jpg')
guardarGrafico(ahp, 'AHP', 'conformista/conformistaahpb.jpg')
guardarGrafico(wp, 'WP', 'conformista/conformistawpb.jpg')
guardarGrafico(odi, 'ODI', 'conformista/conformistaodib.jpg')


input = 'input/conformista_contra_c.in'
output = 'conformista/conformista_contra_c.out'

run = './bin/tp1 0 {} {}'.format(input, output)
os.system(run)
cmm = rankingPonderado(output)

run = './bin/tp1 1 {} {}'.format(input, output)
os.system(run)
wp = rankingPonderado(output)

run = './bin/tp1 2 {} {}'.format(input, output)
os.system(run)
ahp = rankingPonderado(output)

run = './bin/tp1 3 {} {}'.format(input, output)
os.system(run)
odi = rankingPonderado(output)


guardarGrafico(cmm, 'CMM', 'conformista/conformistacmmc.jpg')
guardarGrafico(ahp, 'AHP', 'conformista/conformistaahpc.jpg')
guardarGrafico(wp, 'WP', 'conformista/conformistawpc.jpg')
guardarGrafico(odi, 'ODI', 'conformista/conformistaodic.jpg')
