import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] split = br.readLine().split(" ");
        int a = Integer.parseInt(split[0]), b = Integer.parseInt(split[1]), count = 1;
        while (b > a) {
            if (b % 2 == 0) {
                b >>= 1;
            } else if (b % 10 == 1) {
                b /= 10;
            } else {
                break;
            }
            count += 1;
        }
        System.out.println(b == a ? count : -1);
    }
}