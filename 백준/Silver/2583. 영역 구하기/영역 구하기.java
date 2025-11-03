import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split(" ");
        int m = toInt(str[0]), n = toInt(str[1]), k = toInt(str[2]);
        int[][] poses = new int[k][4];
        for (int i = 0; i < k; i++) {
            String[] pos = br.readLine().split(" ");
            poses[i] = new int[]{toInt(pos[0]), toInt(pos[1]), toInt(pos[2]), toInt(pos[3])};
        }

        final int[][] MOVES = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        boolean[][] spaces = new boolean[m + 2][n + 2];

        for (int i = 1; i < m + 1; i++) {
            Arrays.fill(spaces[i], 1, n + 1, true);
        }

        for (int[] pos : poses) {
            for (int row = pos[1] + 1; row < pos[3] + 1; row++) {
                for (int col = pos[0] + 1; col < pos[2] + 1; col++) {
                    spaces[row][col] = false;
                }
            }
        }

        List<Integer> result = new ArrayList<>();
        for (int y = 1; y < m + 1; y++) {
            for (int x = 1; x < n + 1; x++) {
                if (!spaces[y][x]) {
                    continue;
                }

                int area = 0;
                Deque<int[]> stack = new ArrayDeque<>();
                stack.offer(new int[]{x, y});
                spaces[y][x] = false;
                while (!stack.isEmpty()) {
                    int[] ppos = stack.poll();
                    area++;
                    for (int[] dpos : MOVES) {
                        int nx = ppos[0] + dpos[0], ny = ppos[1] + dpos[1];
                        if (spaces[ny][nx]) {
                            stack.offer(new int[]{nx, ny});
                            spaces[ny][nx] = false;
                        }
                    }
                }
                result.add(area);
            }
        }

        System.out.println(result.size());
        Collections.sort(result);
        System.out.println(result.stream().map(String::valueOf).collect(Collectors.joining(" ")));
    }

    public static int toInt(String s) {
        return Integer.parseInt(s);
    }
}