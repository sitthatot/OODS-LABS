# def sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum(n-1)
#
# print(sum(3))
#1 What's the simplest possible input?
#2 Play around with examples and visualize!
#3 Relate hard case to simpler cases
#4 Generalize the pattern
#5Write code by combining recursive pattern with the base case

def reverse(inp):
    if inp == "":
        return ""
    return reverse(inp[1:]) + inp[0]

print(reverse("hello"))