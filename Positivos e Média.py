count=0
sum=0.0
for i in range(1,7):
    n = float(input())
    if(n>0):
        sum = sum + n
        count=count+1
average = sum/count
print(f"{count} valores positivos")
print(f"{average:0.1f}")


pos=0
med=0.00
for i in range(6):
    x=float(input())
    if x>0:
        pos+=1
        med+=x
print(f"{pos} valores positivos")
print("%.1f"%(med/pos))