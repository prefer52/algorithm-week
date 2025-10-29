import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        ArrayList<Integer>[] nodes = new ArrayList[n + 1];
        for (int i = 0; i < n + 1; i++) {
            nodes[i] = new ArrayList<>();
        }
        for (int i = 0; i < n - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int nodeA = Integer.parseInt(st.nextToken());
            int nodeB = Integer.parseInt(st.nextToken());
            nodes[nodeA].add(nodeB);
            nodes[nodeB].add(nodeA);
        }

        Deque<Integer> queue = new ArrayDeque<>();
        queue.offer(1);
        int[] parents = new int[n + 1];
        parents[1] = 1;
        while (!queue.isEmpty()) {
            int parent = queue.pollFirst();
            for (int child : nodes[parent]) {
                if (parents[child] == 0) {
                    parents[child] = parent;
                    queue.offerLast(child);
                }
            }
        }

        for (int i = 2; i < n+1; i++) {
            System.out.println(parents[i]);
        }
    }
}