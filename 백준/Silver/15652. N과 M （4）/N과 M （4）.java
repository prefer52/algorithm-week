import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        int n = toInt(inputs[0]), m = toInt(inputs[1]);
        List<String> result = new ArrayList<>();
        for (int i = 1; i < n + 1; i++) {
            int[] seqs = new int[m];
            seqs[0] = i;
            backTracking(seqs, 1, n, m, result);
        }

        Collections.sort(result);
        for (String sequence : result) {
            System.out.println(sequence);
        }
    }

    public static int toInt(String s) {
        return Integer.parseInt(s);
    }

    public static void backTracking(int[] seqs, int index, int n, int m, List<String> result) {
        if (index == m) {
            StringBuilder sb = new StringBuilder();
            for (int i : seqs) {
                sb.append(i + " ");
            }
            result.add(sb.toString().strip());
            return;
        }

        for (int i = seqs[index-1]; i < n + 1; i++) {
            seqs[index] = i;
            backTracking(seqs, index + 1, n, m, result);
            seqs[index] = 0;
        }
    }
}