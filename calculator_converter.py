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
    if choice == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a + b)
    elif choice == "2":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a - b)
    elif choice == "3":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a * b)
    elif choice == "4":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if b == 0:
            print("Cannot divide by zero!")
        else:
            print("Result:", a / b)
    elif choice == "5":
        km = float(input("Enter kilometers: "))
        miles = km * 0.621371
        print("Miles:", miles)
    elif choice == "6":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print("Fahrenheit:", fahrenheit)
    elif choice == "7":
        print("Thank you! Goodbye!")
        break
    else:
        print("Invalid choice! Please select 1-7.")
