package exercicios;

import java.util.Scanner;

public class ex03 {

	public static void main(String[] args) {
		System.out.printf("");
		Scanner sc = new Scanner(System.in);
		
		float base, altura, area;
		
		System.out.printf("Base do tri�ngulo: ");
		base = sc.nextFloat();
		
		System.out.printf("Altura do tri�ngulo: ");
		altura = sc.nextFloat();
		
		area = (base * altura) / 2;
		
		System.out.printf("�rea: " + area);
	}

}
