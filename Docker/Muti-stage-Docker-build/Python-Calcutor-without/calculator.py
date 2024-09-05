def calculator():
    print("Hi Naveen , I am a calculator app ....")

    while True:
        # Read input from the user
        text = input("Enter any calculation (Example: 1 + 2 (or) 2 * 5 -> Please maintain spaces as shown in example): ").strip()

        # Check if the user entered "exit" to quit the program
        if text.lower() == "exit":
            break

        # Split the input into parts
        parts = text.split(" ")
        if len(parts) != 3:
            print("Invalid input. Try again.")
            continue

        # Convert operands to integers
        try:
            left = int(parts[0])
            right = int(parts[2])
        except ValueError:
            print("Invalid input. Try again.")
            continue

        # Perform the calculation based on the operator
        operator = parts[1]
        if operator == "+":
            result = left + right
        elif operator == "-":
            result = left - right
        elif operator == "*":
            result = left * right
        elif operator == "/":
            result = left / right
        else:
            print("Invalid operator. Try again.")
            continue

        # Print the result
        print(f"Result: {result}")

# Run the calculator
calculator()
