import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

def initialize_file():
    # Create the CSV file with headers if it doesn't exist
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file: # Create file as a writer, newline='' to avoid blank lines
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d") # Current date
    category = input("Enter category (Food, Travel, Rent, etc.): ")
    description = input("Enter description: ")
    
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("❌ Invalid amount.")
        return

    with open(FILENAME, mode='a', newline='') as file: # Append mode 
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("✅ Expense added successfully!")

def view_expenses():
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader) # Skip header
        print("\n--- All Expenses ---")
        for row in reader:
            print(f"Date: {row[0]}, Category: {row[1]}, Desc: {row[2]}, Amount: ${row[3]}")

def total_expenses():
    total = 0
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += float(row[3])
    print(f"\n💰 Total Expenses: ${total:.2f}")

def filter_by_category():
    category = input("Enter category to filter: ")
    found = False
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        print(f"\n--- Expenses in '{category}' ---")
        for row in reader:
            if row[1].lower() == category.lower():
                print(f"{row[0]} | {row[2]} | ${row[3]}")
                found = True
    if not found:
        print("No expenses found for this category.")

def menu():
    print("""
📊 Personal Expense Tracker
1. Add Expense
2. View All Expenses
3. View Total Expenses
4. Filter by Category
5. Exit
""")

def main():
    initialize_file()
    while True:
        menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            filter_by_category()
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__": 
    main()
