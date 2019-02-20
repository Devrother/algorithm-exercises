/*
Reference : https://www.programcreek.com/2014/01/leetcode-generate-parentheses-java/
*/

class Solution {
	public List<String> generateParenthesis(int n) {
		ArrayList<String> result = new ArrayList<String>();
		dfs(result, "", n, n);
		return result;
	}

	public void dfs(ArrayList<String> result, String phase, int left, int right) {
		if(left > right) { // point! 여는 괄호의 남은 갯수가 닫는 괄호보다 많으면 웰폼드가 무조건 아님
			return ;
		}
		
		if( left == 0 && right ==0) {
			result.add(phase);
			return;
		}
		
		if(left > 0) { // 재귀 만들 때 주의할것, 무한 재귀에 빠지면 탈출문 의심하기 
			dfs(result, phase+"(", left - 1, right);
		}
		
		if(right > 0) {
			dfs(result, phase+")", left, right -1 );
		}
	}
}