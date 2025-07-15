import java.io.*;
import java.util.*;

public class Main {
    static int[] color_count = {0, 0};
    static int[][] color_paper;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        color_paper = new int[n][n];
        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < n; j++) {
                color_paper[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        count_paper(0, 0, n);
        System.out.println(color_count[0] + "\n" + color_count[1]);
    }

    public static void count_paper(int x1, int y1, int n) {
        if (n == 1) {
            color_count[color_paper[y1][x1]] += 1;
            return;
        }

        int init_color = color_paper[y1][x1];
        for (int i = y1; i < y1 + n; i++) {
            for (int j = x1; j < x1 + n; j++) {
                if (color_paper[i][j] != init_color) {
                    n /= 2;
                    count_paper(x1, y1, n);
                    count_paper(x1 + n, y1, n);
                    count_paper(x1, y1 + n, n);
                    count_paper(x1 + n, y1 + n, n);
                    return;
                }
            }
        }
        color_count[init_color] += 1;
    }
}