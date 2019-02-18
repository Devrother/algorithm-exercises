class Solution {
   static int[] parent = new int[26];

   public boolean equationsPossible(String[] equations) {
      for (int i = 0; i < 26; ++i) {
         parent[i] = i;
      }

      for (String e : equations) {
         if (e.charAt(1) == '=')
            parent[find(e.charAt(0) - 'a')] = find(e.charAt(3) - 'a');

      }
      for (String e : equations) {
         if (e.charAt(1) == '!' && find(e.charAt(0) - 'a') == find(e.charAt(3) - 'a'))
            return false;
      }

      return true;
   }

   // union 함수, 현 코드에서는 == 일 때 합친다는 조건이 이미 존재하기 때문에 유효성 검증없이 바로 union 한다.
//    public void union(int a, int b) {
//       a = find(a);
//       b = find(b);

//       if (a == b)
//          return;
//       parent[a] = b;
//    }

   public int find(int x) {
      while (x != parent[x])
         x = parent[x];
      return x;
   }
}