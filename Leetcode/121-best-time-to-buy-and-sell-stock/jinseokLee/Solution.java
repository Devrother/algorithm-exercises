class Solution {
    public int maxProfit(int[] prices) {
        int i,j,
        int min=0; //�ֽİ��� �ּڰ��� �����ϴ� ����
        int max=0; //�ֽ� �� �� ���� ū �̵��� ���� ���� �����Ѵ� ����
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