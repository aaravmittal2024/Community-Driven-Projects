import java.io.IOException;
import java.text.DecimalFormat;
import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.Map;
import java.util.Scanner;

public class ATMInterfaces {
    private Scanner menuInput = new Scanner(System.in);
    private DecimalFormat moneyFormat = new DecimalFormat("'$'###,##0.00");
    private HashMap<Integer, Account> accountData = new HashMap<>();

    // Method to handle user login
    public void getLogin() throws IOException {
        int customerNumber;
        int pinNumber;
        boolean isValidLogin = false;

        while (!isValidLogin) {
            try {
                System.out.print("\nEnter your customer number: ");
                customerNumber = menuInput.nextInt();
                System.out.print("\nEnter your PIN number: ");
                pinNumber = menuInput.nextInt();

                Account account = accountData.get(customerNumber);
                if (account != null && account.getPinNumber() == pinNumber) {
                    getAccountType(account);
                    isValidLogin = true;
                } else {
                    System.out.println("\nWrong Customer Number or Pin Number");
                }
            } catch (InputMismatchException e) {
                System.out.println("\nInvalid Character(s). Only Numbers.");
                menuInput.next(); // Clear the buffer
            }
        }
    }

    // Method to select account type
    public void getAccountType(Account account) {
        boolean isDone = false;
        while (!isDone) {
            try {
                System.out.println("\nSelect the account you want to access: ");
                System.out.println(" Type 1 - Checkings Account");
                System.out.println(" Type 2 - Savings Account");
                System.out.println(" Type 3 - Exit");
                System.out.print("\nChoice: ");

                int selection = menuInput.nextInt();

                switch (selection) {
                    case 1:
                        getChecking(account);
                        break;
                    case 2:
                        getSaving(account);
                        break;
                    case 3:
                        isDone = true;
                        break;
                    default:
                        System.out.println("\nInvalid Choice.");
                }
            } catch (InputMismatchException e) {
                System.out.println("\nInvalid Choice.");
                menuInput.next();
            }
        }
    }

    // Method to handle checking account operations
    public void getChecking(Account account) {
        performAccountOperations(account, "Checkings");
    }

    // Method to handle savings account operations
    public void getSaving(Account account) {
        performAccountOperations(account, "Savings");
    }

    // Helper method to perform account operations
    private void performAccountOperations(Account account, String accountType) {
        boolean isDone = false;
        while (!isDone) {
            try {
                System.out.println("\n" + accountType + " Account: ");
                System.out.println(" Type 1 - View Balance");
                System.out.println(" Type 2 - Withdraw Funds");
                System.out.println(" Type 3 - Deposit Funds");
                System.out.println(" Type 4 - Transfer Funds");
                System.out.println(" Type 5 - Exit");
                System.out.print("\nChoice: ");

                int selection = menuInput.nextInt();

                switch (selection) {
                    case 1:
                        System.out.println("\n" + accountType + " Account Balance: " +
                                moneyFormat.format(accountType.equals("Checkings") ? account.getCheckingBalance() : account.getSavingBalance()));
                        break;
                    case 2:
                        if (accountType.equals("Checkings")) {
                            account.getCheckingWithdrawInput();
                        } else {
                            account.getSavingWithdrawInput();
                        }
                        break;
                    case 3:
                        if (accountType.equals("Checkings")) {
                            account.getCheckingDepositInput();
                        } else {
                            account.getSavingDepositInput();
                        }
                        break;
                    case 4:
                        account.getTransferInput(accountType);
                        break;
                    case 5:
                        isDone = true;
                        break;
                    default:
                        System.out.println("\nInvalid Choice.");
                }
            } catch (InputMismatchException e) {
                System.out.println("\nInvalid Choice.");
                menuInput.next();
            }
        }
    }

    // Method to create a new account
    public void createAccount() throws IOException {
        int customerNumber;
        boolean isUniqueNumber = false;

        while (!isUniqueNumber) {
            try {
                System.out.println("\nEnter your customer number: ");
                customerNumber = menuInput.nextInt();

                if (!accountData.containsKey(customerNumber)) {
                    isUniqueNumber = true;
                } else {
                    System.out.println("\nThis customer number is already registered.");
                }
            } catch (InputMismatchException e) {
                System.out.println("\nInvalid Choice.");
                menuInput.next();
            }
        }

        System.out.println("\nEnter PIN to be registered: ");
        int pinNumber = menuInput.nextInt();
        accountData.put(customerNumber, new Account(customerNumber, pinNumber));
        System.out.println("\nYour new account has been successfully registered!");
        System.out.println("\nRedirecting to login.............");
        getLogin();
    }

    // Method to display the main menu and handle user selection
    public void mainMenu() throws IOException {
        // Pre-populate with some accounts for demonstration purposes
        accountData.put(952141, new Account(952141, 191904, 1000, 5000));
        accountData.put(123, new Account(123, 123, 20000, 50000));

        boolean isDone = false;
        while (!isDone) {
            try {
                System.out.println("\n Type 1 - Login");
                System.out.println(" Type 2 - Create Account");
                System.out.print("\nChoice: ");
                int choice = menuInput.nextInt();

                switch (choice) {
                    case 1:
                        getLogin();
                        isDone = true;
                        break;
                    case 2:
                        createAccount();
                        isDone = true;
                        break;
                    default:
                        System.out.println("\nInvalid Choice.");
                }
            } catch (InputMismatchException e) {
                System.out.println("\nInvalid Choice.");
                menuInput.next();
            }
        }

        System.out.println("\nThank You for using this ATM.\n");
        menuInput.close();
        System.exit(0);
    }
}
