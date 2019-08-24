#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

vector<double> sustitucion(vector<vector<int> > &m, vector<double> b){
	int m_size = m.size() - 1;

	vector<double> res(m_size+1, 0);

	int fila = m_size;

	for(int i = m_size; i >= 0; i--){
		//Resta de 
		for(int j = m_size; j >fila; j-- ){
			
			//cout << j << "  " <<  i  << endl;
			//cout << res[j]*m[i][j] << endl;

			b[i] = b[i] - m[i][j]*res[j];	
			
		}

		res[fila] = b[i]/m[i][fila];
		fila--;
			
	}


	return res;



} 





main(int argc, char *argv[]){

	vector<vector<int> > v = {
		{1,2,2},
		{0,1,4},
		{0,0,3},
	};
	vector<double> b = {3,6,9};

	vector<double> res = sustitucion(v, b);

	
	char *output = argv[1];
	
	//results(res, a);





	//Salida
	ofstream outputFile;
  	outputFile.open(output,std::ofstream::out);

  	if(!outputFile.is_open()){
  		cerr << "Error opening/creating output file" << endl;
  		exit(1);
  	}

  	int i = 0;
  	while(i< v.size()){
  		outputFile << res[i] << endl;
  		i++;

  	}

  	outputFile.close();


}