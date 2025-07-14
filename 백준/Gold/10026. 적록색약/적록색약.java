import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] spaces = new String[n];
        for (int i = 0; i < n; i++) {
            spaces[i] = br.readLine();
        }
        boolean[][] visited = new boolean[n][n];
        boolean[][] combineVisited = new boolean[n][n];
        int[][] MOVES = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        int normal = 0, combined = 0;
        Deque<int[]> stack = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) {
                    stack.add(new int[]{i, j});
                    visited[i][j] = true;
                    normal += 1;
                    while (!stack.isEmpty()) {
                        int[] xy = stack.pop();
                        for (int[] move : MOVES) {
                            int ny = xy[0] + move[0], nx = xy[1] + move[1];
                            if ((0 <= ny && ny < n) && (0 <= nx && nx < n)
                                    && !visited[ny][nx] && spaces[ny].charAt(nx) == spaces[xy[0]].charAt(xy[1])) {
                                stack.push(new int[]{ny, nx});
                                visited[ny][nx] = true;
                            }
                        }
                    }
                }

                if (!combineVisited[i][j]) {
                    stack.add(new int[]{i, j});
                    combineVisited[i][j] = true;
                    combined += 1;
                    while (!stack.isEmpty()) {
                        int[] xy = stack.pop();
                        for (int[] move : MOVES) {
                            int ny = xy[0] + move[0], nx = xy[1] + move[1];
                            if ((0 <= ny && ny < n) && (0 <= nx && nx < n)
                                    && !combineVisited[ny][nx] && (spaces[ny].charAt(nx) == spaces[xy[0]].charAt(xy[1])
                                    || (spaces[ny].charAt(nx) != 'B' && spaces[xy[0]].charAt(xy[1]) != 'B'))) {
                                stack.push(new int[]{ny, nx});
                                combineVisited[ny][nx] = true;
                            }
                        }
                    }
                }
            }
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(normal + " " + combined);
        bw.flush();
    }
}