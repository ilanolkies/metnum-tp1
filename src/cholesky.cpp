using namespace std;

/**
 * Algoritmo para obtener L de Cholesky.
 * Retorna la matriz L de la factorización C = LLt
 *
 * @param C Transformacion lineal cuadrada
 * @returns L de Cholesky
 */
vector<vector<double> > lDeCholesky (vector<vector<double > > &C) {
  uint n = C.size();
  vector<vector<double> > L(n);

  for (uint i = 0; i < n; i++) {
    L[i] = vector<double>(n, 0);
  }

  for (uint i = 0; i < n; i++) {
    for (uint j = 0; j <= i; j++) {
      double sum = 0;
      if (j == i) {
        for (uint k = 0; k < j; k++) {
          sum += pow(L[j][k], 2);
        }
        L[j][j] = sqrt(C[j][j] - sum);
      } else {
        for (int k = 0; k < j; k++) {
          sum += (L[i][k] * L[j][k]);
        }
        L[i][j] = (C[i][j] - sum) / L[j][j];
      }
    }
  }

  return L;
}

/**
 * Procedimeinto para obtener la inversa de una matriz
 *
 * @param A Matriz cuadrada
 * @returns A traspuesta
 */
vector<vector<double> > inversa (vector<vector<double > > &A) {
  uint n = A.size();
  vector<vector<double> > At(n);

  for (uint i = 0; i < n; i++) {
    At[i] = vector<double>(n);
    for (uint j = 0; j < n; j++) {
      At[i][j] = A[j][i];
    }
  }

  return At;
}
