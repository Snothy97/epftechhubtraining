sum =1
a=1
b=0
num=0

while num <4000000 :
 a=b
 b=sum
 sum = a + b
 if sum % 2 == 0:
  num += sum
print(num)