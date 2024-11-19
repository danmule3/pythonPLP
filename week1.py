# Basic Calculator Program  

# Function to perform the calculation  
def calculate(num1, num2, operator):  
    if operator == '+':  
        return num1 + num2  
    elif operator == '-':  
        return num1 - num2  
    elif operator == '*':  
        return num1 * num2  
    elif operator == '/':  
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Cannot divide by 0" 
    else:  
        return "Error: Invalid operator."  

# Main program  
def main():  
    try:  
        # User input  
        num1 = float(input("Enter the first number: "))  
        num2 = float(input("Enter the second number: "))  
        operator = input("Enter an operator (+, -, *, /): ")  

        # Calculate and print the result  
        result = calculate(num1, num2, operator)  
        print(f"{num1} {operator} {num2} = {result}")  

    except ValueError:  
        print("Invalid input. Please enter numeric values.")  

# Run the program  
if __name__ == "__main__":  
    main()