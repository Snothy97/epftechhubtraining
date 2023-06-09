def sum_of_multiples(limit):
  
    sum = 0  # Initialize the sum variable to 0
    
    for num in range(1, limit):  # Iterate through numbers from 1 to limit-1
      
        if num % 3 == 0 or num % 5 == 0:  # Check if the number is divisible by 3 or 5
            sum += num  # Add the number to the sum
            
    return sum  # Return the final sum

limit=1000
result = sum_of_multiples(limit)  # Call the sum_of_multiples function with limit as the argument
print(result)  # Print the result
         