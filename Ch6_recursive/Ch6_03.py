def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
user_enter = input("Enter Input : ").split()
if user_enter[0] == "0" and user_enter[1] == "0":
    print("Error! must be not all zero.")
else:
    user_enter_int = []
    user_enter_int.append(int(user_enter[0]))
    user_enter_int.append(int(user_enter[1]))
    user_enter_int.sort(reverse=True)
    print(f"The gcd of {user_enter_int[0]} and {user_enter_int[1]} is : {gcd(abs(user_enter_int[0]), abs(user_enter_int[1]))}")