import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] instructions = new String[n];
        for (int i = 0; i < n; i++) {
            instructions[i] = br.readLine();
        }

        Deque<String> queue = new ArrayDeque<>();
        for (String instruction : instructions) {
            String[] splitInstruction = instruction.split(" ");
            switch (splitInstruction[0]) {
                case "push":
                    queue.offer(splitInstruction[1]);
                    break;
                case "pop":
                    System.out.println(queue.isEmpty() ? -1 : queue.pollFirst());
                    break;
                case "size":
                    System.out.println(queue.size());
                    break;
                case "empty":
                    System.out.println(queue.isEmpty() ? 1 : 0);
                    break;
                case "front":
                    System.out.println(queue.isEmpty() ? -1 : queue.peekFirst());
                    break;
                case "back":
                    System.out.println(queue.isEmpty() ? -1 : queue.peekLast());
                    break;
            }
        }
    }
}