using namespace std;

/**
 * Calcula el ranking utilizando una version simplificada de AHP
 *
 * @param T Cantidad de equipos
 * @param P Cantidad de enfrentamientos
 * @param inputFile Archivo con los enfrentamientos
 *
 * @returns Puntos de los T equipos en el ranking de CMM luego de los P enfrentamientos
 */

vector<double> ahp(int T, int P, ifstream &inputFile) {
	vector<double> res(T, 1);

	//Matriz C
	vector<vector<double>> C(T);
	for (uint i = 0; i < T; i++) {
		C[i] = vector<double>(T, 0);
		C[i][i] += 1;
	}

	//Contamos cantidad de ganadas a favor de cada equipo
	for (uint i = 0; i < P; i++) {
		string fecha;
		uint iEquipo, iPuntos, jEquipo, jPuntos;
		inputFile >> fecha >> iEquipo >> iPuntos >> jEquipo >> jPuntos;

		iEquipo -= 1;
		jEquipo -= 1;

		winner_looser wl = getWinnerAndLooser(iEquipo, iPuntos, jEquipo, jPuntos);

		C[wl.winner][wl.looser] += 1;
		C[wl.looser][wl.winner] -= 1;
	}

	inputFile.close();

	for (uint i = 0; i < C.size(); i++) {
		for (uint j = 0; j < C.size(); j++) {
			if (C[i][j] != 1) {
				C[i][j] = C[i][j] > 0 ? 1.2 : (1 / 1.2);
			}
		}
	}

	/**
	*	Si hay empate o no hay partidos entre j e i. C[i][j] = 0 
	* Si i gano mas C[i][j] = 1.2
	* Si j gano mas C[i][j] = (1/1.2)
	* Si i = j entonces 1
	**/

	vector<double> total(T, 0);
	for (uint i = 0; i < C.size(); i++) {
		for (uint j = 0; j < C.size(); j++) {
			total[i] += C[j][i];
		}
	}

	for (uint i = 0; i < C.size(); i++) {
		for (uint j = 0; j < C.size(); j++) {
			C[j][i] /= total[i];
		}
	}

	for (int i = 0; i < C.size(); i++) {
		double x = 0;
		for (int j = 0; j < C.size(); j++) {
			x += C[i][j];
		}
		res[i] = x / (double)T;
	}

	return res;
}
