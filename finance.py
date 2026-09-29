import json
import os
from datetime import datetime

DATA_FILE = "data.json"


# ============================================================
# DATA HANDLING
# ============================================================

def load_data():
    """Load finance data from data.json."""

    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)

        except json.JSONDecodeError:
            print("Error reading data file. Starting with empty data.")

    return {
        "transactions": [],
        "monthly_budget": 0
    }


def save_data(data):
    """Save finance data to data.json."""

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print("\nData saved successfully!")


# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def get_amount():
    """Get a valid positive amount."""

    while True:

        try:
            amount = float(input("Enter amount (₹): "))

            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                return amount

        except ValueError:
            print("Please enter a valid number.")


def get_date():
    """Get transaction date."""

    date = input(
        "Enter date (DD-MM-YYYY) "
        "[Press Enter for today]: "
    )

    if date.strip() == "":
        return datetime.now().strftime("%d-%m-%Y")

    try:
        datetime.strptime(date, "%d-%m-%Y")
        return date

    except ValueError:
        print("Invalid date format.")
        print("Today's date will be used.")

        return datetime.now().strftime("%d-%m-%Y")


def print_line():
    print("=" * 65)


# ============================================================
# INCOME
# ============================================================

def add_income(data):

    print_line()
    print("ADD INCOME")
    print_line()

    amount = get_amount()

    source = input("Enter income source: ")

    description = input("Enter description: ")

    date = get_date()

    transaction = {
        "type": "income",
        "amount": amount,
        "category": source,
        "description": description,
        "date": date
    }

    data["transactions"].append(transaction)

    save_data(data)

    print("\nIncome added successfully!")


# ============================================================
# EXPENSE
# ============================================================

