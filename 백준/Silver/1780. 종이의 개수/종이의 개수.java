import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = toInt(br.readLine());
        int[][] paper = new int[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                paper[i][j] = toInt(st.nextToken()) + 1;
            }
        }
        int[] result = new int[3];
        splitPaper(paper, 0, 0, n, result);
        System.out.println(result[0] + "\n" + result[1] + "\n" + result[2]);
    }

    public static void splitPaper(int[][] paper, int x, int y, int area, int[] result) {
        if (area == 1) {
            result[paper[y][x]]++;
            return;
        }

        int start = paper[y][x];
        int i = 0, j = 0;
        for (i = y; i < y + area; i++) {
            for (j = x; j < x + area; j++) {
                if (paper[i][j] != start) {
                    area /= 3;
                    splitPaper(paper, x, y, area, result);
                    splitPaper(paper, x + area, y, area, result);
                    splitPaper(paper, x + (area * 2), y, area, result);

                    splitPaper(paper, x, y + area, area, result);
                    splitPaper(paper, x + area, y + area, area, result);
                    splitPaper(paper, x + (area * 2), y + area, area, result);

                    splitPaper(paper, x, y + (area * 2), area, result);
                    splitPaper(paper, x + area, y + (area * 2), area, result);
                    splitPaper(paper, x + (area * 2), y + (area * 2), area, result);
                    return;
                }
            }
        }

        result[paper[y][x]]++;
    }

    public static int toInt(String s) {
        return Integer.parseInt(s);
    }
}