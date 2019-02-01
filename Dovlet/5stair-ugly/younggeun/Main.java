import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	public static void ugly(int n) {
		if (n == 1) {
			System.out.println(1);
		}

		long[] pList = { 2, 3, 5 };
		long[] pHeap = { 1, 2, 3, 5 };
		PriorityQueue<Long> heapq = new PriorityQueue<>();

		for (long i : pHeap) {
			heapq.add(i);
		}

		int cnt = n;
		while (cnt > 1) {
			long num = heapq.peek();
			heapq.remove(heapq.peek());
			for (long i : pList) {
				long uglyNum = i * num;
				if (!heapq.contains(uglyNum)) {
					heapq.add(uglyNum);
				}
			}
			cnt--;
		}
		System.out.println("The " + n + "'th ugly number is " + heapq.peek() + ".");
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();

		ugly(n);
		sc.close();
	}
}