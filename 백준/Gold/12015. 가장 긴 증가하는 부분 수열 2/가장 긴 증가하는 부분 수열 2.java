import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = toInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = toInt(st.nextToken());
        }

        List<Integer> seqs = new ArrayList<>();
        seqs.add(nums[0]);
        for (int i = 1; i < n; i++) {
            if (nums[i] > seqs.get(seqs.size() - 1)) {
                seqs.add(nums[i]);
            } else {
                int start = 0, end = seqs.size() - 1;
                while (start <= end) {
                    int mid = (start + end) / 2;
                    if (seqs.get(mid) < nums[i]) {
                        start = mid + 1;
                    } else {
                        end = mid - 1;
                    }
                }
                seqs.set(start, nums[i]);
            }
        }

        System.out.println(seqs.size());
    }

    public static int toInt(String s) {
        return Integer.parseInt(s);
    }
}