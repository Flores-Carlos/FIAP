
package exercicios;

import java.util.Scanner;

	
public class ex06 {
		
	public static void main(String[] args) {	
		System.out.printf("");
		Scanner sc = new Scanner(System.in);
		
		double cotD, d, r;
	
		System.out.printf("Cotação do Dólar: ");
		cotD = sc.nextDouble();
			
		System.out.printf("Dólares: ");
		d = sc.nextDouble();
		
		r = d * cotD;
					
		System.out.printf("R$" + r);

	}
}
