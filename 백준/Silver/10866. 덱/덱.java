import java.io.*;
import java.util.*;

public class Main {
    static int[] parents;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] instructions = new String[n];
        for (int i = 0; i < n; i++) {
            instructions[i] = br.readLine();
        }
        Deque<Integer> deque = new ArrayDeque<>();

        for (String instruction : instructions) {
            String[] instructionTokens = instruction.split(" ");
            switch (instructionTokens[0]) {
                case "push_front":
                    deque.offerFirst(Integer.parseInt(instructionTokens[1]));
                    break;
                case "push_back":
                    deque.offerLast(Integer.parseInt(instructionTokens[1]));
                    break;
                case "pop_front":
                    if (deque.isEmpty()) {
                        System.out.println(-1);
                    } else {
                        System.out.println(deque.pollFirst());
                    }
                    break;
                case "pop_back":
                    if (deque.isEmpty()) {
                        System.out.println(-1);
                    } else {
                        System.out.println(deque.pollLast());
                    }
                    break;
                case "size":
                    System.out.println(deque.size());
                    break;
                case "empty":
                    System.out.println(deque.isEmpty() ? 1 : 0);
                    break;
                case "front":
                    if (deque.isEmpty()) {
                        System.out.println(-1);
                    } else {
                        System.out.println(deque.peekFirst());
                    }
                    break;
                case "back":
                    if (deque.isEmpty()) {
                        System.out.println(-1);
                    } else {
                        System.out.println(deque.peekLast());
                    }
                    break;
            }
        }
    }
}