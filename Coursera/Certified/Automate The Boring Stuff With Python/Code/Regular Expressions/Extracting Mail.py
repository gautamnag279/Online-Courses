import re
x = "From gautamnag@gmail.com to shrutinag@gmail.com"
y = re.findall('\S+@\S+' , x)
print(y)
