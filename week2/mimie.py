# num = input("Enter All Bid : ").split()
# if len(num) <= 1:
#     print("not enough bidder")
# else:
#     num_to_int = []
#     for item in num:
#         num_to_int.append(int(item))
#     num_to_int.sort()
#     print(num_to_int)
#     print(f"winner bid is {num_to_int[-1]} need to pay {num_to_int[-2]}")
def odd_list(nums):
    new_odd = []
    for item in nums:
        if(item % 2 != 0):
            new_odd.append(item)
    return new_odd

def even_list(nums):
    new_odd = []
    for item in nums:
        if(item % 2 == 0):
            new_odd.append(item)
    return new_odd

nums = []
for number in range(0,8):
    nums.append(number)

print(odd_list(nums))
print(even_list(nums))