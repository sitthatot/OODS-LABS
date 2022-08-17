def odd_list(al):
    new_odd = []
    for item in al:
        if(item % 2 != 0):
            new_odd.append(item)
    return new_odd


print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
# print(ls)
opls = odd_list(ls)
print("Input list : ", ls, "\n"
        "Output list : ", opls)
