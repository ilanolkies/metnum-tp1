import csv

f = open('./in/atp_matches_2015.in', 'w')

equipos = {}

with open('./dataset/atp_players.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  line_count = -1
  for row in csv_reader:
    if line_count > -1:
      equipos[row[0]] = line_count
    line_count += 1

partidos = []

with open('./dataset/atp_matches_2015.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  line_count = 0
  for row in csv_reader:
    if line_count > 0:
      partidos.append([row[5], equipos[row[7]], 1, equipos[row[17]], 0])
    line_count += 1

f.write(str(len(equipos)) + '\n')
f.write(str(len(partidos)) + '\n')
for partido in partidos:
  f.write('{} {} {} {} {}\n'.format(partido[0], partido[1], partido[2], partido[3], partido[4]))
f.close()
