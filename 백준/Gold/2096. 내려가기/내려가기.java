import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        long l = Long.parseLong(st.nextToken()), m = Long.parseLong(st.nextToken()), r = Long.parseLong(st.nextToken());
        long minL = l, minM = m, minR = r;

        for (int i = 1; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            Long curL = Long.parseLong(st.nextToken()), curM = Long.parseLong(st.nextToken()), curR = Long.parseLong(st.nextToken());
            Long tempL = curL + Math.max(l, m), tempM = curM + Math.max(Math.max(l, m), r), tempR = curR + Math.max(m, r);
            Long tempMinL = curL + Math.min(minL, minM), tempMinM = curM + Math.min(Math.min(minL, minM), minR), tempMinR = curR + Math.min(minM, minR);
            l = tempL;
            m = tempM;
            r = tempR;
            minL = tempMinL;
            minM = tempMinM;
            minR = tempMinR;
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(Math.max(Math.max(l, m), r) + " " + Math.min(Math.min(minL, minM), minR));
        bw.flush();
    }
}