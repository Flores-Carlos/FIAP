package exercicios;

import java.util.Scanner;

public class ex05 {

	public static void main(String[] args) {
		System.out.printf("");
		Scanner sc = new Scanner(System.in);
		
		double c, f;
	
		System.out.printf("Temperatura em Celsius: ");
		c = sc.nextDouble();
		
		f = 1.8 * c + 32;
	
		System.out.printf("Temperatura em Fahrenheit: " + f);

	}

}
