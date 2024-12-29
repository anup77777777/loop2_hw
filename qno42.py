a = "hello how are you"
vowels = "aeiou"
result = ""
for i in a:
    if i not in vowels: 
        result +=i
print(result)