import re
x = "There are 5 vowels in the english alphabet EIOUA, but they are commonly wrtitten as AEIOU"
y = re.findall('[0-9]+' , x)
z = re.findall('[AEIOU]+' , x)
print(y)
print(z)
