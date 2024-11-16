def calculate_discount(price, discount_percent):  
    if discount_percent >= 20:  # Check if the discount is 20% or higher  
        discount_amount = (discount_percent / 100) * price  # Calculate the discount amount  
        final_price = price - discount_amount  # Subtract the discount from the original price  
        return final_price  
    else:  
        return price  # Return original price if discount is less than 20%  

# Prompting user for input  
original_price = float(input("Enter the original price of the item: "))  
discount_percentage = float(input("Enter the discount percentage: "))  

# Calculating the final price  
final_price = calculate_discount(original_price, discount_percentage)  

# Printing the result  
if final_price == original_price:  
    print(f"The original price of the item is: ${final_price:.2f}")  
else:  
    print(f"The final price after applying the discount is: ${final_price:.2f}")