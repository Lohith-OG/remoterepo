# Simple Python Program to Greet User and Calculate Age

def main():
    # Get user input for name and age
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    # Calculate the year when the user will turn 100
    current_year = 2025  # You can use datetime module for dynamic current year
    year_turn_100 = current_year + (100 - age)

    # Greet the user
    print(f"\nHello, {name}! You are currently {age} years old.")
    print(f"You will turn 100 years old in the year {year_turn_100}.")

if __name__ == "__main__":
    main()

def(a,b)