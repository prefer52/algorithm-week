import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] grapes = new int[n + 1];
        for (int i = 0; i < n; i++) {
            grapes[i] = Integer.parseInt(br.readLine());
        }
        grapes[n] = 0;

        int[][] dp = new int[n + 1][2];
        for (int i = 0; i < n + 1; i++) {
            dp[i][0] = dp[i][1] = 0;
        }
        if (n < 3) {
            System.out.println(n == 1? grapes[0]:grapes[0]+grapes[1]);
            return;
        }
        dp[0][0] = dp[1][1] = grapes[0];
        dp[0][1] = 0;
        dp[1][0] = grapes[0] + grapes[1];
        for (int i = 2; i < n; i++) {
            dp[i][0] = Math.max(dp[i - 1][1], dp[i - 2][1] + grapes[i - 1]) + grapes[i];
            dp[i][1] = Math.max(dp[i - 1][0], dp[i - 1][1]);
        }

        System.out.println(Math.max(dp[n - 1][0], dp[n - 1][1]));
    }
}