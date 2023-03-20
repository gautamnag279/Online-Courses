import re

message = 'Batman may have been a cool superhero, but Batwoman was cOOler'

bat = re.compile(r'Bat(wo)?man')

output = bat.search(message)

print(output.group())
