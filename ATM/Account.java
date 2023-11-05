import java.text.DecimalFormat;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Account {
    // Class variables
    private int customerNumber;
    private int pinNumber;
    private double checkingAccountBalance = 0;
    private double savingsAccountBalance = 0;

    // Scanner for user input
    private Scanner input = new Scanner(System.in);
    // Formatter for currency display
    private DecimalFormat moneyFormat = new DecimalFormat("'$'###,##0.00");

    // Default constructor
    public Account() {
    }

    // Constructor with customer number and PIN
    public Account(int customerNumber, int pinNumber) {
        this.customerNumber = customerNumber;
        this.pinNumber = pinNumber;
    }

    // Constructor with all account details
    public Account(int customerNumber, int pinNumber, double checkingBalance, double savingBalance) {
        this.customerNumber = customerNumber;
        this.pinNumber = pinNumber;
        this.checkingAccountBalance = checkingBalance;
        this.savingsAccountBalance = savingBalance;
    }

    // Setters and Getters for customer number and PIN
    public int setCustomerNumber(int customerNumber) {
        this.customerNumber = customerNumber;
        return customerNumber;
    }

    public int getCustomerNumber() {
        return customerNumber;
    }

    public int setPinNumber(int pinNumber) {
        this.pinNumber = pinNumber;
        return pinNumber;
    }

    public int getPinNumber() {
        return pinNumber;
    }

    // Getters for account balances
    public double getCheckingBalance() {
        return checkingAccountBalance;
    }

    public double getSavingBalance() {
        return savingsAccountBalance;
    }

    // Withdrawal methods for checking and savings
    public double calcCheckingWithdraw(double amount) {
        checkingAccountBalance -= amount;
        return checkingAccountBalance;
    }

    public double calcSavingWithdraw(double amount) {
        savingsAccountBalance -= amount;
        return savingsAccountBalance;
    }

    // Deposit methods for checking and savings
    public double calcCheckingDeposit(double amount) {
        checkingAccountBalance += amount;
        return checkingAccountBalance;
    }

    public double calcSavingDeposit(double amount) {
        savingsAccountBalance += amount;
        return savingsAccountBalance;
    }

    // Transfer methods between accounts
    public void calcCheckTransfer(double amount) {
        checkingAccountBalance -= amount;
        savingsAccountBalance += amount;
    }

    public void calcSavingTransfer(double amount) {
        savingsAccountBalance -= amount;
        checkingAccountBalance += amount;
    }

    // User input methods for withdrawal, deposit, and transfer
    public void getCheckingWithdrawInput() {
        processWithdrawal(checkingAccountBalance, "Checkings");
    }

    public void getSavingWithdrawInput() {
        processWithdrawal(savingsAccountBalance, "Savings");
    }

    private void processWithdrawal(double accountBalance, String accountType) {
        boolean completed = false;
        while (!completed) {
            try {
                System.out.println("\nCurrent " + accountType + " Account Balance: " + moneyFormat.format(accountBalance));
                System.out.print("\nAmount you want to withdraw from " + accountType + " Account: ");
                double amount = input.nextDouble();

                if ((accountBalance - amount) >= 0 && amount >= 0) {
                    if (accountType.equals("Checkings")) {
                        calcCheckingWithdraw(amount);
                    } else {
                        calcSavingWithdraw(amount);
                    }
                    System.out.println("\nNew " + accountType + " Account Balance: " + moneyFormat.format(accountBalance));
                    completed = true;
                } else {
                    System.out.println("\nBalance Cannot be Negative.");
                }
            } catch (InputMismatchException e) {
                System.out.println("\nInvalid Choice.");
                input.next(); // Clear the buffer
            }
        }
    }

    public void getCheckingDepositInput() {
        processDeposit(checkingAccountBalance, "Checkings");
    }

    public void getSavingDepositInput() {
        processDeposit(savingsAccountBalance, "Savings");
    }

    private void processDeposit(double accountBalance, String accountType) {
        boolean completed = false;
        while (!completed) {
            try {
                System.out.println("\nCurrent " + accountType + " Account Balance: " + moneyFormat.format(accountBalance));
                System.out.print("\nAmount you want to deposit into " + accountType + " Account: ");
                double amount = input.nextDouble();

                if (amount >= 0) {
                    if (accountType.equals("Checkings")) {
                        calcCheckingDeposit(amount);
                    } else {
                        calcSavingDeposit(amount);
                    }
                    System.out.println("\nNew " + accountType + " Account Balance: " + moneyFormat.format(accountBalance));
                    completed = true;
                } else {
                    System.out.println("\nAmount must be greater than zero.");
                }
            } catch (InputMismatchException e) {
                System.out.println("\nInvalid Choice.");
                input.next(); // Clear the buffer
            }
        }
    }

    public void getTransferInput(String accountType) {
        boolean completed = false;
        while (!completed) {
            try {
                // Display transfer options based on account type
                if (accountType.equals("Checkings")) {
                    completed = processTransfer(checkingAccountBalance, savingsAccountBalance, "Savings");
                } else if (accountType.equals("Savings")) {
                    completed = processTransfer(savingsAccountBalance, checkingAccountBalance, "Checkings");
                }
            } catch (InputMismatchException e) {
                System.out.println("\nInvalid Choice.");
                input.next(); // Clear the buffer
            }
        }
    }

    private boolean processTransfer(double fromBalance, double toBalance, String toAccountType) {
        System.out.println("\nSelect an account you wish to transfer funds to:");
        System.out.println("1. " + toAccountType);
        System.out.println("2. Exit");
        System.out.print("\nChoice: ");
        int choice = input.nextInt();

        if (choice == 1) {
            System.out.println("\nCurrent " + toAccountType + " Account Balance: " + moneyFormat.format(toBalance));
            System.out.print("\nAmount you want to transfer: ");
            double amount = input.nextDouble();

            if ((fromBalance - amount) >= 0 && (toBalance + amount) >= 0 && amount >= 0) {
                if (toAccountType.equals("Savings")) {
                    calcCheckTransfer(amount);
                } else {
                    calcSavingTransfer(amount);
                }
                System.out.println("\nNew " + toAccountType + " Account Balance: " + moneyFormat.format(toBalance));
                return true;
            } else {
                System.out.println("\nBalance Cannot Be Negative.");
                return false;
            }
        } else if (choice == 2) {
            return true; // Exit the transfer process
        } else {
            System.out.println("\nInvalid Choice.");
            return false;
        }
    }
}
