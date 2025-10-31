import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder str = new StringBuilder(br.readLine());
        if (str.indexOf("a") == -1) {
            System.out.println(0);
            return;
        }
        int aCount = 0;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == 'a') {
                aCount++;
            }
        }
        str.append(str.substring(0, aCount - 1));

        ArrayDeque<Character> window = new ArrayDeque<>();
        int minChange = 0;
        for (int i = 0; i < aCount; i++) {
            window.offer(str.charAt(i));
            minChange += str.charAt(i) - 'a';
        }
        int change = minChange;
        for (int i = aCount; i < str.length(); i++) {
            change += 'a' - window.pollFirst() + str.charAt(i) - 'a';
            window.offer(str.charAt(i));
            minChange = Math.min(change, minChange);
        }
        System.out.println(minChange);
    }
}