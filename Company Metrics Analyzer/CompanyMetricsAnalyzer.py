import requests
import matplotlib.pyplot as plt

API_KEY = "71782d32ceb91d0902fa2973754cd7f9"
BASE_URL = "https://financialmodelingprep.com/api/v3/balance-sheet-statement/"

def get_balance_sheet(company, years):
    """Retrieve balance sheet data for a given company and number of years."""
    response = requests.get(f'{BASE_URL}{company}?limit={years}&apikey={API_KEY}')
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()

def display_financial_metrics(balance_sheet):
    """Display financial metrics based on the balance sheet data."""
    total_current_assets = balance_sheet[0]['totalCurrentAssets']
    print(f"Total Current Assets: {total_current_assets:,}")

    total_current_liabilities = balance_sheet[0]['totalCurrentLiabilities']
    print(f"Total Current Liabilities: {total_current_liabilities:,}")

    total_debt = balance_sheet[0]['totalDebt']
    cash_and_equivalents = balance_sheet[0]['cashAndCashEquivalents']
    cash_debt_difference = cash_and_equivalents - total_debt
    print(f"Cash Debt Difference: {cash_debt_difference:,}")

    goodwill_and_intangibles = balance_sheet[0]['goodwillAndIntangibleAssets']
    total_assets = balance_sheet[0]['totalAssets']
    pct_intangible = goodwill_and_intangibles / total_assets
    print(f"Pct of Intangible Assets: {pct_intangible * 100:.2f}%")

def visualize_data(balance_sheet):
    """Visualize financial data using matplotlib."""
    # Example: Plot cash-debt difference over the years
    years = [data['date'] for data in balance_sheet]
    cash_debt_differences = [data['cashAndCashEquivalents'] - data['totalDebt'] for data in balance_sheet]
    
    plt.plot(years, cash_debt_differences, marker='o')
    plt.title("Cash-Debt Difference Over Years")
    plt.xlabel("Year")
    plt.ylabel("Cash-Debt Difference")
    plt.show()

def main():
    company = input("Enter the company ticker (e.g., FB): ").upper()
    years = int(input("Enter the number of years: "))
    
    balance_sheet = get_balance_sheet(company, years)
    display_financial_metrics(balance_sheet)
    visualize_data(balance_sheet)

if __name__ == "__main__":
    main()
