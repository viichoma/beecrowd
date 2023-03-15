// https://www.beecrowd.com.br/judge/pt/problems/view/1180

#include <iostream>
using namespace std;
int main()
{
    int n; cin >> n;
    int vetor[n];
    for(int i=0; i < n; i++)
    {
        cin >> vetor[i];
    }
    int min = vetor[0], index=0;
        for(int i=0; i < n; i++)
    {
        if (vetor[i] < min)
        {
            min = vetor[i];
            index = i;
        }
    }
    cout << "Menor valor: " << min << endl;
    cout << "Posicao: " << index << endl;
}