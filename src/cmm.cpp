using namespace std;

/**
 * Calcula el ranking de CMM
 *
 * @param T Cantidad de equipos
 * @param P Cantidad de enfrentamientos
 * @param inputFile Archivo con los enfrentamientos
 *
 * @returns Puntos de los T equipos en el ranking de CMM luego de los P enfrentamientos
 */
vector<double> cmm (uint T, uint P, ifstream &inputFile, bool cholesky = false) {
  // Contruccion de matriz C y vector b

  /**
   * Cij =
   * -nij si i!=j
   * 2 + ni si i==j
   *
   * bi = 1 + (wi - li) / 2
   */

  vector<vector<double> > C(T);
  for (uint i = 0; i < T; i++) {
    C[i] = vector<double>(T, 0);
    C[i][i] += 2;
  }


  // Para construir b necesitamos partidos ganados y perdidos de cada equipo
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

    // i!=j
    C[iEquipo][jEquipo] -= 1;
    C[jEquipo][iEquipo] -= 1;

    // i==j
    C[iEquipo][iEquipo] += 1;
    C[jEquipo][jEquipo] += 1;
  }

  inputFile.close();

  vector<double> b(T, 0);
  for(uint i = 0; i < T; i++) {
    b[i] = 1 + (w[i] - l[i]) / 2;
  }


  if (!cholesky) {
    // Cr = b
    // C = LU
    // LUr = b
    eliminacionGaussiana(C, b);

    // Ur = L-1b
    vector<double> r = sustitucion(C, b);

    return r;
  } else {
    // Cr = b
    // C = LL'
    // LL'r = b
    vector<vector<double> > L = lDeCholesky(C);

    // Ly = b
    vector<double> y = sustitucionInvertida(L, b);

    // L'r = y
    vector<vector<double> > Lt = inversa(L);
    vector<double> r = sustitucion(Lt, y);

    return r;
  }
}
