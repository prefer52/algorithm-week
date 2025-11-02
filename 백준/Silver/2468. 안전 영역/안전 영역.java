import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] spaces = new int[n+2][n+2];
        StringTokenizer st;
        for (int row = 1; row < n + 1; row++) {
            st = new StringTokenizer(br.readLine());
            for (int col = 1; col < n + 1; col++) {
                spaces[row][col] = toInt(st.nextToken());
            }
        }
        int[][] MOVES = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int max_zone_count = 1;
        for (int height = 1; height < 101; height++) {
            int zone_count = 0;
            boolean[][] visited = new boolean[n + 2][n + 2];
            for (int y = 1; y < n + 1; y++) {
                for (int x = 1; x < n + 1; x++) {
                    if (spaces[y][x] <= height || visited[y][x]) {
                        continue;
                    }

                    zone_count++;
                    visited[y][x] = true;
                    Deque<int[]> stack = new ArrayDeque<>();
                    stack.offer(new int[]{x, y});
                    while (!stack.isEmpty()) {
                        int[] pos = stack.pollLast();
                        for (int[] move : MOVES) {
                            int nx = pos[0] + move[0], ny = pos[1] + move[1];
                            if (spaces[ny][nx] > height && !visited[ny][nx]) {
                                stack.offer(new int[]{nx, ny});
                                visited[ny][nx] = true;
                            }
                        }
                    }
                }
            }

            max_zone_count = Math.max(max_zone_count, zone_count);
        }

        System.out.println(max_zone_count);
    }

    public static int toInt(String s) {
        return Integer.parseInt(s);
    }
}