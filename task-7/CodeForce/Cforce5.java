import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int value = 0;

        for (int i = 0; i < n; i++) {
            String instruction = scanner.next();
            if (instruction.equals("++")) {
                value++;
            } else if (instruction.equals("--")) {
                value--;
            }
        }

        System.out.println(value);

        scanner.close();
    }
}
