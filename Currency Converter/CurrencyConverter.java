import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class CurrencyConverter {

    private static final Map<String, Double> conversionRatesToUSD = new HashMap<>();

    static {
        conversionRatesToUSD.put("USD", 1.00);
        conversionRatesToUSD.put("EUR", 0.85);
        conversionRatesToUSD.put("JPY", 110.00);
        conversionRatesToUSD.put("GBP", 0.73);
        conversionRatesToUSD.put("AUD", 1.30);
        conversionRatesToUSD.put("CAD", 1.25);
        conversionRatesToUSD.put("CHF", 0.92);
        conversionRatesToUSD.put("CNY", 6.45);
        conversionRatesToUSD.put("SEK", 8.50);
        conversionRatesToUSD.put("NZD", 1.40);
        conversionRatesToUSD.put("MXN", 20.00);
        conversionRatesToUSD.put("SGD", 1.33);
        conversionRatesToUSD.put("HKD", 7.75);
        conversionRatesToUSD.put("NOK", 8.50);
        conversionRatesToUSD.put("KRW", 1100.00);
        conversionRatesToUSD.put("TRY", 8.50);
        conversionRatesToUSD.put("RUB", 75.00);
        conversionRatesToUSD.put("INR", 73.50);
        conversionRatesToUSD.put("BRL", 5.20);
        conversionRatesToUSD.put("ZAR", 15.00);
        conversionRatesToUSD.put("THB", 30.00);
        conversionRatesToUSD.put("PLN", 3.75);
        conversionRatesToUSD.put("IDR", 14500.00);
        conversionRatesToUSD.put("COP", 3600.00);
        conversionRatesToUSD.put("PKR", 160.00);
        conversionRatesToUSD.put("EGP", 15.70);
        conversionRatesToUSD.put("NGN", 380.00);
        conversionRatesToUSD.put("CLP", 700.00);
        conversionRatesToUSD.put("TWD", 28.00);
        conversionRatesToUSD.put("MYR", 4.10);
        conversionRatesToUSD.put("PHP", 50.00);
        conversionRatesToUSD.put("VND", 23000.00);
        conversionRatesToUSD.put("BDT", 85.00);
        conversionRatesToUSD.put("PEN", 3.60);
        conversionRatesToUSD.put("UYU", 42.00);
    }

    public static double convertCurrency(String fromCurrency, double amount, String toCurrency) {
        // Convert the source currency to USD
        double amountInUSD = amount / conversionRatesToUSD.get(fromCurrency);
        
        // Convert from USD to the target currency
        double convertedAmount = amountInUSD * conversionRatesToUSD.get(toCurrency);
        
        return convertedAmount;
    }

    public static void main(String[] args) {

        
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to the Currency Converter!");

        // Ask the user for input
        System.out.print("Enter the currency you want to convert from (e.g., USD, EUR, JPY): ");
        String fromCurrency = scanner.nextLine().toUpperCase();

        System.out.print("Enter the amount you have in " + fromCurrency + ": ");
        double amount = scanner.nextDouble();
        scanner.nextLine();  // Consume newline

        System.out.print("Enter the currency you want to convert to (e.g., USD, EUR, JPY): ");
        String toCurrency = scanner.nextLine().toUpperCase();

        // Perform the conversion
        double convertedAmount = convertCurrency(fromCurrency, amount, toCurrency);
        System.out.printf("Converted Amount: %.2f %s\n", convertedAmount, toCurrency);

        scanner.close();
    }
}
