public class Main {
	public String integerToBinary(int n, int element) {
		return String.format("%" + String.valueOf(n) + "s", Integer.toBinaryString(element));
	}

	public String[] solution(int n, int[] arr1, int[] arr2) {
		String[] answer = new String[n];

		for (int i = 0; i < n; i++) {
			String element = "";
			String binaryLineForArr1 = integerToBinary(n, arr1[i]);
			String binaryLineForArr2 = integerToBinary(n, arr2[i]);

			for (int j = 0; j < n; j++) {
				if (binaryLineForArr1.charAt(j) == '1' || binaryLineForArr2.charAt(j) == '1') {
					element += "#";
				} else {
					element += " ";
				}
			}
			answer[i] = element;
		}
		return answer;
	}
}