import java.io.*;
import java.util.*;

public class Main {
    static int[] parents;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        parents = new int[n + 1];
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        for (int i = 0; i < n + 1; i++) {
            parents[i] = i;
        }

        StringTokenizer st;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()), b = Integer.parseInt(st.nextToken()), c = Integer.parseInt(st.nextToken());
            heap.offer(new int[]{c, a, b});
        }

        int result = 0;
        while (!heap.isEmpty()) {
            int[] cab = heap.poll();
            if (findParents(cab[1]) != findParents(cab[2])) {
                unionParents(cab[1], cab[2]);
                result += cab[0];
            }
        }

        System.out.println(result);
    }

    public static int findParents(int a) {
        while (a != parents[a]) {
            a = parents[a];
        }
        return a;
    }

    public static void unionParents(int a, int b) {
        a = findParents(a);
        b = findParents(b);
        if (a > b) {
            parents[a] = b;
        } else {
            parents[b] = a;
        }
    }
}