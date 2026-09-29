import finance


# ============================================================
# MAIN MENU
# ============================================================

def display_menu():

    print("\n")
    finance.print_line()

    print("       STUDENT FINANCE MANAGEMENT SYSTEM")

    finance.print_line()

    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Balance")
    print("5. Set Monthly Budget")
    print("6. View Budget Status")
    print("7. Financial Summary")
    print("8. Search Transactions")
    print("9. Monthly Expense Analysis")
    print("10. Delete Transaction")
    print("11. Save Data")
    print("12. Exit")

    finance.print_line()


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    # Load existing data
    data = finance.load_data()

    print("\n")
    print("=" * 65)
    print("     WELCOME TO STUDENT FINANCE MANAGER")
    print("=" * 65)

    while True:

        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":

            finance.add_income(data)

        elif choice == "2":

            finance.add_expense(data)

        elif choice == "3":

            finance.view_transactions(data)

        elif choice == "4":

            finance.view_balance(data)

        elif choice == "5":

            finance.set_budget(data)

        elif choice == "6":

            finance.budget_status(data)

        elif choice == "7":

            finance.financial_summary(data)

        elif choice == "8":

            finance.search_transactions(data)

        elif choice == "9":

            finance.monthly_analysis(data)

        elif choice == "10":

            finance.delete_transaction(data)

        elif choice == "11":

            finance.save_data(data)

        elif choice == "12":

            finance.save_data(data)

            print("\nThank you for using")
            print("Student Finance Management System!")

            print("\nGoodbye!")

            break

        else:

            print("\nInvalid choice.")
            print("Please enter a number between 1 and 12.")


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()