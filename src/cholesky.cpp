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





/**
 * Algoritmo para obtener L de Cholesky.
 * Retorna la matriz L de la factorización C = LLt
 *
 * @param C Transformacion lineal cuadrada
 * @returns L de Cholesky
 */
vector<map<int,double> > lDeCholesky_ralo(vector<map<int,double> > &C){
  uint n = C.size();
  vector<map<int, double> > L(n);
  double aux;

  for (uint i = 0; i < n; i++) {
    for (uint j = 0; j <= i; j++) {
      double sum = 0;
      if (j == i) {
        for (uint k = 0; k < j; k++) {
          if(L[j].count(k) == 1){
            sum += pow(L[j][k], 2); 
          }
        }
        aux = sqrt(C[j][j] - sum);
        if(abs(aux) >= 0.000000001){
          L[j][j] = aux;
        }
      } else {
        for (int k = 0; k < j; k++) {
          if(L[i].count(k) == 1 && L[j].count(k) == 1){
            sum += (L[i][k] * L[j][k]);
          }
        }

        if(C[i].count(j) == 1){  
          aux = (C[i][j] - sum) / L[j][j];
        }else{
          aux = (-sum)/L[j][j];
        }
        if(abs(aux) >= 0.000000001){
          L[i][j] = aux;
        }
      }
    }
  }
  return L;
}
/**
 * Procedimeinto para obtener la inversa de una matriz
 *
 * @param A Matriz rala cuadrada
 * @returns A traspuesta
 */
vector<map<int,double> > inversa_ralo (vector<map<int,double> > &A) {
  uint n = A.size();
  vector<map<int, double> > At(n);

  for (uint i = 0; i < n; i++) {
    for (uint j = 0; j < n; j++) {
      if(A[j].count(i) == 1){
        At[i][j] = A[j][i]; 
      }
    }
  }

  return At;
}


