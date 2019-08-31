using namespace std;

vector<double> pseudo_odi (uint T, uint P, ifstream &inputFile) {
  vector<double> r(T, 0);

  for (uint i = 0; i < P; i++) {
    string fecha;
    uint iEquipo, iPuntos, jEquipo, jPuntos;
    inputFile >> fecha >> iEquipo >> iPuntos >> jEquipo >> jPuntos;

    iEquipo -= 1;
    jEquipo -= 1;

    int r_dif = r[iEquipo] - r[jEquipo];

    if (r_dif >= 40) {
      // i > j
      if (iPuntos > jPuntos) {
        // gano el mejor
        r[iEquipo] += 10;
        r[jEquipo] -= 10;
      } else {
        // gano el peor
        r[iEquipo] -= 90;
        r[jEquipo] += 90;
      }
    } else if (r_dif <= -40) {
      // j > i
      if (iPuntos > jPuntos) {
        // gano el peor
        r[iEquipo] += 90;
        r[jEquipo] -= 90;
      } else {
        // gano el mejor
        r[iEquipo] -= 10;
        r[jEquipo] += 10;
      }
    } else {
      // j = i
      if (iPuntos > jPuntos) {
        r[iEquipo] += 50;
        r[jEquipo] -= 50;
      } else {
        r[iEquipo] -= 50;
        r[jEquipo] += 50;
      }
    }
  }

  return r;
}