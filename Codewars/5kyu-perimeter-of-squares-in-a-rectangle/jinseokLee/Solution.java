typedef unsigned long long ull;
ull perimeter(int n) {
  // your code
  // your code
    ull p[10000];
    p[0]=1;p[1]=1;
    int i;
    ull sum=2;
    for(i=2;i<=n;i++){
    p[i]=p[i-1]+p[i-2];
    sum+=p[i];
	}
  return sum*4;
}