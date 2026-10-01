# Student Finance Management System

## Introduction

Student Finance Management System is a Python-based application designed to help students manage their personal finances in an easy and organized manner. The system allows students to record their income and expenses, set monthly budgets, monitor their available balance, search transactions, and analyze their spending habits.

The main purpose of this project is to provide students with a simple financial management tool that helps them understand where their money is being spent and how much they can save. The application stores financial information permanently using a JSON file, so the data remains available even after the program is closed.

## Objectives

The main objectives of the Student Finance Management System are:

1. To maintain student income records.
2. To record daily expenses.
3. To categorize different types of expenses.
4. To calculate the current financial balance.
5. To set and monitor a monthly spending budget.
6. To analyze the student's spending patterns.
7. To calculate savings and spending statistics.
8. To store financial data permanently.
9. To search and manage previously recorded transactions.
10. To provide a simple and user-friendly finance management system.

## Features

### 1. Add Income

The system allows users to record different sources of income. Students can enter income received from sources such as monthly allowance, scholarships, part-time jobs, freelance work, gifts, or other sources.

The income record can contain information such as the amount, description, category, and date of the transaction.

Examples of income sources include:

* Monthly allowance
* Scholarship
* Part-time income
* Freelance income
* Gifts
* Other sources

### 2. Add Expense

Users can record their daily expenses in the system. Each expense can be assigned to a particular category, making it easier to understand spending habits.

Common expense categories include:

* Food
* Transport
* Education
* Shopping
* Entertainment
* Accommodation
* Recharge
* Other

For example, if a student spends ₹200 on food, the transaction can be stored with the amount, category, description, and date.

### 3. View Transactions

The system provides an option to display all recorded transactions. Users can view their income and expenses together with important information such as transaction type, amount, category, description, and date.

This feature helps students keep track of their financial activities.

### 4. Balance Calculation

The application automatically calculates the student's current balance.

The formula used is:

Total Balance = Total Income - Total Expenses

For example, if the total income is ₹10,000 and total expenses are ₹6,500:

Total Balance = ₹10,000 - ₹6,500

Total Balance = ₹3,500

Therefore, the student has ₹3,500 remaining.

### 5. Monthly Budget

Students can set a monthly spending budget according to their financial situation.

For example, a student may set a monthly expense budget of ₹8,000.

The system monitors expenses against the budget and provides warnings when spending reaches important limits.

A warning can be displayed when:

* 80% of the budget is reached.
* 100% of the budget is reached or exceeded.

This helps students control unnecessary spending.

### 6. Financial Summary

The financial summary provides an overall view of the student's financial condition.

The system can display:

* Total income
* Total expenses
* Remaining balance
* Category-wise expenses
* Highest spending category
* Highest individual expense
* Average expense
* Savings percentage

The summary helps users understand their financial habits and identify areas where they may be spending more money.

### 7. Search Transactions

The system allows users to search for previously recorded transactions.

Transactions can be searched using:

* Category
* Description
* Date

For example, the user can search for all transactions related to "Food" or search for expenses made on a particular date.

### 8. Monthly Analysis

The monthly analysis feature allows students to analyze their financial activities for a particular month.

The user can select a month and view the income and expenses recorded during that period.

This feature is useful for comparing spending patterns between different months.

### 9. Delete Transactions

Users can delete incorrect or unwanted transactions from the system.

For example, if an expense was entered twice by mistake, the duplicate transaction can be deleted.

This helps keep the financial records accurate.

### 10. Data Storage

The application uses a JSON file to store financial information.

The data is saved in:

data.json

JSON provides a simple way to store structured data. When the program starts, it can read existing information from the JSON file. When a new transaction is added, the updated information can be saved back to the file.

This ensures that financial records are not lost when the program is closed.

## Technologies Used

The following technologies are used in the project:

### Python

Python is the main programming language used to develop the application. It provides simple syntax and many built-in features that make it suitable for developing a student finance management system.

### JSON

