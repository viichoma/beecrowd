/*
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, 
mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário,
imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.
*/

import java.io.IOException;
import java.util.Scanner;
public class Main {
 public static void main(String[] args) throws IOException {
		Scanner scanner = new Scanner(System.in);
        double A = scanner.nextDouble();
        double B = scanner.nextDouble();
        double C = scanner.nextDouble();
        double delta = B*B - 4.0*A*C;
        if (delta < 0 || A == 0)
		System.out.println("Impossivel calcular");
        else
        {
        System.out.println(String.format("R1 = %.5f", (-B+Math.sqrt(delta))/(2.0*A)));
        System.out.println(String.format("R2 = %.5f", (-B-Math.sqrt(delta))/(2.0*A)));
        }
    }
}
