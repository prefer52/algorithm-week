import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()), x = Integer.parseInt(st.nextToken());
        int visits[] = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; st.hasMoreTokens() ; i++) {
            visits[i] = Integer.parseInt(st.nextToken());
        }
        int sum = 0;
        for (int i = 0 ; i < x ; i++) {
            sum += visits[i];
        }
        int max = sum, count = 1;
        for (int i = x ; i < n ; i++) {
            sum += visits[i] - visits[i-x];
            if (sum > max) {
                max = sum;
                count = 1;
            } else if (sum == max) {
                count++;
            }
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        if (max == 0) {
            bw.write("SAD");
        } else {
            bw.write(String.valueOf(max) + "\n" + String.valueOf(count));
        }
        bw.flush();
    }
}