using namespace std;

/**
 * Define el equipo ganador y perdedor de un enfrentamiento
 *
 * @param iEquipo primer equipo
 * @param iPuntos puntaje del primer equipo
 * @param jEquipo segundo equipo
 * @param jPuntos puntaje del segundo equipo
 *
 * @returns una tupla con el equipo ganador y del perdedor
 */
winner_looser getWinnerAndLooser (uint iEquipo, uint iPuntos, uint jEquipo, uint jPuntos) {
  winner_looser result;
  result.winner = iPuntos > jPuntos ? iEquipo : jEquipo;
  result.looser = result.winner == iEquipo ? jEquipo : iEquipo;
  return result;
}
