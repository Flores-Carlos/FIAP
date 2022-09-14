package exercicios;

import java.util.Scanner;

	public class ex04 {
		public static void main(String[] args) {
			System.out.printf("");
			Scanner sc = new Scanner(System.in);
			
			float a, b, c, d, media;
		
			System.out.printf("Primeiro valor: ");
			a = sc.nextFloat();
		
			System.out.printf("Segundo valor: ");
			b = sc.nextFloat();
			
			System.out.printf("Terceiro valor: ");
			c = sc.nextFloat();
			
			System.out.printf("Quarto valor: ");
			d = sc.nextFloat();
		
			media = (a + b + c + d) / 4;
		
			System.out.printf("Média aritmética: " + media);
	}
}
