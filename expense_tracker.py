import csv
import os
import matplotlib.pyplot as plt

# Define the CSV file
CSV_FILE = "expenses.csv"

# Initialize CSV file with headers if not exists
def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])  # Column headers

# Add an Expense
def add_expense(date, category, amount, description):
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("Expense added successfully!")

# View All Expenses
def view_expenses():
    with open(CSV_FILE, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        print("\nExpenses:")
        for row in reader:
            print(row)

# Filter Expenses by Category
def filter_by_category(category):
    with open(CSV_FILE, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        print(f"\nExpenses in category '{category}':")
        for row in reader:
            if row[1] == category:
                print(row)

# Delete an Expense (by row number)
def delete_expense(row_number):
    with open(CSV_FILE, mode="r") as file:
        rows = list(csv.reader(file))

    if row_number < 1 or row_number >= len(rows):
        print("Invalid row number!")
        return

    del rows[row_number]

    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Expense deleted successfully!")

# Show Expense Summary
def expense_summary():
    summary = {}

    with open(CSV_FILE, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            category = row[1]
            amount = float(row[2])
            summary[category] = summary.get(category, 0) + amount

    print("\nExpense Summary:")
    for category, total in summary.items():
        print(f"{category}: ${total:.2f}")

# Show Expense Chart
def show_expense_chart():
    summary = {}

    with open(CSV_FILE, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            category = row[1]
            amount = float(row[2])
            summary[category] = summary.get(category, 0) + amount

    if not summary:
        print("No expenses to display.")
        return

    categories = list(summary.keys())
    amounts = list(summary.values())

    plt.figure(figsize=(7, 7))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title("Expense Distribution")
    plt.show()

# CLI Menu for User
def main():
    initialize_csv()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter by Category")
        print("4. Delete Expense")
        print("5. Show Summary")
        print("6. Show Expense Chart")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            add_expense(date, category, amount, description)
        
        elif choice == "2":
            view_expenses()

        elif choice == "3":
            category = input("Enter category to filter: ")
            filter_by_category(category)

        elif choice == "4":
            row_number = int(input("Enter row number to delete (starting from 1): "))
            delete_expense(row_number)

        elif choice == "5":
            expense_summary()

        elif choice == "6":
            show_expense_chart()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
