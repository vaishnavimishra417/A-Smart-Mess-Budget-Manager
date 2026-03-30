import datetime

# 1. Course Concept: Dictionaries for Data Storage
mess_menu = {
    
}

def view_menu():
    day = datetime.datetime.now().strftime("%A")
    print(f"\n--- Today's Menu ({day}) ---")
    today_meals = mess_menu.get(day, "Menu not updated for today.")
    for meal, dish in today_meals.items():
        print(f"{meal}: {dish}")

def log_expense():
    # 2. Course Concept: File Handling (Input/Output)
    item = input("Enter item name: ")
    price = input("Enter price: ")
    with open("expenses.txt", "a") as f:
        f.write(f"{item}: {price}\n")
    print("Expense logged successfully!")

def main():
    while True:
        print("\n--- Campus Crate v1.0 ---")
        print("1. View Today's Mess Menu")
        print("2. Log Extra Food Expense")
        print("3. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            view_menu()
        elif choice == '2':
            log_expense()
        elif choice == '3':
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
