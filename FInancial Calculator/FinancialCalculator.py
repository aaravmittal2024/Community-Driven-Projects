from __future__ import annotations
from typing import List
import math

# Simple Interest Calculation
def simple_interest(principal: float, daily_interest_rate: float, days_between_payments: float) -> float:
    if days_between_payments <= 0:
        raise ValueError("days_between_payments must be > 0")
    if daily_interest_rate < 0:
        raise ValueError("daily_interest_rate must be >= 0")
    if principal <= 0:
        raise ValueError("principal must be > 0")
    return principal * daily_interest_rate * days_between_payments

# Compound Interest Calculation
def compound_interest(principal: float, nominal_annual_interest_rate_percentage: float, number_of_compounding_periods: float) -> float:
    if number_of_compounding_periods <= 0:
        raise ValueError("number_of_compounding_periods must be > 0")
    if nominal_annual_interest_rate_percentage < 0:
        raise ValueError("nominal_annual_interest_rate_percentage must be >= 0")
    if principal <= 0:
        raise ValueError("principal must be > 0")
    return principal * (
        (1 + nominal_annual_interest_rate_percentage) ** number_of_compounding_periods
        - 1
    )

# APR Interest Calculation
def apr_interest(principal: float, nominal_annual_percentage_rate: float, number_of_years: float) -> float:
    if number_of_years <= 0:
        raise ValueError("number_of_years must be > 0")
    if nominal_annual_percentage_rate < 0:
        raise ValueError("nominal_annual_percentage_rate must be >= 0")
    if principal <= 0:
        raise ValueError("principal must be > 0")
    return compound_interest(
        principal, nominal_annual_percentage_rate / 365, number_of_years * 365
    )

# Equated Monthly Installments (EMI) Calculation
def equated_monthly_installments(principal: float, rate_per_annum: float, years_to_repay: int) -> float:
    if principal <= 0:
        raise Exception("Principal borrowed must be > 0")
    if rate_per_annum < 0:
        raise Exception("Rate of interest must be >= 0")
    if years_to_repay <= 0 or not isinstance(years_to_repay, int):
        raise Exception("Years to repay must be an integer > 0")
    rate_per_month = rate_per_annum / 12
    number_of_payments = years_to_repay * 12
    return (
        principal
        * rate_per_month
        * (1 + rate_per_month) ** number_of_payments
        / ((1 + rate_per_month) ** number_of_payments - 1)
    )

# Present Value Calculation
def present_value(discount_rate: float, cash_flows: List[float]) -> float:
    if discount_rate < 0:
        raise ValueError("Discount rate cannot be negative")
    if not cash_flows:
        raise ValueError("Cash flows list cannot be empty")
    present_value = sum(
        cash_flow / ((1 + discount_rate) ** i) for i, cash_flow in enumerate(cash_flows)
    )
    return round(present_value, ndigits=2)

# Price with Tax Calculation
def price_plus_tax(price: float, tax_rate: float) -> float:
    return price * (1 + tax_rate)

# Future Value Calculation
def future_value(principal: float, rate: float, periods: int) -> float:
    return principal * (1 + rate) ** periods

# Loan Payoff Time
def loan_payoff_time(principal: float, monthly_payment: float, rate: float) -> float:
    return -math.log(1 - (rate * principal / monthly_payment)) / math.log(1 + rate)

# Mortgage Calculator
def mortgage_payment(principal: float, rate: float, years: int) -> float:
    monthly_rate = rate / 12
    payments = years * 12
    return principal * monthly_rate / (1 - (1 + monthly_rate) ** -payments)

# Retirement Planning
def retirement_savings(goal: float, years_until_retirement: int, rate: float) -> float:
    monthly_rate = rate / 12
    payments = years_until_retirement * 12
    return goal * monthly_rate / ((1 + monthly_rate) ** payments - 1)

# Investment Return
def investment_return(principal: float, rate: float, years: int) -> float:
    return principal * (1 + rate) ** years - principal

# Currency Converter
def currency_converter(amount: float, exchange_rate: float) -> float:
    return amount * exchange_rate

# Savings Goal Calculator
def savings_goal(principal: float, goal: float, rate: float, years: int) -> float:
    future_val = future_value(principal, rate, years)
    required_savings = (goal - future_val) / ((1 + rate) ** years - 1) * rate
    return required_savings

# Tax Calculator
def income_tax(income: float, tax_rate: float) -> float:
    return income * tax_rate

# Depreciation Calculator
def straight_line_depreciation(cost: float, salvage_value: float, life: int) -> float:
    return (cost - salvage_value) / life

# Inflation Impact Calculator
def inflation_impact(principal: float, inflation_rate: float, years: int) -> float:
    return principal * (1 - inflation_rate) ** years

# Tip Calculator
def tip_calculator(bill: float, tip_rate: float) -> float:
    return bill * tip_rate

