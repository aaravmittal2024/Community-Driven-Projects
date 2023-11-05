import java.io.IOException;

public class ATM {

    // Entry point of the ATM application
    public static void main(String[] args) throws IOException {
        // Display the introduction message
        displayIntroduction();
        
        // Create an instance of OptionMenu to handle user options
        OptionMenu optionMenu = new OptionMenu();
        
        // Invoke the main menu of the option menu to start the application
        optionMenu.mainMenu();
    }

    // Displays a welcome message to the user
    public static void displayIntroduction() {
        System.out.println("Welcome to the ATM Project!");
    }
}
