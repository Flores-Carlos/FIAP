
package exercicios;

import java.util.Scanner;

	
public class ex06 {
		
	public static void main(String[] args) {	
		System.out.printf("");
		Scanner sc = new Scanner(System.in);
		
		double cotD, d, r;
	
		System.out.printf("Cota��o do D�lar: ");
		cotD = sc.nextDouble();
			
		System.out.printf("D�lares: ");
		d = sc.nextDouble();
		
		r = d * cotD;
					
		System.out.printf("R$" + r);

	}
}
