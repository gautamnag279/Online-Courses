stuff = dict()
names = ['natalie' , 'emma' , 'natalie' , 'jessica' , 'emma' , 'emma']
for name in names:
    if name in stuff:
        stuff[name] = stuff[name] + 1
    else:
        stuff[name] = 1
print(stuff)
