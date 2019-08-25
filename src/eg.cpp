using namespace std;

/**
 * Algoritmo de eliminacion Gaussiana (in-place).
 * Luego de ejecutar este método, la matriz C representa
 * un sistema de ecuaciones lineales triangular superior.
 *
 * @param C Transformacion lineal cuadrada
 * @param b Termino independeinte
 */
void eliminacionGaussiana (vector<vector<double > > &C, vector<double> &b) {
  uint n = C.size();
  for (uint i = 0; i < n-1; i++) {
    for (uint j = i+1; j < n; j++) {
      double mij = C[j][i] / C[i][i];
      for(uint k = i; k < n; k++) {
        C[j][k] -= mij * C[i][k];
      }
      b[j] -= mij * b[i];
    }
  }
}
