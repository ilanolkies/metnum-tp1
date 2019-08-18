#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main (int argc, char *argv[]) {
  if (argc != 4) {
    printf("Formato de parametros invalido.\n");
    return 1;
  }

  // parametros por linea de comando
  int mode = atoi(argv[1]);
  char *input = argv[2];
  char *output = argv[3];

  // lectura del input
  ifstream inputFile;
  inputFile.open(input);

  if (!inputFile.is_open()) {
    printf("Archivo de entrada invalido.\n");
    return 1;
  }

  // T: cantidad de equipos
  // P: cantidad de partidos
  uint T, P;
  inputFile >> T >> P;

  // Contruccion de matriz C y vector b
  // Se contruye mientras se leen los datos
  vector<vector<int> > C(T);
  for (uint i = 0; i < T; i++) {
    C[i] = vector<int>(T, 0);
    C[i][i] += 2;
  }

  // Pra construir b necesitamos partidos ganados y perdidos de cada equipo
  vector<int> w(T, 0);
  vector<int> l(T, 0);

  for (uint i = 0; i < P; i++) {
    uint fecha, iEquipo, iPuntos, jEquipo, jPuntos;
    inputFile >> fecha >> iEquipo >> iPuntos >> jEquipo >> jPuntos;

    iEquipo -= 1;
    jEquipo -= 1;

    uint winner = iPuntos > jPuntos ? iEquipo : jEquipo;
    uint looser = winner == iEquipo ? jEquipo : iEquipo;

    w[winner] += 1;
    l[looser] += 1;

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

  for (uint i = 0; i < T; i++) {
    for (uint j = 0; j < T; j++) {
      printf("%d ", C[i][j]);
    }
    printf("%f\n", b[i]);
  }

  return 0;
}
