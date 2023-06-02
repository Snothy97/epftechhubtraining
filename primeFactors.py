"""
Solution 1

num=600851475143
i=2
while i * i< num:
    while num % i==0:
      num = num/i
    i=i+1
print (int(num))
"""
#Solution 2
def largest_prime_factor(n):
    i=2
    while i * i < n:
        while n % i==0:
            n = n/i
        i+=1     
    print(int(n))
largest_prime_factor(600851475143)         
            
    
