// https://www.beecrowd.com.br/judge/pt/problems/view/1002

#include <stdio.h>
#include <math.h>
main(){
    double n, area, raio;
    scanf ("%lf", &raio);
    n = 3.14159;
    area = n * pow (raio, 2);
    printf ("A=%.4lf\n",area);
    
}