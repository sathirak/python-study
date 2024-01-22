def calculate_year_100(age):
    import datetime
    current_year = datetime.datetime.now().year
    year_100 = current_year + (100 - age)
    return year_100

def main():
    # Get user input
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    # Calculate the year the user will turn 100
    year_100 = calculate_year_100(age)

    # Print a personalized message
    print(f"Hello, {name}! You will turn 100 years old in the year {year_100}.")

if __name__ == "__main__":
    main()
