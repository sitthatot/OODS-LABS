print("*** Converting hh.mm.ss to seconds ***")
h,m,s = input("Enter hh mm ss : ").split()
h,m,s = int(h),int(m),int(s)
if m >= 60 or m < 0:
    print(f"mm({m}) is invalid!")
elif s >= 60 or s < 0:
    print(f"mm({s}) is invalid!")
else:
    timeToSec = (h*60*60)+(m*60)+s
    print(f"{h:02}:{m:02}:{s:02} = {timeToSec:,} seconds")
