def draw(front,back):
    if back > 0:
        print("_"*(back-1) + "#"*front)
        draw(front+1,back-1)
    if back < 0:
        print("_"*front + "#"*(back*-1))
        draw(front+1,back+1)

num = int(input("Enter Input : "))
if num > 0:
    draw(1,num)
elif num < 0:
    draw(0, num)
else:
    print("Not Draw!")
