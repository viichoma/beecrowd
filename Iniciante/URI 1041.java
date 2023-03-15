// https://www.beecrowd.com.br/judge/pt/problems/view/1041

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