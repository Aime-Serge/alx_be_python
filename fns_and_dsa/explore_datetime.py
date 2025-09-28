from datetime import datetime, timedelta


def display_current_datetime():
    """Displays the current date and time in YYYY-MM-DD HH:MM:SS format."""
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date


def calculate_future_date(days: int):
    """
    Calculates and displays the date after a given number of days.

    Args:
        days (int): Number of days to add
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date


def main():
    current_date = display_current_datetime()
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("⚠️ Please enter a valid integer.")


if __name__ == "__main__":
    main()
