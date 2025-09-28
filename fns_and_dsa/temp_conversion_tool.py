# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FREEZING_POINT_F = 32


def convert_to_celsius(fahrenheit: float) -> float:
    """Converts Fahrenheit to Celsius using the global factor."""
    return (fahrenheit - FREEZING_POINT_F) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius: float) -> float:
    """Converts Celsius to Fahrenheit using the global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_F


def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            result = convert_to_celsius(temp)
            print(f"{temp}°F is {result}°C")
        elif unit == "C":
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {result}°F")
        else:
            raise ValueError("Invalid unit entered. Use 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(f"⚠️ Invalid input: {e}")


if __name__ == "__main__":
    main()
# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FREEZING_POINT_F = 32


def convert_to_celsius(fahrenheit: float) -> float:
    """Converts Fahrenheit to Celsius using the global factor."""
    return (fahrenheit - FREEZING_POINT_F) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius: float) -> float:
    """Converts Celsius to Fahrenheit using the global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_F


def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            result = convert_to_celsius(temp)
            print(f"{temp}°F is {result}°C")
        elif unit == "C":
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {result}°F")
        else:
            raise ValueError("Invalid unit entered. Use 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(f"⚠️ Invalid input: {e}")


if __name__ == "__main__":
    main()
