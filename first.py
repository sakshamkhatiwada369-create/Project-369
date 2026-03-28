# calculator.py
def calculator():
    """Simple command-line calculator."""
    while True:
        try:
            choice = input("Operation (1:+ 2:- 3:* 4:/) or 'q' to quit: ")
            if choice.lower() == 'q': break
            
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1': print(f"Result: {num1 + num2}")
            elif choice == '2': print(f"Result: {num1 - num2}")
            elif choice == '3': print(f"Result: {num1 * num2}")
            elif choice == '4':
                print(f"Result: {num1 / num2}" if num2 != 0 else "Error: Division by zero")
            else: print("Invalid Input")
        except ValueError:
            print("Error: Invalid number format.")

if __name__ == "__main__":
    calculator()
