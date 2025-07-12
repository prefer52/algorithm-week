import java.math.BigInteger;
import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        long[] dists = new long[n-1];
        for (int i = 0; i < n-1; i++) {
            dists[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        long[] costs = new long[n];
        for (int i = 0; i < n; i++) {
            costs[i] = Integer.parseInt(st.nextToken());
        }

        BigInteger totalCost = new BigInteger(String.valueOf(costs[0]*dists[0]));
        long minCost = costs[0];
        for (int i = 1 ; i < n-1 ; i++) {
            if (costs[i] < minCost) {
                minCost = costs[i];
            }
            totalCost = totalCost.add(BigInteger.valueOf(dists[i]).multiply(BigInteger.valueOf(minCost)));
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(totalCost.toString());
        bw.flush();
    }
}