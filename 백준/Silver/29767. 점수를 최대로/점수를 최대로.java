import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        long[] scores = new long[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            scores[i] = Long.parseLong(st.nextToken());
        }

        for (int i = 1; i < n; i++) {
            scores[i] += scores[i - 1];
        }
        Arrays.sort(scores);
        Long totalScore = 0L;
        for (int i = n - 1; i > n - k - 1; i--) {
            totalScore += scores[i];
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(String.valueOf(totalScore));
        bw.flush();
    }
}