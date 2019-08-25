/**
 * Calcula el ranking de WP
 *
 * @param T Cantidad de equipos
 * @param P Cantidad de enfrentamientos
 * @param inputFile Archivo con los enfrentamientos
 *
 * @returns Puntos de los T equipos en el ranking de WP luego de los P enfrentamientos
 */
vector<double> wp (uint T, uint P, ifstream &inputFile) {
  vector<double> x(T, 0);

  vector<double> w(T, 0);
  vector<double> l(T, 0);

  for (uint i = 0; i < P; i++) {
    string fecha;
    uint iEquipo, iPuntos, jEquipo, jPuntos;
    inputFile >> fecha >> iEquipo >> iPuntos >> jEquipo >> jPuntos;

    iEquipo -= 1;
    jEquipo -= 1;

    winner_looser wl = getWinnerAndLooser(iEquipo, iPuntos, jEquipo, jPuntos);
    w[wl.winner] += 1;
    l[wl.looser] += 1;
  }

  for (uint i = 0; i < T; i++) {
    x[i] = w[i] / (w[i] + l[i]);
  }

  return x;
}