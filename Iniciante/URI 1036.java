// https://www.beecrowd.com.br/judge/pt/problems/view/1036

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