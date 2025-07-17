import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String a = br.readLine().strip();
        String b = br.readLine().strip();

        int[][] dp = new int[b.length() + 1][a.length() + 1];
        for (int i = 1; i < b.length() + 1; i++) {
            for (int j = 1; j < a.length() + 1; j++) {
                dp[i][j] = a.charAt(j - 1) == b.charAt(i - 1) ? dp[i - 1][j - 1] + 1 : Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }

        System.out.println(dp[b.length()][a.length()]);
    }
}