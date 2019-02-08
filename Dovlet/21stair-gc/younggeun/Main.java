import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();

		if (n == 1) {
			System.out.println(1);
			System.exit(0);
		}

		int count1 = 1;
		int count2 = 2;
		int result = 0;

		for (int i = 3; i <= n; i++) {
			result = count1 + count2;
			count1 = count2;
			count2 = result;
		}
		System.out.println(result);
	}
}