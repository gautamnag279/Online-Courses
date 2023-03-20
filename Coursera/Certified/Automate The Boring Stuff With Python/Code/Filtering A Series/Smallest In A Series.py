smallest = None
num_set = [5,56,77,33,8,5,3,88,4,32,6,4,7]
for i in num_set:
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest = i
print("The smallest number in the series is:" , smallest)
