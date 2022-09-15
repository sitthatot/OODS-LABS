def draw(front,back):
    if back > 0:
        print("_"*(back-1) + "#"*front)
        draw(front+1,back-1)
    elif back < 0:
        print("_"*front + "#"*(back*-1))
        draw(front+1,back+1)

my_number = int(input("Enter Input : "))
if my_number > 0:
   draw(1, my_number)
elif my_number < 0:
    draw(0, my_number)
else:
    print("Not Draw!")
