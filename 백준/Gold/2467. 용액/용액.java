import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Long[] liquids = new Long[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            liquids[i] = Long.parseLong(st.nextToken());
        }
        int start = 0, end = n-1, minStart = 0, minEnd = n-1;
        Long minSum = Math.abs(liquids[start] + liquids[end]);

        while (start < end) {
            Long liquidSum = liquids[start] + liquids[end];
            if (minSum > Math.abs(liquidSum)) {
                minSum = Math.abs(liquidSum);
                minStart = start;
                minEnd = end;
            }
            
            if (liquidSum > 0) {
                end -= 1;
            } else {
                start += 1;
            }
        }
        
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(liquids[minStart] + " " + liquids[minEnd]);
        bw.flush();
    }
}