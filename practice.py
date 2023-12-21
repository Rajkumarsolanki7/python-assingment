num=kayak
t1=num
rev=0
while t1>0:
    digit=t1%10
    rev=rev*10+digit
    t1//=10
if rev==num:
    print("pallindrome")
else:
    print("Not a pallindrome")
