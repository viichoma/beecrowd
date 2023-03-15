/*
Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100])
este valor se encontra. Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.

O símbolo ( representa "maior que". Por exemplo:
[0,25]  indica valores entre 0 e 25.0000, inclusive eles.
(25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000

Entrada
O arquivo de entrada contém um número com ponto flutuante qualquer.

Saída
A saída deve ser uma mensagem conforme exemplo abaixo.
*/

import java.io.IOException;
import java.util.Scanner;
public class Main {
 public static void main(String[] args) throws IOException {
		Scanner scanner = new Scanner(System.in);
        double A = scanner.nextDouble();
        if(A<0 || A>100.0)
        System.out.print("Fora de intervalo\n");
        else if(A<=25.0)
        System.out.print("Intervalo [0,25]\n");
        else if(A<=50.0)
        System.out.print("Intervalo (25,50]\n");
        else if(A<=75.0)
        System.out.print("Intervalo (50,75]");
        else if(A<=100.0)
        System.out.print("Intervalo (75,100]\n");
    }
}
