import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int x = toInt(br.readLine()), stick = 64;
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        heap.add(stick);
        int sum = 64;

        while (sum != x) {
            int halfStick = heap.poll() / 2;
            sum -= halfStick * 2;
            if (sum + halfStick >= x) {
                heap.add(halfStick);
                sum += halfStick;
            } else {
                heap.add(halfStick);
                heap.add(halfStick);
                sum += halfStick*2;
            }
        }

        System.out.println(heap.size());
    }

    public static int toInt(String s) {
        return Integer.parseInt(s);
    }
}