def add_expense(data):

    print_line()
    print("ADD EXPENSE")
    print_line()

    amount = get_amount()

    categories = [
        "Food",
        "Transport",
        "Education",
        "Shopping",
        "Entertainment",
        "Accommodation",
        "Recharge",
        "Other"
    ]

    print("\nExpense Categories:")

    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    while True:

        try:
            choice = int(input("Select category: "))

            if 1 <= choice <= len(categories):
                category = categories[choice - 1]
                break

            print("Please select a valid category.")

        except ValueError:
            print("Please enter a number.")

    description = input("Enter description: ")

    date = get_date()

    transaction = {
        "type": "expense",
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    data["transactions"].append(transaction)

    save_data(data)

    print("\nExpense added successfully!")


# ============================================================
# BALANCE
# ============================================================

def calculate_balance(data):

    total_income = 0
    total_expense = 0

    for transaction in data["transactions"]:

        if transaction["type"] == "income":
            total_income += transaction["amount"]

        elif transaction["type"] == "expense":
            total_expense += transaction["amount"]

    balance = total_income - total_expense

    return total_income, total_expense, balance


def view_balance(data):

    print_line()
    print("CURRENT BALANCE")
    print_line()

    income, expense, balance = calculate_balance(data)

    print(f"Total Income    : ₹{income:.2f}")
    print(f"Total Expenses  : ₹{expense:.2f}")
    print(f"Current Balance : ₹{balance:.2f}")

    if balance > 0:
        print("\nStatus: Positive balance.")

    elif balance == 0:
        print("\nStatus: Balance is zero.")

    else:
        print("\nStatus: Expenses are higher than income.")


# ============================================================
# TRANSACTIONS
# ============================================================

def view_transactions(data):

    print_line()
    print("TRANSACTION HISTORY")
    print_line()

    transactions = data["transactions"]

    if not transactions:
        print("No transactions found.")
        return

    for i, transaction in enumerate(transactions, 1):

        if transaction["type"] == "income":
            symbol = "+"
        else:
            symbol = "-"

        print(f"\nTransaction #{i}")
        print(f"Type        : {transaction['type'].title()}")
        print(f"Amount      : {symbol}₹{transaction['amount']:.2f}")
        print(f"Category    : {transaction['category']}")
        print(f"Description : {transaction['description']}")
        print(f"Date        : {transaction['date']}")

        print("-" * 65)


# ============================================================
# BUDGET
# ============================================================

def set_budget(data):

    print_line()
    print("SET MONTHLY BUDGET")
    print_line()

    budget = get_amount()

    data["monthly_budget"] = budget

    save_data(data)

    print(f"\nMonthly budget set to ₹{budget:.2f}")


def budget_status(data):

    print_line()
    print("BUDGET STATUS")
    print_line()

    budget = data["monthly_budget"]

    if budget <= 0:
        print("No monthly budget has been set.")
        return

    total_expense = 0

    for transaction in data["transactions"]:

        if transaction["type"] == "expense":
            total_expense += transaction["amount"]

    remaining = budget - total_expense

    percentage = (total_expense / budget) * 100

    print(f"Monthly Budget : ₹{budget:.2f}")
    print(f"Total Spent    : ₹{total_expense:.2f}")
    print(f"Remaining      : ₹{remaining:.2f}")
    print(f"Budget Used    : {percentage:.2f}%")

    if percentage >= 100:

        print("\nWARNING: Budget exceeded!")

    elif percentage >= 80:

        print("\nWARNING: You have used more than 80% of your budget.")

    else:

        print("\nYou are within your budget.")


# ============================================================
# FINANCIAL SUMMARY
# ============================================================

def financial_summary(data):

    print_line()
    print("FINANCIAL SUMMARY")
    print_line()

    transactions = data["transactions"]

    if not transactions:
        print("No financial data available.")
        return

    income, expense, balance = calculate_balance(data)

    print(f"Total Income      : ₹{income:.2f}")
    print(f"Total Expenses    : ₹{expense:.2f}")
    print(f"Remaining Balance : ₹{balance:.2f}")

    # Category-wise expenses

    category_expenses = {}

    for transaction in transactions:

        if transaction["type"] == "expense":

            category = transaction["category"]
            amount = transaction["amount"]

            if category not in category_expenses:
                category_expenses[category] = 0

            category_expenses[category] += amount

    print("\nEXPENSE BY CATEGORY")
    print("-" * 40)

    for category, amount in category_expenses.items():

        print(f"{category:<20} ₹{amount:.2f}")

    # Highest spending category

    if category_expenses:

        highest_category = max(
            category_expenses,
            key=category_expenses.get
        )

        print("\nHighest Spending Category:")

        print(
            f"{highest_category} "
            f"(₹{category_expenses[highest_category]:.2f})"
        )

    # Highest individual expense

    expenses = [
        t for t in transactions
        if t["type"] == "expense"
    ]

    if expenses:

        highest_expense = max(
            expenses,
            key=lambda x: x["amount"]
        )

        print("\nHighest Individual Expense:")

        print(
            f"₹{highest_expense['amount']:.2f} - "
            f"{highest_expense['description']}"
        )

        # Average expense

        average = sum(
            t["amount"] for t in expenses
        ) / len(expenses)

        print(f"\nAverage Expense : ₹{average:.2f}")

    # Savings percentage

    if income > 0:

        savings_percentage = (
            balance / income
        ) * 100

        print(
            f"Savings Percentage : "
            f"{savings_percentage:.2f}%"
        )


# ============================================================
# SEARCH
# ============================================================

def search_transactions(data):

    print_line()
    print("SEARCH TRANSACTIONS")
    print_line()

    keyword = input(
        "Enter category, description or date: "
    ).lower()

    found = False

    for transaction in data["transactions"]:

        searchable_text = (
            transaction["category"]
            + " "
            + transaction["description"]
            + " "
            + transaction["date"]
        ).lower()

        if keyword in searchable_text:

            found = True

            print("\n------------------------------")

            print(
                f"Type        : "
                f"{transaction['type'].title()}"
            )

            print(
                f"Amount      : "
                f"₹{transaction['amount']:.2f}"
            )

            print(
                f"Category    : "
                f"{transaction['category']}"
            )

            print(
                f"Description : "
                f"{transaction['description']}"
            )

            print(
                f"Date        : "
                f"{transaction['date']}"
            )

    if not found:
        print("\nNo matching transactions found.")


# ============================================================
# DELETE
# ============================================================

def delete_transaction(data):

    print_line()
    print("DELETE TRANSACTION")
    print_line()

    transactions = data["transactions"]

    if not transactions:

        print("No transactions available.")
        return

    for i, transaction in enumerate(transactions, 1):

        print(
            f"{i}. "
            f"{transaction['type'].title()} | "
            f"₹{transaction['amount']:.2f} | "
            f"{transaction['category']} | "
            f"{transaction['description']}"
        )

    try:

        choice = int(
            input("\nEnter transaction number: ")
        )

        if 1 <= choice <= len(transactions):

            removed = transactions.pop(choice - 1)

            save_data(data)

            print(
                f"\nTransaction "
                f"'{removed['description']}' deleted."
            )

        else:

            print("Invalid transaction number.")

    except ValueError:

        print("Please enter a valid number.")


# ============================================================
# MONTHLY ANALYSIS
# ============================================================

def monthly_analysis(data):

    print_line()
    print("MONTHLY EXPENSE ANALYSIS")
    print_line()

    month = input(
        "Enter month and year (MM-YYYY): "
    )

    monthly_expenses = []

    for transaction in data["transactions"]:

        if transaction["type"] != "expense":
            continue

        try:

            transaction_date = datetime.strptime(
                transaction["date"],
                "%d-%m-%Y"
            )

            transaction_month = (
                transaction_date.strftime("%m-%Y")
            )

            if transaction_month == month:
                monthly_expenses.append(transaction)

        except ValueError:
            continue

    if not monthly_expenses:

        print("\nNo expenses found for this month.")
        return

    total = sum(
        t["amount"]
        for t in monthly_expenses
    )

    print(
        f"\nTotal Expenses for {month}: "
        f"₹{total:.2f}"
    )

    print("\nExpenses:")

    for transaction in monthly_expenses:

        print(
            f"- ₹{transaction['amount']:.2f} | "
            f"{transaction['category']} | "
            f"{transaction['description']}"
        )

    average = total / len(monthly_expenses)

    print(
        f"\nNumber of Transactions : "
        f"{len(monthly_expenses)}"
    )

    print(
        f"Average Expense        : "
        f"₹{average:.2f}"
    )