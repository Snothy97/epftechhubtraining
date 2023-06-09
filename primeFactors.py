def largest_prime_factor(n):
    # Initialize factor to 2, the smallest prime number
    i = 2

    while i * i <= n:
        #check if the square root of i does not exceed the nth term
        if n % i == 0:
            # If n is divisible by the factor, divide it by the factor
            n //= i
        else:
            # If n is not divisible by the factor, increment the factors
            i += 1

    # At this point, n is either a prime factor or the remaining prime number
    return n

largest_factor = largest_prime_factor(600851475143)
print(largest_factor)         
