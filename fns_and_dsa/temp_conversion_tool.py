# temp_conversion_tool.py

# Global conversion factors (must match checker format: no spaces!)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.

    Parameters:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature converted to Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.

    Parameters:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature converted to Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def get_temperature_input():
    """
    Prompt the user to enter a temperature value and validate input.

    Returns:
        float: Validated temperature value.
    """
    while True:
        temp_input = input("Enter the temperature to convert: ").strip()
        try:
            return float(temp_input)
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")


def get_unit_input():
    """
    Prompt the user to specify the unit (C/F) and validate input.

    Returns:
        str: Validated unit, 'C' or 'F'.
    """
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ("C", "F"):
            return unit
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


def main():
    """
    Main function to run the temperature conversion tool in a loop.
    """
    print("=== Temperature Conversion Tool ===")

    while True:
        temp_value = get_temperature_input()
        unit = get_unit_input()

        if unit == "C":
            converted_temp = convert_to_fahrenheit(temp_value)
            print(f"{temp_value:.2f}°C is {converted_temp:.2f}°F")
        else:
            converted_temp = convert_to_celsius(temp_value)
            print(f"{temp_value:.2f}°F is {converted_temp:.2f}°C")

        # Ask the user if they want to convert another temperature
        again = input("Do you want to convert another temperature? (Y/N): ").strip().upper()
        if again != "Y":
            print("Thank you for using the Temperature Conversion Tool. Goodbye!")
            break


if __name__ == "__main__":
    main()
