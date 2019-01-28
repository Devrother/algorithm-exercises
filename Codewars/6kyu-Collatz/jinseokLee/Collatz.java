public class Collatz {
  public static String collatz(int n) {
    String p=String.valueOf(n);
    while(true){
    if(n==1)break;
    p+="->";
    if(n%2==0){n=n/2;p+=n;}
    else {n=n*3+1;p+=n;}
    }
    return p;
  }
}