class Solution {
    static int[] parent=new int[26];
    public boolean equationsPossible(String[] equations) {
        for(int i=0;i<26;++i)parent[i]=i;
        for(String e : equations){
            if(e.charAt(1)=='=')parent[find(e.charAt(0)-'a')]=find(e.charAt(3)-'a');
        }
        for(String e : equations){
            if(e.charAt(1)=='!' && find(e.charAt(0)-'a')==find(e.charAt(3)-'a'))
                return false;
        }
        return true;
    }
    public int find(int x){
        while(x!=parent[x])x=parent[x];
        return x;
    }
}