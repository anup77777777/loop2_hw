multiples = 0
for num in range(3, 99):
    if num % 3 == 0 or num % 5 == 0:
        multiples += num
print("The sum of all multiples of 3 or 5 below 99 is", multiples)
