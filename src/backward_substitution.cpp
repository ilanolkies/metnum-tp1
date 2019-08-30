using namespace std;

/**
 * Procedimiento de backward-substitution.
 * Resuelve un sistema de ecuaciones lineal triangular
 * superior.
 *
 * @param A Matriz triangular superior
 * @param b Teermino independiente
 *
 * @returns x : Ax = b
 */
vector<double> sustitucion(vector<vector<double> > &A, vector<double> &b) {
  int n = A.size();

  vector<double> x(n, 0);

  for (int i = n-1; i >=0; i--) {x[i] = b[i];
    for (uint j = i + 1; j < n; j++) {
      x[i] -= A[i][j] * x[j];
    }
    x[i] /= A[i][i];
  }

  return x;
}
