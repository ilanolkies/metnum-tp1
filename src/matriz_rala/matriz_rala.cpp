using namespace std;

/**
 * Calcula el ranking de CMM asumiendo que la matriz sera rala
 *
 * @param T Cantidad de equipos
 * @param P Cantidad de enfrentamientos
 * @param inputFile Archivo con los enfrentamientos
 *
 * @returns Puntos de los T equipos en el ranking de CMM luego de los P enfrentamientos
 */


vector<double> matriz_rala(uint T, uint P, ifstream &inputFile) {
  // Contruccion de matriz C y vector b

  /**
   * Cij =
   * -nij si i!=j
   * 2 + ni si i==j
   *
   * bi = 1 + (wi - li) / 2
   */

  vector<map<int,double> > C(T);
  for (uint i = 0; i < T; i++) {

    C[i][i] = 2;

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


    if(C[iEquipo].count(jEquipo) == 1){
      C[iEquipo][jEquipo] -= 1;
    }else{
      C[iEquipo][jEquipo] = -1;
    }
    if(C[jEquipo].count(iEquipo) == 1){
      C[jEquipo][iEquipo] -= 1;
    }else{
      C[jEquipo][iEquipo] = -1;
    }

    C[iEquipo][iEquipo] += 1;
    C[jEquipo][jEquipo] += 1;

    
  }

  inputFile.close();

  vector<double> b(T, 0);
  for(uint i = 0; i < T; i++) {
    b[i] = 1 + (w[i] - l[i]) / 2;
  }

  
  //Cholesky

  // Cr = b
  // C = LL'
  // LL'r = b
  vector<map<int,double> > L = lDeCholesky_ralo(C);

  // Ly = b
  std::vector<double> y = sustitucionInvertida_ralo(L,b);
  
  //L'r = y
  vector<map<int, double> > Lt = inversa_ralo(L); 
  vector<double> r = sustitucion_ralo(Lt,y);

  return r;
  
  
}