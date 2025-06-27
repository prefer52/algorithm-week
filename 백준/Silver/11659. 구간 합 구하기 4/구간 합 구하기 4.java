import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt((st.nextToken()));
        st = new StringTokenizer(br.readLine());
        int[] nums = new int[n + 1];
        int[][] ranges = new int[m][2];
        for (int i = 1; st.hasMoreTokens() ; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        for (int i = 0; i < m; i ++) {
            st = new StringTokenizer(br.readLine());
            ranges[i][0] = Integer.parseInt(st.nextToken());
            ranges[i][1] = Integer.parseInt(st.nextToken());
        }
        for (int i = 1; i < nums.length; i++) {
            nums[i] += nums[i-1];
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int[] range:ranges) {
            bw.write(String.valueOf(nums[range[1]] - nums[range[0] - 1]));
            bw.newLine();
        }
        bw.flush();
    }
}