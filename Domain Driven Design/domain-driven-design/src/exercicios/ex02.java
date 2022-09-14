package exercicios;

import java.util.Scanner;

public class ex02 {

	public static void main(String[] args) {
		System.out.printf("");
		Scanner sc = new Scanner(System.in);
		
		float aresta, area;
		
		System.out.printf("Aresta do quadrado: ");
		aresta = sc.nextFloat();
		
		area = aresta * aresta;
		
		System.out.printf("Área: " + area);

	}

}
