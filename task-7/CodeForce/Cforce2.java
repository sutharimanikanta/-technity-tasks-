import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int n = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character
        
        for (int i = 0; i < n; i++) {
            String word = scanner.nextLine();
            
            if (word.length() > 10) {
                char firstLetter = word.charAt(0);
                char lastLetter = word.charAt(word.length() - 1);
                int numLettersBetween = word.length() - 2;
                
                System.out.println(firstLetter + Integer.toString(numLettersBetween) + lastLetter);
            } else {
                System.out.println(word);
            }
        }
        
        scanner.close();
    }
}
