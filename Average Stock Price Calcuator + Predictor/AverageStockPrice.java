/**
 * This program allows users to manage a stock portfolio through an interactive menu.
 * Users can buy/sell stocks, distribute dividends, perform stock splits, and view stock reports.
 * The program tracks transaction history and provides insights on average stock prices.
 */


import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class AverageStockPrice {
    public static void main(String[] args) {
        Portfolio portfolio = new Portfolio();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Choose an option:");
            System.out.println("1. Buy stock");
            System.out.println("2. Sell stock");
            System.out.println("3. Distribute dividend");
            System.out.println("4. Perform stock split");
            System.out.println("5. View stock report");
            System.out.println("6. Exit");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter ticker: ");
                    String buyTicker = scanner.next();
                    System.out.print("Enter price: ");
                    double buyPrice = scanner.nextDouble();
                    System.out.print("Enter shares: ");
                    int buyShares = scanner.nextInt();
                    portfolio.buy(buyTicker, buyPrice, buyShares);
                    break;
                case 2:
                    System.out.print("Enter ticker: ");
                    String sellTicker = scanner.next();
                    System.out.print("Enter price: ");
                    double sellPrice = scanner.nextDouble();
                    System.out.print("Enter shares: ");
                    int sellShares = scanner.nextInt();
                    portfolio.sell(sellTicker, sellPrice, sellShares);
                    break;
                case 3:
                    System.out.print("Enter ticker: ");
                    String dividendTicker = scanner.next();
                    System.out.print("Enter dividend amount per share: ");
                    double dividendAmount = scanner.nextDouble();
                    portfolio.getStock(dividendTicker).distributeDividend(dividendAmount);
                    break;
                case 4:
                    System.out.print("Enter ticker for stock split: ");
                    String splitTicker = scanner.next();
                    portfolio.getStock(splitTicker).performStockSplit();
                    break;
                case 5:
                    System.out.print("Enter ticker to view report: ");
                    String reportTicker = scanner.next();
                    System.out.println(portfolio.getStock(reportTicker).generateReport());
                    break;
                case 6:
                    System.out.println("Exiting...");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice. Try again.");
            }
        }
    }
}

class Portfolio {
    private List<Stock> stocks = new ArrayList<>();

    public void buy(String ticker, double price, int shares) {
        Stock stock = getStock(ticker);
        if (stock == null) {
            stock = new Stock(ticker);
            stocks.add(stock);
        }
        stock.buy(price, shares);
    }

    public void sell(String ticker, double price, int shares) {
        Stock stock = getStock(ticker);
        if (stock != null) {
            stock.sell(price, shares);
        }
    }

    public Stock getStock(String ticker) {
        for (Stock stock : stocks) {
            if (stock.getTicker().equals(ticker)) {
                return stock;
            }
        }
        return null;
    }
}

class Stock {
    private String ticker;
    private int shares;
    private double capital;
    private double price;
    private List<String> transactionHistory = new ArrayList<>();

    public Stock(String ticker) {
        this.ticker = ticker;
    }

    public void buy(double p, int s) {
        shares += s;
        price = p;
        capital += s * p;
        transactionHistory.add("Bought " + s + " shares at " + p);
    }

    public void sell(double p, int s) {
        if (s > shares) {
            System.out.println("Error: Not enough shares to sell.");
            return;
        }
        shares -= s;
        price = p;
        capital -= s * p;
        transactionHistory.add("Sold " + s + " shares at " + p);
    }

    public void distributeDividend(double amountPerShare) {
        capital -= amountPerShare * shares;
        transactionHistory.add("Distributed dividend of " + amountPerShare + " per share");
    }

    public void performStockSplit() {
        shares *= 2;
        transactionHistory.add("Performed a 2-for-1 stock split");
    }

    public int getShares() {
        return shares;
    }

    public double getPrice() {
        return price;
    }

    public double getAveragePrice() {
        return capital / getShares();
    }

    public String getTicker() {
        return ticker;
    }

    public List<String> getTransactionHistory() {
        return transactionHistory;
    }

    public String generateReport() {
        StringBuilder report = new StringBuilder();
        report.append("Report for stock: ").append(ticker).append("\n");
        report.append("Shares: ").append(shares).append("\n");
        report.append("Last transaction price: ").append(price).append("\n");
        report.append("Average price: ").append(getAveragePrice()).append("\n");
        report.append("Transaction history: \n");
        for (String transaction : transactionHistory) {
            report.append(transaction).append("\n");
        }
        return report.toString();
    }
}
