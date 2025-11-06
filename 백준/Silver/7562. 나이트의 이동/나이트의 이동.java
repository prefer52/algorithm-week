import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader br;

    public static void main(String[] args) throws Exception {
        br = new BufferedReader(new InputStreamReader(System.in));
        int[][] MOVES = new int[][]{{-2, -1}, {-2, 1}, {-1, -2}, {-1, 2}, {1, -2}, {1, 2}, {2, -1}, {2, 1}};
        int t = toInt(br.readLine());
        for (int i = 0; i < t; i++) {
            int l = toInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            int curX = toInt(st.nextToken()), curY = toInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            int toX = toInt(st.nextToken()), toY = toInt(st.nextToken());

            int[][] chess = new int[l][l];
            Deque<int[]> deque = new ArrayDeque<>();
            deque.offer(new int[]{curX, curY, 0});
            while (!deque.isEmpty()) {
                int[] pos = deque.pollFirst();
                if (pos[0] == toX && pos[1] == toY) {
                    System.out.println(pos[2]);
                    break;
                }
                for (int[] move : MOVES) {
                    int nx = pos[0] + move[0], ny = pos[1] + move[1];
                    if (isIn(nx, ny, l) && chess[nx][ny] == 0) {
                        chess[nx][ny] = pos[2] + 1;
                        deque.offer(new int[]{nx, ny, pos[2] + 1});
                    }
                }
            }
        }
    }

    static int toInt(String s) {
        return Integer.parseInt(s);
    }

    static boolean isIn(int x, int y, int size) {
        return (x >= 0 && x < size && y >= 0 && y < size);
    }
}