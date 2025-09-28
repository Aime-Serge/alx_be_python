# ---- Global Conversion Factors ----
FAHRENHEIT_TO_CELSIUS = 5 / 9
CELSIUS_TO_FAHRENHEIT = 9 / 5
FREEZING_POINT_F = 32


def to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - FREEZING_POINT_F) * FAHRENHEIT_TO_CELSIUS


def to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT) + FREEZING_POINT_F


def display_menu():
    """Show the temperature conversion menu."""
    print("\nTemperature Conversion Tool")
    print("1. Convert Fahrenheit to Celsius")
    print("2. Convert Celsius to Fahrenheit")
    print("3. Exit")


def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("⚠️ Invalid input. Please enter a number between 1 and 3.")
            continue

        if choice == 1:
            try:
                f = float(input("Enter temperature in Fahrenheit: "))
                c = to_celsius(f)
                print(f"{f:.2f}°F = {c:.2f}°C")
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == 2:
            try:
                c = float(input("Enter temperature in Celsius: "))
                f = to_fahrenheit(c)
                print(f"{c:.2f}°C = {f:.2f}°F")
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == 3:
            print("Goodbye! 🌡️")
            break
        else:
            print("⚠️ Invalid choice. Please select between 1 and 3.")


if __name__ == "__main__":
    main()
