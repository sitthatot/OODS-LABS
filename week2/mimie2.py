def odd_even(type,data,mode):
    if type == 'S':
        if mode == 'Odd':
            for x in range(len(data)):
                if x % 2 == 0:
                    print(data[x],end='')
        elif mode == 'Even':
            for i in range(len(data)):
                if i % 2 == 1:
                    print(data[i],end='')
    elif type == 'L':
        list = []
        for i in data:

            if i == ' ':
                pass
            else:

                list.append(i)
                print(list,end='')


print(" Odd Even ")
check = input("Enter Input : ").split(',')
odd_even(check[0],check[1],check[2])