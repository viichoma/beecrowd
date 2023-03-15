// https://www.beecrowd.com.br/judge/pt/problems/view/1183

#include <iostream>
using namespace std;
int main() 
{
    char op; cin >> op;
    float matriz[12][12];
    for(int i=0;i<12;i++)
    {
    for(int j=0;j<12;j++) 
    {
        float x; cin >> x;
        matriz[i][j] = x;
    }
    }
    int coluna = 1;
    float soma = 0;
    float contador = 0;
    for(int h=0;h<12;h++)
    {
        for(int k=coluna; k< 12;k++)
        {
        soma += matriz[h][k];
        contador++;
        }
        coluna++;
    }
    if (op == 'S')  printf("%.1f\n", soma);
    if (op == 'M')  printf("%.1f\n", soma/contador);
}