JSON is used for storing financial information in a structured format. It allows transaction data to be saved and loaded easily.

### File Handling

Python file handling is used to read information from and write information to the JSON file.

### Datetime Module

The datetime module is used to work with dates and times. It can be used to record transaction dates and perform monthly analysis.

## Python Concepts Used

The project demonstrates several important Python programming concepts.

### Variables

Variables are used to store information such as transaction amounts, descriptions, categories, dates, budgets, and balances.

### Data Types

Different Python data types are used in the project, including:

* Integer
* Float
* String
* Boolean
* List
* Dictionary

### Operators

Arithmetic operators are used to perform calculations such as addition, subtraction, and division.

For example:

Total Balance = Total Income - Total Expenses

### Conditional Statements

`if`, `elif`, and `else` statements are used to make decisions in the program.

For example, the program can check whether the user's expenses have reached 80% or 100% of the monthly budget.

### Loops

Loops are used to repeatedly perform operations. For example, a loop can be used to display all transactions or repeatedly show the main menu until the user chooses to exit.

### Functions

Functions divide the program into smaller and reusable sections.

Examples include functions for:

* Adding income
* Adding expenses
* Viewing transactions
* Calculating balance
* Setting budgets
* Searching transactions
* Deleting transactions
* Generating financial summaries

### Lists

Lists can be used to store multiple transactions in memory.

### Dictionaries

Dictionaries can be used to store information about individual transactions.

For example, a transaction may contain:

```text
Amount
Category
Description
Date
Type
```

### Exception Handling

Exception handling is used to prevent the program from crashing when the user enters invalid information.

For example, if the program expects a number but the user enters text, an exception can be handled and an appropriate error message can be displayed.

### File Handling

File handling allows the program to save and retrieve financial information from files.

The program can open the JSON file, read its contents, modify the data, and save the updated information.

### JSON

The JSON module is used to convert Python data into JSON format and convert JSON data back into Python objects.

### Lambda Functions

Lambda functions can be used for short operations, such as sorting transactions based on amount or date.

### Modules

Python modules are used to organize the project into separate files.

For example:

```text
main.py
finance.py
```

The `main.py` file can handle the main program and user menu, while `finance.py` can contain finance-related functions.

### Date and Time

The datetime module can be used to record transaction dates and perform monthly calculations and analysis.

## Project Structure

The project can be organized as follows:

```text
Student-Finance-Management/
│
├── main.py
├── finance.py
├── data.json
└── README.md
```

### main.py

The `main.py` file is the main entry point of the application. It displays the menu and allows the user to select different operations.

### finance.py

The `finance.py` file contains functions related to finance management, such as adding income, adding expenses, calculating balances, searching transactions, and generating summaries.

### data.json

The `data.json` file is used to permanently store transaction and budget information.

### README.md

The `README.md` file contains information about the project, its features, installation instructions, usage instructions, and other relevant details.

# How to Set Up and Run the Project

## 1. Install Python

First, make sure that Python is installed on your computer.

Open Command Prompt or Terminal and type:

```text
python --version
```

If the command does not work, you can also try:

```text
python3 --version
```

The project requires Python 3.x.

## 2. Open the Project Folder

Download or copy the Student Finance Management project to your computer.

Open Command Prompt, PowerShell, or the terminal in VS Code.

Navigate to the project folder using the `cd` command.

For example:

```text
cd Desktop/Student-Finance-Management
```

If the folder is located somewhere else, provide the appropriate path.

## 3. Check the Project Files

Make sure the project folder contains the required files:

```text
Student-Finance-Management/
│
├── main.py
├── finance.py
├── data.json
└── README.md
```

If `data.json` is not present, the program can be designed to create the file automatically when it is run.

## 4. Run the Program

After opening the project folder in the terminal, run the following command:

```text
python main.py
```

On systems where Python 3 is accessed using `python3`, use:

```text
python3 main.py
```

The Student Finance Management System will start running in the terminal.

## 5. Main Menu

After starting the program, the user can be presented with a menu similar to:

