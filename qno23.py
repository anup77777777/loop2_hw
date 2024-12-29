string = input("Enter a string: ")
count = 0
for char in string:
    if char == ' ': 
        count += 1
print(f"The number of spaces in the given string is{count}")