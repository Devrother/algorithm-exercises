class Solution {
    public int maxProfit(int[] prices) {
        int i,j,
        int min=0; //주식값중 최솟값을 저장하는 변수
        int max=0; //주식 팔 때 가장 큰 이득을 보는 값을 저장한는 변수
        for(i=0;i<prices.length-1;i++){
                min=prices[i];
            for(j=i+1;j<prices.length;j++){
                if(prices[j]>min){
                    if(max<prices[j]-min)max=prices[j]-min;
                }
            }
        }
    return max;
    }   
}