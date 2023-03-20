import re

message = 'Call me at 9845533978 or at 9788654779'
phone= re.compile(r'\d\d\d\d\d\d\d\d\d\d\d')
out = re.findall(message)
print(out)
