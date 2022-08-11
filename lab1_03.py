print(" *** Summation of each digit ***")
number = input("Enter a positive number : ")
saperator = [int(d) for d in str(number)]
collect = 0
for item in saperator:
    collect += item
print(f"Summation of each digit =  {collect}")


