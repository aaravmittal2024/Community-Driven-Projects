/**
 * The  BudgetAllocation program allows users to allocate their monthly expenses by specifying categories 
 * and their respective budgeted proportions. Users can then input their actual expenses for each category, 
 * and the program will compare the actual expenses against the budgeted amounts. If users overspend in a category, 
 * they receive alerts, and based on their spending habits, the program provides suggestions for potential savings.
 */


import java.util.Scanner;
import java.util.ArrayList;
import java.util.HashMap;

public class BudgetAllocation {

    private static Scanner scan = new Scanner(System.in);
    private static HashMap<String, Double> expenseHistory = new HashMap<>();
    private static String currency = "$";

    public static void main(String[] args) {
        selectCurrency();
        double totalSpent = getTotalSpent();
        ArrayList<String> categories = new ArrayList<>();
        ArrayList<Double> proportions = getProportions(categories);
        ArrayList<Double> actualExpenses = getActualExpenses(categories);
        compareBudgetVsActual(proportions, actualExpenses, totalSpent);
        displaySuggestions();
    }

    private static void selectCurrency() {
        System.out.println("Select your currency ($, €, £, etc.):");
        currency = scan.nextLine();
    }

    private static double getTotalSpent() {
        System.out.println("How much did you spend?");
        return scan.nextDouble();
    }

    private static ArrayList<Double> getProportions(ArrayList<String> categories) {
        ArrayList<Double> proportions = new ArrayList<>();
        double cumulativeProportion = 0;
        do {
            scan.nextLine(); // Clear the buffer
            System.out.println("Enter the category for expense:");
            categories.add(scan.nextLine());
            System.out.println("Enter the proportion for " + categories.get(categories.size() - 1) + ":");
            double proportionValue = scan.nextDouble();
            proportions.add(proportionValue);
            cumulativeProportion += proportionValue;
            if (cumulativeProportion >= 100) {
                break;
            }
        } while (true);

        if (cumulativeProportion > 100) {
            double adjustedSum = 0.0;
            for (int j = 0; j < proportions.size() - 1; j++) {
                adjustedSum += proportions.get(j);
            }
            proportions.set(proportions.size() - 1, 100.0 - adjustedSum);
        }
        return proportions;
    }

    private static ArrayList<Double> getActualExpenses(ArrayList<String> categories) {
        ArrayList<Double> actualExpenses = new ArrayList<>();
        for (String category : categories) {
            System.out.println("Enter the actual expense for " + category + ":");
            double actualExpense = scan.nextDouble();
            actualExpenses.add(actualExpense);
            expenseHistory.put(category, actualExpense);
        }
        return actualExpenses;
    }

    private static void compareBudgetVsActual(ArrayList<Double> proportions, ArrayList<Double> actualExpenses, double totalSpent) {
        for (int i = 0; i < proportions.size(); i++) {
            double budgetedExpense = proportions.get(i) * totalSpent / 100.0;
            double actualExpense = actualExpenses.get(i);
            System.out.println("Budgeted for " + proportions.get(i) + "% equals " + currency + budgetedExpense);
            System.out.println("Actual expense: " + currency + actualExpense);
            if (actualExpense > budgetedExpense) {
                System.out.println("Alert! You overspent in this category by " + currency + (actualExpense - budgetedExpense));
            }
        }
    }

    private static void displaySuggestions() {
        if (expenseHistory.containsKey("Dining Out") && expenseHistory.get("Dining Out") > 100) {
            System.out.println("Suggestion: Consider dining out less to save money.");
        }
        if (expenseHistory.containsKey("Entertainment") && expenseHistory.get("Entertainment") > 50) {
            System.out.println("Suggestion: Consider cheaper entertainment options or free activities.");
        }
    }
}
