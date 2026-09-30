while True:
    print("\n===== CALCULATOR & UNIT CONVERTER =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Kilometers to Miles")
    print("6. Celsius to Fahrenheit")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == "7":
        print("Thank you! Goodbye!")
        break
    elif choice in ["1", "2", "3", "4"]:
        while True:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                break
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        if choice == "1":
            print("Result:", a + b)
        elif choice == "2":
            print("Result:", a - b)
        elif choice == "3":
            print("Result:", a * b)
        elif choice == "4":
            if b == 0:
                print("Cannot divide by zero!")
            else:
                print("Result:", a / b)
    elif choice == "5":
        while True:
            try:
                km = float(input("Enter kilometers: "))
                break
            except ValueError:
                print("Invalid input! Please enter a number.")
        miles = km * 0.621371
        print("Miles:", miles)
    elif choice == "6":
        while True:
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                break
            except ValueError:
                print("Invalid input! Please enter a number.")
        fahrenheit = (celsius * 9 / 5) + 32
        print("Fahrenheit:", fahrenheit)
    else:
        print("Invalid choice! Please select 1-7.")
