import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine().strip());
        int[][] spaces = new int[n+2][];
        spaces[0] = new int[n+2];
        spaces[n+1] = new int[n+2];
        Arrays.fill(spaces[0], 100);
        Arrays.fill(spaces[n+1], 100);
        for (int i = 1; i <= n; i++) {
            spaces[i] = Arrays.stream(("100 " + br.readLine() + " 100").split(" ")).mapToInt(Integer::valueOf).toArray();
        }
        int[][] MOVES = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

        int[] sharkPos = new int[3];
        boolean find = false;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++)
                if (spaces[i][j] == 9) {
                    sharkPos = new int[]{i, j, 0};
                    spaces[i][j] = 0;
                    find = true;
                    break;
                }
            if (find) {
                break;
            }
        }
        int sharkLevel = 2, eatingCount = 0;
        ArrayDeque<int[]> deq = new ArrayDeque<>();
        boolean[][] visited = new boolean[n+2][n+2];

        while(true) {
            visited[sharkPos[0]][sharkPos[1]] = true;
            deq.add(sharkPos);
            ArrayList<int[]> eatingList = new ArrayList<>();
            while (!deq.isEmpty()) {
                int[] infos = deq.poll();
                infos[2] += 1;
                for (int[] mv:MOVES) {
                    int dy = mv[0] + infos[0];
                    int dx = mv[1] + infos[1];
                    if (!visited[dy][dx]) {
                        if (0 < spaces[dy][dx] && spaces[dy][dx] < sharkLevel) {
                            eatingList.add(new int[] {dy, dx, infos[2]});
                            visited[dy][dx] = true;
                        } else if (spaces[dy][dx] == sharkLevel || spaces[dy][dx] == 0) {
                            visited[dy][dx] = true;
                            deq.add(new int[]{dy, dx, infos[2]});
                        }
                    }
                }
            }
            if (eatingList.isEmpty()) {
                break;
            }
            eatingList.sort((a, b) -> {
                if (a[2] != b[2]) {
                    return a[2] - b[2];
                } else if (a[0] != b[0]) {
                    return a[0] - b[0];
                } else {
                    return a[1] - b[1];
                }
            });
            int[] curs = eatingList.get(0);
            sharkPos = curs;
            eatingCount += 1;
            spaces[curs[0]][curs[1]] = 0;
            deq.clear();
            if (eatingCount == sharkLevel) {
                sharkLevel += 1;
                eatingCount = 0;
            }
            visited = new boolean[n+2][n+2];
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(String.valueOf(sharkPos[2] - 1));
        bw.close();
    }
}