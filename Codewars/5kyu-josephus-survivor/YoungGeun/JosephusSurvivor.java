import java.util.LinkedList;

public class JosephusSurvivor {
	public static int josephusSurvivor(final int n, final int k) {
		LinkedList<Integer> queue = new LinkedList<>();

		for (int i = 1; i <= n; i++)
			queue.add(i);

		while (queue.size() != 1) {
			for (int i = 0; i < k - 1; i++) {
				int temp = queue.removeFirst();
				queue.add(temp);
			}
			queue.removeFirst();
		}
		return queue.peek();
	}
}
