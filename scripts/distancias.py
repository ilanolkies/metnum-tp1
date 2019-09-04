import sys
import os

# compila tp1.cpp
compile = 'g++ src/tp1.cpp -o bin/tp1'
os.system(compile)

# nombre de archivo .in en carpeta ./input
INPUT = sys.argv[1]

# borra la corrida anterior
rm = 'rm -r distancias/{0} 2> /dev/null'.format(INPUT)
os.system(rm)
mkdir = 'mkdir distancias/{0}'.format(INPUT)
os.system(mkdir)

# corre los 4 metodos y el outpu en distancias/INPUT/metodo-x.out
for i in range(4):
  run = "./bin/tp1 {0} input/{1}.in distancias/{1}/metodo-{0}.out".format(i, INPUT)
  os.system(run)


out_dir = 'distancias/{}'.format(INPUT)
# retorna el orden por equipo de un ranking dado
def rankingPonderado(method):
  f = open('{}/metodo-{}.out'.format(out_dir, method), 'r')
  ranking = [float(r) for r in f.read().splitlines()]
  f.close()

  ranking.sort()

  rankingMin = ranking[0]
  if rankingMin < 0:
    ranking = [r + abs(rankingMin) for r in ranking]

  t = sum(ranking)
  return [r/t for r in ranking]

# ordenar los 4 rankings
cmm = rankingPonderado(0)
wp = rankingPonderado(1)
ahp = rankingPonderado(2)
odi = rankingPonderado(3)

from matplotlib import pyplot as plt

x = range(1, len(cmm) + 1)


plt.bar(x, cmm, align = 'center')
plt.title('CMM')
plt.xlabel('Equipo')
plt.ylabel('Posicion (normalizada)')
plt.xlim(0.5, len(cmm) + 0.5)
plt.ylim(0, 1)
plt.savefig(out_dir + '/' + INPUT + '-cmm_dist.jpg')
plt.clf()

plt.bar(x, wp, align = 'center')
plt.title('WP')
plt.xlabel('Equipo')
plt.ylabel('Posicion (normalizada)')
plt.xlim(0.5, len(cmm) + 0.5)
plt.ylim(0, 1)
plt.savefig(out_dir + '/' + INPUT + '-wp_dist.jpg')
plt.clf()

plt.bar(x, ahp, align = 'center')
plt.title('AHP')
plt.xlabel('Equipo')
plt.ylabel('Posicion (normalizada)')
plt.xlim(0.5, len(cmm) + 0.5)
plt.ylim(0, 1)
plt.savefig(out_dir + '/' + INPUT + '-ahp_dist.jpg')
plt.clf()

plt.bar(x, odi, align = 'center')
plt.title('ODI')
plt.xlabel('Equipo')
plt.ylabel('Posicion (normalizada)')
plt.xlim(0.5, len(cmm) + 0.5)
plt.ylim(0, 1)
plt.savefig(out_dir + '/' + INPUT + '-odi_dist.jpg')
plt.clf()
