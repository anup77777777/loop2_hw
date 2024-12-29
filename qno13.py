lst = [1, 2, 3, "d", 4, 5, "a"]
integers = [element for element in lst 
            if type(element) == int]
strings = [element for element in lst 
           if type(element) == str]
print("Integers:", integers)
print("Strings:", strings)
