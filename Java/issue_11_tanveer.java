import java.util.Random;
import java.util.Scanner;

public class issue_11_tanveer {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        int targetNumber = random.nextInt(100) + 1;
        int userInput;
        int attempts = 0;
        int score = 100; 
        int maxAttempts = 10; 

        System.out.println("Welcome to the Number Guessing Game!");
        System.out.println("Guess the number between 1 and 100. You have " + maxAttempts + " attempts.");
        
        do {
            System.out.print("Enter your guess: ");
            userInput = scanner.nextInt();
            attempts++;

            if (userInput < targetNumber) {
                System.out.println("Too low! Try again.");
                score -= 10; 
            } else if (userInput > targetNumber) {
                System.out.println("Too high! Try again.");
                score -= 10; 
            } else {
                System.out.println("Congratulations! You guessed the number.");
                score += 50; 
            }
        } while (userInput != targetNumber && attempts < maxAttempts);

        if (userInput != targetNumber) {
            System.out.println("Sorry, you've used all your attempts. The correct number was " + targetNumber + ".");
        }
        
        System.out.println("Your final score is: " + score);
        scanner.close();
    }
}