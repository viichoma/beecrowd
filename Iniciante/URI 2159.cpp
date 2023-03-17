/*https://www.beecrowd.com.br/judge/pt/problems/view/2159
Schoenfeld e Rosser publicaram em 1962 um artigo descrevendo um valor mínimo e máximo para a quantidade de números primos até n, para n ≥ 17. 
Esta quantidade é representada pela função (n) e a fórmula é mostrada abaixo.

Sua tarefa é, dado um natural n, calcular o mínimo e máximo do intervalo para o número aproximado de primos até n.

Entrada
A entrada é um número natural n (17 ≤ n ≤ 109).

Saída
A saída são dois valores P e M com 1 casa decimal cada, tal que P < (n) < M, de acordo com a fórmula dada acima. Os valores devem ser separados por um espaço em branco.
*/
#include <iostream>
#include <cmath>
using namespace std;
int main() 
{
    double n, p, m; cin >> n;
    p = n / log(n);
    m = (1.25506) * (n / log(n));
    printf("%.1lf %.1lf\n", p, m);
}