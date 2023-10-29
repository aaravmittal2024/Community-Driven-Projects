import calendar
import datetime

class Expense:
    """Represent an individual expense item."""
    def __init__(self, name, category, amount) -> None:
        self.name = name
        self.category = category
        self.amount = amount

    def __repr__(self):
        """Return a string representation of the Expense object."""
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f} >"


def main():
    """Main function to run the Expense Tracker."""
    print(f"🎯 Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = 2000

    # Get user input for expense.
    expense = get_user_expense()

    # Write their expense to a file.
    save_expense_to_file(expense, expense_file_path)

    # Read file and summarize expenses.
    summarize_expenses(expense_file_path, budget)


def get_user_expense():
    """Prompt user to enter expense details and return an Expense object."""
    print(f"🎯 Getting User Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories = [
        "🍔 Food",
        "🏠 Home",
        "💼 Work",
        "🎉 Fun",
        "✨ Misc",
    ]

    # Loop to ensure the user selects a valid category
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        # Check for valid category selection
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
            )
            return new_expense
        else:
            print("Invalid category. Please try again!")


def save_expense_to_file(expense: Expense, expense_file_path):
    """Save the given Expense object to the specified file path."""
    print(f"🎯 Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a", encoding='utf-8') as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expenses(expense_file_path, budget):
    """Read the expense file, summarize expenses and compare against the budget."""
    print(f"🎯 Summarizing User Expense")
    expenses = []
    
    # Read expense file and populate list of Expense objects
    with open(expense_file_path, "r", encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category,
            )
            expenses.append(line_expense)

    # Summarize expenses by category
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    # Output summary
    print("Expenses By Category 📈:")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"💵 Total Spent: ${total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"✅ Budget Remaining: ${remaining_budget:.2f}")

    # Calculate daily budget based on remaining days of the month
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print(green(f"👉 Budget Per Day: ${daily_budget:.2f}"))


def green(text):
    """Wrap text in green color escape codes."""
    return f"\033[92m{text}\033[0m"


if __name__ == "__main__":
    main()
