public class Greed{
  public static int greedy(int[] dice) {
		int[] numberCount = { 0, 0, 0, 0, 0, 0, 0 };
		int[] threeScores = { 0, 1000, 200, 300, 400, 500, 600 };
		int result = 0;

		for (int i = 0; i < 5; i++) {
			numberCount[dice[i]]++;

			if (dice[i] == 1 || dice[i] == 5) {
				result += dice[i] == 1 ? 100 : 50;
			}

			if (numberCount[dice[i]] == 3) {
				if ((dice[i] == 1 || dice[i] == 5)) {
					result += dice[i] == 1 ? threeScores[dice[i]] - 300 : threeScores[dice[i]] - 150;
				} else {
					result += threeScores[dice[i]];
				}
			}
		}

		return result;
	}
}