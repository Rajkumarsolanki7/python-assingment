num = 153
digit = 0
t1 = num
while t1>0:
    t1//=10
    digit+=1

t2 = num
armstrong_sum = 0
while t2>0:
    rem = t2%10
    armstrong_sum+=rem**digit
    t2//=10
if armstrong_sum==num:
    print("it is a armstrong")
else:
    print("it is not a armstrong")