import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        long[] pados = new long[101];
        pados[1] = pados[2] = pados[3] = 1;
        pados[4] = pados[5] = 2;
        for (int i = 6; i < 101; i++) {
            pados[i] = pados[i - 1] + pados[i - 5];
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) {
            int test = Integer.parseInt(br.readLine());
            sb.append(pados[test] + "\n");
        }
        System.out.println(sb.toString().strip());
    }
}