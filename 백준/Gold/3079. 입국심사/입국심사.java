import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] nm = br.readLine().split(" ");
        int n = Integer.parseInt(nm[0]);
        long m = Long.parseLong(nm[1]);

        long[] times = new long[n];
        for (int i = 0; i < n; i++) {
            times[i] = Long.parseLong(br.readLine());
        }
        Arrays.sort(times);
        long start = 1L;
        long end = times[times.length - 1]*m;
        while (start <= end) {
            long mid = (start + end)/2L;
            long total = 0L;
            for (long time : times) {
                total += mid / time;
                if (total >= m) {
                    break;
                }
            }
            if (total < m) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(String.valueOf(start));
        bw.flush();
    }
}