import re
x = "From: And install to : directory"
y = re.findall('^F.+?:' , x)
print(y)
