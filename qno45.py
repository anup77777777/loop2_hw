number = int(input("Enter a number: "))
prime = True
if number <= 1:
    prime = False
else:
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            prime = False
            break
if prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
