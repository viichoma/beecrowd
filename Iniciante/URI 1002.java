// https://www.beecrowd.com.br/judge/pt/problems/view/1002

import java.io.IOException;
import java.util.Scanner;
public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
	    double raio = scanner.nextDouble();
	    double pi = 3.14159;
	    double area = pi * (raio * raio);
	    System.out.println(String.format("A=%.4f", area));
    }
 
}