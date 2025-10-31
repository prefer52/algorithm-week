import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] budgets = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int m = Integer.parseInt(br.readLine());

        int maxBudget = 0;
        if (Arrays.stream(budgets).sum() < m) {
            System.out.println(Arrays.stream(budgets).max().getAsInt());
        } else {
            int start = 1, end = 1_000_000_000;
            while (start <= end) {
                int mid = (start + end) / 2;
                int[] allocatedBudgets = Arrays.stream(budgets).map(budget -> {
                    if (budget <= mid) {
                        return budget;
                    } else {
                        return mid;
                    }
                }).toArray();

                if (Arrays.stream(allocatedBudgets).sum() > m) {
                    end = mid - 1;
                } else {
                    maxBudget = Math.max(maxBudget, Arrays.stream(allocatedBudgets).max().getAsInt());
                    start = mid + 1;
                }
            }
            System.out.println(maxBudget);
        }
    }
}