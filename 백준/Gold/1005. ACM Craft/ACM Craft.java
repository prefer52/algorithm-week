import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = toInt(br.readLine());
        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = toInt(st.nextToken()), k = toInt(st.nextToken());
            int[] delays = new int[n + 1];
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                delays[j + 1] = toInt(st.nextToken());
            }

            List<Integer>[] nexts = new ArrayList[n + 1];
            for (int j = 0; j < n + 1; j++) {
                nexts[j] = new ArrayList<>();
            }
            int[] indegrees = new int[n + 1];
            for (int j = 0; j < k; j++) {
                st = new StringTokenizer(br.readLine());
                int before = toInt(st.nextToken()), after = toInt(st.nextToken());
                nexts[before].add(after);
                indegrees[after]++;
            }

            int target = toInt(br.readLine());
            PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[1] - b[1]);
            for (int j = 1; j < n + 1; j++) {
                if (indegrees[j] == 0) {
                    heap.add(new int[]{j, delays[j]});
                }
            }

            int time = 0;
            while (indegrees[target] != 0) {
                int[] constructInfo = heap.poll();
                time += constructInfo[1];
                heap.iterator().forEachRemaining(ci -> ci[1] -= constructInfo[1]);
                for (int next : nexts[constructInfo[0]]) {
                    --indegrees[next];
                    if (indegrees[next] == 0) {
                        heap.add(new int[]{next, delays[next]});
                    }
                }
            }
            System.out.println(time + delays[target]);
        }
    }

    static int toInt(String s) {
        return Integer.parseInt(s);
    }
}