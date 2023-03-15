// https://www.beecrowd.com.br/judge/pt/problems/view/1002

#include <iostream>
#include <cmath>

using namespace std;
main(){
    double n, area, raio;
    cin >> raio;
    n = 3.14159;
    area = n * pow (raio, 2);
    cout << fixed; cout.precision(4);
    cout << "A="<< area << endl;
}