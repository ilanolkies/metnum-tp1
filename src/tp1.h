#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>

struct winner_looser {
  uint winner;
  uint looser;
};

#include "util.cpp"
#include "print_linear_system.cpp"

#include "eg.cpp"
#include "backward_substitution.cpp"
#include "cholesky.cpp"

#include "cmm.cpp"
#include "wp.cpp"
#include "ahp.cpp"
#include "pseudo_odi.cpp"
