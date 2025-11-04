import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = toInt(st.nextToken()), m = toInt(st.nextToken());
        int[] mems = getIntArray(br.readLine(), n);
        int[] costs = getIntArray(br.readLine(), n);
        int totalCost = 0;
        for (int i = 0; i < n; i++) {
            totalCost += costs[i];
        }

        int[][] apps = new int[n+1][totalCost+1];
        for (int app = 1; app < n+1; app++) {
            for (int cost = 0; cost < totalCost + 1; cost++) {
                int notOffMem = apps[app-1][cost];
                int offMem = cost - costs[app-1] >= 0 ? apps[app-1][cost - costs[app-1]] + mems[app-1] : 0;
                apps[app][cost] = Math.max(notOffMem, offMem);
            }
        }

        for (int cost = 0; cost < totalCost + 1; cost++) {
            if (apps[n][cost] >= m) {
                System.out.println(cost);
                break;
            }
        }
    }

    public static int toInt(String s) {
        return Integer.parseInt(s);
    }

    public static int[] getIntArray(String s, int index) {
        StringTokenizer st = new StringTokenizer(s);
        int[] array = new int[index];
        for (int i = 0; i < index; i++) {
            array[i] = toInt(st.nextToken());
        }
        return array;
    }
}