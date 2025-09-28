# ---- Global Conversion Factors ----
KG_TO_LB = 2.20462
LITER_TO_GALLON = 0.264172

# ---- Conversion Functions ----
def kg_to_lb(kg):
    return kg * KG_TO_LB

def liter_to_gallon(liter):
    return liter * LITER_TO_GALLON

# ---- Menu Display ----
def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Convert Units")
    print("5. Exit")

# ---- Main Program ----
def main():
    shopping_list = []  # required array

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-5): "))  # must be an integer
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' added to shopping list.")

        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from shopping list.")
            else:
                print(f"'{item}' not found in shopping list.")

        elif choice == 3:
            if shopping_list:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Shopping list is empty.")

        elif choice == 4:
            print("\nUnit Converter")
            try:
                sub_choice = int(input("Enter 1 for kg→lb, 2 for liter→gallon: "))
                if sub_choice == 1:
                    kg = float(input("Enter weight in kg: "))
                    print(f"{kg} kg = {kg_to_lb(kg):.2f} lb")
                elif sub_choice == 2:
                    liter = float(input("Enter volume in liters: "))
                    print(f"{liter} L = {liter_to_gallon(liter):.2f} gallons")
                else:
                    print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == 5:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
