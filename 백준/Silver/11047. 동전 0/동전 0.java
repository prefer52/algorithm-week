import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nk[] = br.readLine().split(" ");
        int n  = Integer.parseInt(nk[0]), k = Integer.parseInt(nk[1]);
        Integer coins[] = new Integer[n];
        for(int i = 0 ; i < n ; i++) {
            coins[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(coins, Collections.reverseOrder());

        int count = 0;
        for (int cost:coins) {
            count += k / cost;
            k %= cost;
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(String.valueOf(count));
        bw.flush();
    }
}