```text
===== Student Finance Management System =====

1. Add Income
2. Add Expense
3. View Transactions
4. View Balance
5. Set Monthly Budget
6. Financial Summary
7. Search Transactions
8. Monthly Analysis
9. Delete Transaction
10. Exit

Enter your choice:
```

The user can enter the number corresponding to the required operation.

For example, entering `1` can open the Add Income feature, while entering `2` can open the Add Expense feature.

## 6. Adding Income

To add income, select the Add Income option.

The program can ask the user to enter information such as:

```text
Enter income amount:
Enter income category:
Enter description:
Enter date:
```

The information is then stored in the transaction records.

## 7. Adding an Expense

To record an expense, select the Add Expense option.

The system can ask for:

```text
Enter expense amount:
Enter expense category:
Enter description:
Enter date:
```

After entering the information, the expense is stored in the JSON file.

## 8. Viewing Transactions

Selecting View Transactions displays the transactions stored in the system.

The user can see details such as:

```text
Transaction Type
Amount
Category
Description
Date
```

This provides a complete record of financial activities.

## 9. Checking the Balance

The balance can be calculated automatically using the total income and total expenses.

The formula is:

```text
Balance = Total Income - Total Expenses
```

The result represents the amount remaining after expenses.

## 10. Setting a Monthly Budget

The user can select the Monthly Budget option and enter the maximum amount they want to spend during the month.

For example:

```text
Enter monthly budget: 8000
```

The system then compares the user's expenses with the selected budget.

## 11. Running Financial Analysis

The Financial Summary option provides information about the user's overall financial condition.

It can display the total income, total expenses, remaining balance, average expense, savings percentage, and category-wise spending.

## 12. Searching Transactions

The Search Transactions option allows users to find specific financial records.

The user can search using information such as:

```text
Category
Description
Date
```

This is useful when the user wants to find a particular transaction among many records.

## 13. Monthly Analysis

The user can select a specific month to analyze financial activity.

For example, the user may enter:

```text
Enter month: 09
Enter year: 2026
```

The system can then display the income and expenses recorded during that month.

## 14. Deleting Transactions

If a transaction has been entered incorrectly or is no longer required, the user can select the Delete Transaction option.

The system can display the available transactions and allow the user to select the transaction that should be removed.

## 15. Data Storage

The financial records are stored in the `data.json` file.

The JSON file ensures that information remains available after the program is closed.

For example, the data may be stored in a structured form containing transaction details, budgets, and other financial information.

## Requirements

The project requires:

```text
Python 3.x
JSON
datetime
File Handling
```

JSON and datetime are part of Python's standard library, so external packages are not required for the basic project.

Therefore, there is normally no need to use a command such as:

```text
pip install
```

## Running the Project in Visual Studio Code

The project can also be executed using Visual Studio Code.

First, open Visual Studio Code and select:

```text
File → Open Folder
```

Select the `Student-Finance-Management` project folder.

Open `main.py`.

Then select:

```text
Terminal → New Terminal
```

In the terminal, run:

```text
python main.py
```

The program will start in the VS Code terminal.

## Quick Start

The project can be started quickly by opening the terminal and entering:

```text
cd Student-Finance-Management
python main.py
```

If your computer uses `python3`, enter:

```text
cd Student-Finance-Management
python3 main.py
```

After executing the command, the Student Finance Management System will start and display the main menu.

## Conclusion

The Student Finance Management System is a simple Python-based application developed to help students organize and monitor their personal finances. It provides features for recording income and expenses, calculating balances, setting monthly budgets, searching transactions, deleting records, and analyzing spending patterns.

The project also demonstrates important Python concepts such as functions, lists, dictionaries, loops, conditional statements, exception handling, file handling, JSON, modules, lambda functions, and date-time operations.

By storing financial information in a JSON file, the application provides persistent data storage while maintaining a simple structure that is easy to understand and modify. This project can also be extended in the future with features such as graphical user interfaces, charts, login systems, database storage, expense reminders, and advanced financial reports.
