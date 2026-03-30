import datetime

# 1. DATA (7-Day Menu) 
mess_menu = {
    "Monday": {"Breakfast": "Poha & Tea", "Lunch": "Rajma Chawal", "Dinner": "Paneer Butter Masala"},
    "Tuesday": {"Breakfast": "Aloo Paratha", "Lunch": "Kadhi Pakoda", "Dinner": "Egg Curry"},
    "Wednesday": {"Breakfast": "Idli Sambar", "Lunch": "Chole Bhature", "Dinner": "Chicken Curry"},
    "Thursday": {"Breakfast": "Bread Pakora", "Lunch": "Dal Makhani", "Dinner": "Kadhai Paneer"},
    "Friday": {"Breakfast": "Puri Sabzi", "Lunch": "Dal Arhar & Rice", "Dinner": "Veg Biryani"},
    "Saturday": {"Breakfast": "Sabudana Khichdi", "Lunch": "Veg Biryani & Raita", "Dinner": "Chana Masala"},
    "Sunday": {"Breakfast": "Chole Bhature", "Lunch": "Shahi Paneer & Naan", "Dinner": "Malai Kofta"}
}

# 2. FUNCTIONS 

def view_menu():
    user_day = input("\nWhich day's menu? (e.g., Monday): ").strip().capitalize()
    today = mess_menu.get(user_day)
    if today:
        print(f"--- {user_day} Schedule ---")
        print(f"B-Fast: {today['Breakfast']}\nLunch: {today['Lunch']}\nDinner: {today['Dinner']}")
    else:
        print("Invalid day entered.")

def log_expense():
    item = input("Item name: ")
    price = input("Price (Numbers only): ")
    if price.isdigit():
        with open("expenses.txt", "a") as f:
            f.write(f"{item}:{price}\n") # Format: Item:Price
        print("Expense Saved!")
    else:
        print("Please enter a valid numeric price.")

def view_total():
    """Reads the file and calculates the total sum."""
    total = 0
    try:
        with open("expenses.txt", "r") as f:
            for line in f:
                # Split the line at the colon and take the second part (the price)
                parts = line.strip().split(":")
                if len(parts) == 2:
                    total += int(parts[1])
        print(f"\n💰 YOUR TOTAL SPENDING: Rs. {total}")
    except FileNotFoundError:
        print("\nNo expenses logged yet!")

# 3. MAIN LOOP 

def main():
    while True:
        print("\n===== CAMPUS CRATE: VIT BHOPAL =====")
        print("1. View Mess Menu")
        print("2. Log New Expense")
        print("3. View Total Monthly Spending")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ")
        if choice == '1': view_menu()
        elif choice == '2': log_expense()
        elif choice == '3': view_total()
        elif choice == '4': break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()
