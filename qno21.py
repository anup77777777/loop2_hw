start = int(input("Enter the start of the range "))
end = int(input("Enter the end of the range "))
odd = 0
for num in range(start, end + 1):
    if num % 2 != 0:  
        odd += num
print(f" {start} and {end} is: {odd}")