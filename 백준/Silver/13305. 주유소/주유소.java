import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] dists = new int[n-1];
        for (int i = 0; st.hasMoreTokens(); i++) {
            dists[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        int[] costs = new int[n];
        for (int i = 0; st.hasMoreTokens(); i++) {
            costs[i] = Integer.parseInt(st.nextToken());
        }

        int totalCost = costs[0] * dists[0], minCost = costs[0];

        for (int i = 1 ; i < n-1 ; i++) {
            minCost = Math.min(minCost, costs[i]);
            totalCost += dists[i]*minCost;
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(String.valueOf(totalCost));
        bw.flush();
    }
}