import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        int[] nums = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int max_num = nums[0];
        for (int i = 1; i < n; i++) {
            nums[i] = Math.max(nums[i], nums[i-1] + nums[i]);
            max_num = Math.max(max_num, nums[i]);
        }
        System.out.println(max_num);
    }
}