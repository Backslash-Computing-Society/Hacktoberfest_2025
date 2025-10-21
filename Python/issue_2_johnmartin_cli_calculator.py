# issue_2_johnmartin_cli_calculator.py
# Simple CLI Calculator
# This program performs basic arithmetic operations (+, -, *, /) and returns clean results (whole numbers without .0, floats when needed)

# Function to perform Addition
def add(n1, n2):
    return n1 + n2

# Function to perform Subtraction   
def subtract(n1, n2):
    return n1 - n2

# Function to perform Multiplication
def multiply(n1, n2):
    return n1 * n2

# Function to perform Division
def divide(n1, n2):
    if n2 == 0:
        return "Error: Cannot divide by 0."
    return n1 / n2

# Main Function
def calculator():
    print("Simple CLI Calculator")
    print("Operations: Add(+), Subtract(-), Multiply(*), Divide(/)")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter calculation: ")

        if user_input.lower() == "exit":
            print("User Exited.")
            break

        try:
             # Split input into number, operator, number
            parts = user_input.split()

            if len(parts) != 3:
                print("Error: Input should be: number operator number")
                continue
            
            # Convert inputs to float for flexibility
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])

            # Perform chosen operation
            if operator == "+":
                result = add(num1, num2)
            elif operator == "-":
                result = subtract(num1, num2)
            elif operator == "*":
                result = multiply(num1, num2)
            elif operator == "/":
                result = divide(num1, num2)
            else:
                print("Error: Enter +, -, *, or /")
                continue
            
            # Convert float results like 10.0 → 10
            if isinstance(result, (int, float)):
                if result.is_integer():
                    result = int(result)

            print(f"Result: {result}\n")

        except ValueError:
            print("Error: Enter numbers.\n")

if __name__ == "__main__":
    calculator()
