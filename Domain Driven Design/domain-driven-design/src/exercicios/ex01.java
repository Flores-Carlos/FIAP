package exercicios;

import java.util.Scanner;

public class ex01 {

	public static void main(String[] args) {
		System.out.printf("");
		Scanner sc = new Scanner(System.in);
		
		float base, altura, area;
		
		System.out.printf("Base do ret�ngulo: ");
		base = sc.nextFloat();
		
		System.out.printf("Altura do ret�ngulo: ");
		altura = sc.nextFloat();
		
		area = base * altura;
		
		System.out.printf("�rea: " + area);
	}

}
