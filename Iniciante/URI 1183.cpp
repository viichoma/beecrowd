/* https://www.beecrowd.com.br/judge/pt/problems/view/1183

Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. 
Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão acima da diagonal principal da matriz, 
conforme ilustrado abaixo (área verde).

Entrada
A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada 
com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.

Saída
Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.
*/

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
