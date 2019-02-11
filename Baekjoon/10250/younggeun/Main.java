import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();
		for(int test_case = 0; test_case < T; test_case++) {
			int H = sc.nextInt(); int W = sc.nextInt(); int N = sc.nextInt();
			
			int xx = 1;
		
			while(N>H) {
				xx++;
				N-=H;
			}

			System.out.printf("%d%02d\n",N,xx);
		}
		
		sc.close();
	}
}