/* https://www.beecrowd.com.br/judge/pt/problems/view/1041
Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. 
A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).

Se o ponto estiver na origem, escreva a mensagem “Origem”.

Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.

Entrada
A entrada contem as coordenadas de um ponto.

Saída
A saída deve apresentar o quadrante em que o ponto se encontra.
*/

import java.io.IOException;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        double X = scanner.nextDouble();
        double Y = scanner.nextDouble();
        if (X == 0.0 && Y == 0.0)
        {
        System.out.print("Origem\n");
        }
        else if (X == 0.0 && Y != 0.0)
        {
        System.out.print("Eixo Y\n");
        }
        else if (Y == 0.0 && X != 0.0)
        {
        System.out.print("Eixo X\n");
        }
        else if (X > 0.0)
    {
        if (Y > 0.0)
        {
            System.out.print("Q1\n");
        }
        else System.out.print("Q4\n");
    }
        else if (Y > 0.0)
    {
        System.out.print("Q2\n");
    }
        else System.out.print("Q3\n");
    }
 
}
