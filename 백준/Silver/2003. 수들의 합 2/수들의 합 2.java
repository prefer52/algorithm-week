import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
        int nums[] = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0 ; st.hasMoreTokens(); i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        int start = 0, end = 0, count = 0;
        while (end < n && start < n) {
            for (; end < n && m - nums[end] >= 0 ; end++) {
                m -= nums[end];
            }
            if (m == 0) {
                count++;
            }
            m += nums[start++];
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(String.valueOf(count));
        bw.flush();
    }
}