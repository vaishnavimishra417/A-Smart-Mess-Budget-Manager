import datetime

# --- 1. DATA (7-Day Menu) ---
mess_menu = {
    "Monday": {"Breakfast": "Poha & Tea", "Lunch": "Rajma Chawal", "Dinner": "Paneer Butter Masala"},
    "Tuesday": {"Breakfast": "Aloo Paratha", "Lunch": "Kadhi Pakoda", "Dinner": "Egg Curry"},
    "Wednesday": {"Breakfast": "Idli Sambar", "Lunch": "Chole Bhature", "Dinner": "Chicken Curry"},
    "Thursday": {"Breakfast": "Bread Pakora", "Lunch": "Dal Makhani", "Dinner": "Kadhai Paneer"},
    "Friday": {"Breakfast": "Puri Sabzi", "Lunch": "Dal Arhar & Rice", "Dinner": "Veg Biryani"},
    "Saturday": {"Breakfast": "Sabudana Khichdi", "Lunch": "Veg Biryani & Raita", "Dinner": "Chana Masala"},
    "Sunday": {"Breakfast": "Chole Bhature", "Lunch": "Shahi Paneer & Naan", "Dinner": "Malai Kofta"}
}

# --- 2. FUNCTIONS ---

def view_menu():
    """Asks the user for the day and displays that day's menu."""
    # Ask the user for the day
    user_day = input("\nWhich day's menu do you want to see? (e.g., Monday): ").strip().capitalize()
    
    print(f"\n--- {user_day} Mess Schedule ---")
    
    # Check if the day exists in our dictionary
    today_meals = mess_menu.get(user_day)
    
    if today_meals:
        print(f"B-Fast: {today_meals['Breakfast']}")
        print(f"Lunch:  {today_meals['Lunch']}")
        print(f"Dinner: {today_meals['Dinner']}")
    else:
        print("Error: Please enter a valid day of the week.")

def log_expense():
    """Logs food spending to a text file."""
    item = input("What did you buy? ")
    price = input("How much did it cost? ")
    with open("expenses.txt", "a") as f:
        f.write(f"{item}: Rs.{price}\n")
    print("Logged! Data saved to expenses.txt.")

# --- 3. MAIN LOOP ---

def main():
    while True:
        print("\n===== CAMPUS CRATE: VIT BHOPAL =====")
        print("1. View Mess Menu (Select Day)")
        print("2. Log Outside Food Expense")
        print("3. Exit Program")
        
        choice = input("\nEnter choice (1-3): ")
        
        if choice == '1':
            view_menu()
        elif choice == '2':
            log_expense()
        elif choice == '3':
            print("Exiting... Good luck with your studies!")
            break
        else:
            print("Invalid input. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
