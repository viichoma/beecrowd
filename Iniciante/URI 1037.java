// https://www.beecrowd.com.br/judge/pt/problems/view/1037

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