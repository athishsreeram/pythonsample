a = int(input("enter no : "))
if (a > 1) :
    for x in range(2,a):
        if ((a%x) == 0):
            print("non prime")
            break
        else:
            print("prime")
            break
else:
    print("non prime")