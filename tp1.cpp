#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#include "cmm.cpp"

using namespace std;

int main (int argc, char *argv[]) {
  if (argc != 4) {
    printf("Formato de parametros invalido.\n");
    return 1;
  }

  // parametros por linea de comando
  uint mode = atoi(argv[1]);
  char *input = argv[2];
  char *output = argv[3];

  // lectura del input
  ifstream inputFile;
  inputFile.open(input);

  if (mode > 2) {
    printf("Metodo invalido");
    return 1;
  }

  if (!inputFile.is_open()) {
    printf("Archivo de entrada invalido.\n");
    return 1;
  }


  // T: cantidad de equipos
  // P: cantidad de partidos
  uint T, P;
  inputFile >> T >> P;

  vector<double> r; // ranking

  // eleccion de metodo:
  switch (mode) {
    case 0:
      r = cmm(T, P, inputFile);
      break;
    case 1:
      printf("Implementar WP");
      return 1;
    case 2:
      printf("Implementar ?");
      return 1;
  }

  inputFile.close();


  ofstream outputFile;
  outputFile.open(output);

  write_vector(r, outputFile);
}
