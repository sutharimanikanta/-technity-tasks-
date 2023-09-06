import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        
        long n = scanner.nextLong();
        long m = scanner.nextLong();
        long a = scanner.nextLong();

        
        long flagstonesWidth = (long) Math.ceil((double) n / a);
        long flagstonesHeight = (long) Math.ceil((double) m / a);

        
        long totalFlagstones = flagstonesWidth * flagstonesHeight;

        
        System.out.println(totalFlagstones);

        scanner.close();
    }
}
