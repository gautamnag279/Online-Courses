counts = dict()
names = {'john' , 'allen' , 'ruby' , 'samantha'}

for i in names:
    if i not in counts:
        counts[i] = counts.get(i,0) + 1
print(counts)

