class Solution {
    public int largestPerimeter(int[] A) {
        int i,j,k,max=0,su=0,tmp;
        for(i=0;i<A.length-1;i++){
            for(j=i+1;j<A.length;j++){
                if(A[i]<A[j]){tmp=A[i];A[i]=A[j];A[j]=tmp;}
            }
    }
        for(i=0;i<A.length-2;i++){
            for(j=i+1;j<A.length-1;j++){
                for(k=i+2;k<A.length;k++){
                    if(A[i]<A[j]+A[k]){su=A[i]+A[j]+A[k];break;}
                }
                if(su!=0)break;
            }
            if(su!=0)break;
        }
        return su;
}
}