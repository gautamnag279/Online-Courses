num = int(input("Enter a number:"))
if num > 1:
    for i in range(2,num//2):
        if (num % i) == 0:
            print(num , "is not a Prime Number")
            break
        else:
            print(num , "is a Prime Number")
            break
