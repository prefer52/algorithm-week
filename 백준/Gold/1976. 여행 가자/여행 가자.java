import java.util.*;
import java.io.*;

public class Main {
    static int[] parents;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = toInt(br.readLine());
        int m = toInt(br.readLine());

        List<Integer>[] cities = new ArrayList[n + 1];
        for (int i = 0; i < n + 1; i++) {
            cities[i] = new ArrayList<>();
        }

        parents = new int[n + 1];
        for (int i = 1; i < n + 1; i++) {
            parents[i] = i;
        }

        for (int city = 0; city < n; city++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                int connected = toInt(st.nextToken());
                if (connected == 1) {
                    cities[city + 1].add(i + 1);
                    union(city + 1, i + 1);
                }
            }
        }

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] plans = new int[m];
        for (int i = 0; i < m; i++) {
            plans[i] = toInt(st.nextToken());
        }
        
        for (int i = 1; i < m; i++) {
            if (findParent(plans[i - 1]) != findParent(plans[i])) {
                System.out.println("NO");
                return;
            }
        }
        System.out.println("YES");
    }

    static int toInt(String s) {
        return Integer.parseInt(s);
    }

    static int findParent(int node) {
        while (parents[node] != node) {
            node = parents[node];
        }

        return parents[node];
    }

    static void union(int a, int b) {
        a = findParent(a);
        b = findParent(b);

        if (a > b) {
            parents[a] = b;
        } else {
            parents[b] = a;
        }
    }
}