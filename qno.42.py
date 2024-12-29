number = int(input("Enter a number"))
number_str = str(number)
reversed_str = number_str[::-1]
if number_str == reversed_str:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
