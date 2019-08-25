#include <fstream>
#include <vector>

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
      for(uint k = i; k < n; k++){
        double multiplicador = C[j][i]/C[i][i];
        C[j][k] -= multiplicador * C[i][k];
        b[k] -= multiplicador * b[k];
      }
    }
  }
}
