import java.io.*;
import java.util.*;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        BigInteger[] factorial = new BigInteger[31];
        factorial[0] = BigInteger.ONE;
        for (int i = 1; i < 31; i++) {
            factorial[i] = BigInteger.valueOf((long)i).multiply(factorial[i-1]);
        }

        for (int i = 0; i < t; i++) {
            int[] nm = Arrays.stream(br.readLine().split(" ")).mapToInt(num -> Integer.parseInt(num)).toArray();
            System.out.println(factorial[nm[1]].divide(factorial[nm[1]-nm[0]].multiply(factorial[nm[0]])).toString());
        }
    }
}