def main():
    print("Welcome to the Financial Calculator!")
    while True:
        print("\nChoose an option:")
        print("1. Simple Interest Calculation")
        print("2. Compound Interest Calculation")
        print("3. APR Interest Calculation")
        print("4. Equated Monthly Installments (EMI) Calculation")
        print("5. Present Value Calculation")
        print("6. Price with Tax Calculation")
        print("7. Future Value Calculation")
        print("8. Loan Payoff Time")
        print("9. Mortgage Calculator")
        print("10. Retirement Planning")
        print("11. Investment Return")
        print("12. Currency Converter")
        print("13. Savings Goal Calculator")
        print("14. Income Tax Calculator")
        print("15. Straight Line Depreciation Calculator")
        print("16. Inflation Impact Calculator")
        print("17. Tip Calculator")
        print("18. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            principal = float(input("Enter principal: "))
            daily_interest_rate = float(input("Enter daily interest rate: "))
            days_between_payments = float(input("Enter days between payments: "))
            print(f"Simple Interest: {simple_interest(principal, daily_interest_rate, days_between_payments)}")
        elif choice == 2:
            principal = float(input("Enter principal: "))
            rate = float(input("Enter nominal annual interest rate percentage: "))
            periods = float(input("Enter number of compounding periods: "))
            print(f"Compound Interest: {compound_interest(principal, rate, periods)}")
        elif choice == 3:
            principal = float(input("Enter principal: "))
            rate = float(input("Enter nominal annual percentage rate: "))
            years = float(input("Enter number of years: "))
            print(f"APR Interest: {apr_interest(principal, rate, years)}")
        elif choice == 4:
            principal = float(input("Enter principal borrowed: "))
            rate = float(input("Enter rate of interest per annum: "))
            years = int(input("Enter years to repay the loan: "))
            print(f"EMI: {equated_monthly_installments(principal, rate, years)}")
        elif choice == 5:
            discount_rate = float(input("Enter discount rate: "))
            cash_flows = [float(x) for x in input("Enter cash flows separated by comma: ").split(",")]
            print(f"Present Value: {present_value(discount_rate, cash_flows)}")
        elif choice == 6:
            price = float(input("Enter price: "))
            tax_rate = float(input("Enter tax rate: "))
            print(f"Price with Tax: {price_plus_tax(price, tax_rate)}")
        elif choice == 7:
            principal = float(input("Enter principal: "))
            rate = float(input("Enter interest rate: "))
            periods = int(input("Enter number of periods: "))
            print(f"Future Value: {future_value(principal, rate, periods)}")
        elif choice == 8:
            principal = float(input("Enter loan principal: "))
            monthly_payment = float(input("Enter monthly payment amount: "))
            rate = float(input("Enter monthly interest rate: "))
            print(f"Loan Payoff Time (in months): {loan_payoff_time(principal, monthly_payment, rate)}")
        elif choice == 9:
            principal = float(input("Enter loan principal: "))
            rate = float(input("Enter annual interest rate: "))
            years = int(input("Enter loan term in years: "))
            print(f"Monthly Mortgage Payment: {mortgage_payment(principal, rate, years)}")
        elif choice == 10:
            goal = float(input("Enter your retirement savings goal: "))
            years_until_retirement = int(input("Enter number of years until retirement: "))
            rate = float(input("Enter expected annual return rate: "))
            print(f"Monthly Savings Required: {retirement_savings(goal, years_until_retirement, rate)}")
        elif choice == 11:
            principal = float(input("Enter initial investment: "))
            rate = float(input("Enter annual return rate: "))
            years = int(input("Enter number of years: "))
            print(f"Investment Return after {years} years: {investment_return(principal, rate, years)}")
        elif choice == 12:
            amount = float(input("Enter amount in your currency: "))
            exchange_rate = float(input("Enter the exchange rate to the desired currency: "))
            print(f"Converted Amount: {currency_converter(amount, exchange_rate)}")
        elif choice == 13:
            principal = float(input("Enter current savings: "))
            goal = float(input("Enter savings goal: "))
            rate = float(input("Enter expected annual return rate: "))
            years = int(input("Enter number of years to reach goal: "))
            print(f"Monthly Savings Required: {savings_goal(principal, goal, rate, years)}")
        elif choice == 14:
            income = float(input("Enter your income: "))
            tax_rate = float(input("Enter your tax rate: "))
            print(f"Income Tax: {income_tax(income, tax_rate)}")
        elif choice == 15:
            cost = float(input("Enter initial cost of the asset: "))
            salvage_value = float(input("Enter salvage value of the asset: "))
            life = int(input("Enter useful life of the asset in years: "))
            print(f"Annual Depreciation: {straight_line_depreciation(cost, salvage_value, life)}")
        elif choice == 16:
            principal = float(input("Enter current amount: "))
            inflation_rate = float(input("Enter expected annual inflation rate: "))
            years = int(input("Enter number of years: "))
            print(f"Value after {years} years accounting for inflation: {inflation_impact(principal, inflation_rate, years)}")
        elif choice == 17:
            bill = float(input("Enter your bill amount: "))
            tip_rate = float(input("Enter tip rate (e.g., 0.15 for 15%): "))
            print(f"Tip Amount: {tip_calculator(bill, tip_rate)}")
        elif choice == 18:
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
