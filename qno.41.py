number = int(input("Enter a number: "))
num_digits = len(str(number))
number_str = str(number)
sum_of_digits = 0
for digit in number_str:
    sum_of_digits += int(digit) ** num_digits
if sum_of_digits == number:
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number.")
