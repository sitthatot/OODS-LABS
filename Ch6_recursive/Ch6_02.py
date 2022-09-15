def length(txt):
    if txt == '':
        print("")
        return 0
    elif txt[1:] == '':
        print(txt[0]+'*')
        return 1
    print(txt[0]+"*"+txt[1]+"~",end='')
    return 2 + length(txt[2:])

user_enter = input("Enter Input : ")
print(str(length(user_enter)))