def Rshift(num,shift):
    shift = num >> shift
    return shift

n,s = input("Enter number and shiftcount : ").split()
print(Rshift(int(n),int(s)))
