import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = toInt(br.readLine());
        int[] nums = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = toInt(st.nextToken());
        }
        Arrays.sort(nums);
        int x = toInt(br.readLine());
        int start = 0, end = n - 1, result = 0;

        while (start < n - 1 && start < end) {
            int numSum = nums[start] + nums[end];
            if (numSum == x) {
                result++;
                start++;
            } else if (numSum < x) {
                start++;
            } else {
                end--;
            }
        }

        System.out.println(result);
    }

    public static int toInt(String s) {
        return Integer.parseInt(s);
    }
}