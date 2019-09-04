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
rm = 'rm -r 2e_random 2> /dev/null'
os.system(rm)
mkdir = 'mkdir 2e_random'
os.system(mkdir)
mkdir = 'mkdir 2e_random/input'
os.system(mkdir)
mkdir = 'mkdir 2e_random/output'
os.system(mkdir)

def rankingPonderado(output):
  f = open(output, 'r')
  ranking = [float(r) for r in f.read().splitlines()]
  f.close()

  ranking.sort()

  rankingMin = ranking[0]
  if rankingMin < 0:
    ranking = [r + abs(rankingMin) for r in ranking]

  t = sum(ranking)
  return [r/t for r in ranking]

ejecuciones = range(1,20)
enfrentamientos = range(50,200)

xAxis = np.repeat(np.array(enfrentamientos), ejecuciones[-1])
cmmY = []
wpY = []
ahpY = []

for j in enfrentamientos:
  for i in ejecuciones:
    out = '2 {0}\n'.format(j)
    for k in range(j):
      winner = random.randrange(1, 3, 1)
      loser =  2 if winner == 1 else 1
      out += '1 {} 1 {} 0\n'.format(winner, loser)

    f = open('2e_random/input/{0}.in'.format(j), 'w')
    f.write(out)
    f.close()

    run = './bin/tp1 0 2e_random/input/{0}.in 2e_random/output/cmm_{1}.out'.format(j, j)
    os.system(run)
    run = './bin/tp1 1 2e_random/input/{0}.in 2e_random/output/wp_{1}.out'.format(j, j)
    os.system(run)
    run = './bin/tp1 2 2e_random/input/{0}.in 2e_random/output/ahp_{1}.out'.format(j, j)
    os.system(run)

    # obtiene los 3 resultados
    cmm = rankingPonderado('2e_random/output/cmm_{0}.out'.format(j))
    wp = rankingPonderado('2e_random/output/wp_{0}.out'.format(j))
    ahp = rankingPonderado('2e_random/output/ahp_{0}.out'.format(j))

    cmmY.append(abs(cmm[0] - cmm[1]))
    wpY.append(abs(wp[0] - wp[1]))
    ahpY.append(abs(ahp[0] - ahp[1]))

plt.plot(xAxis, cmmY, 'ro')
plt.axis([xAxis[0], xAxis[-1], 0, 0.5])
plt.title('CMM')
plt.xlabel('Cant. de enfrentamientos')
plt.ylabel('Diferencia entre rankings normalizada')
plt.savefig('2e_random/2e_random-cmm.jpg')
plt.clf()

plt.plot(xAxis, wpY, 'ro')
plt.axis([xAxis[0], xAxis[-1], 0, 0.5])
plt.title('WP')
plt.xlabel('Cant. de enfrentamientos')
plt.ylabel('Diferencia entre rankings normalizada')
plt.savefig('2e_random/2e_random-wp.jpg')
plt.clf()

plt.plot(xAxis, ahpY, 'ro')
plt.axis([xAxis[0], xAxis[-1], 0, 0.5])
plt.title('AHP')
plt.xlabel('Cant. de enfrentamientos')
plt.ylabel('Diferencia entre rankings normalizada')
plt.savefig('2e_random/2e_random-ahp.jpg')
plt.clf()
