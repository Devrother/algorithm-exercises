import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the largestRectangle function below.
    static long largestRectangle(int[] h) {
        int i;
        long max=0;
        for(i=0;i<h.length;i++){
            int l,r;
            for(l=i;l>=0;l--){
                if(h[i]>h[l]){l=l+1;break;}
                if(l==0)break;
            }
            for(r=i;r<h.length;r++){
                if(h[i]>h[r])break;
            }
            if((r-l)*h[i]>max){max=(r-l)*h[i];System.out.println(i+" "+l+" "+r+" "+max);}

        }
        return max;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] h = new int[n];

        String[] hItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int hItem = Integer.parseInt(hItems[i]);
            h[i] = hItem;
        }

        long result = largestRectangle(h);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
