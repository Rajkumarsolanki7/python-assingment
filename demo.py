# # num=143
# # digit=0
# # t1=num
# # while t1>0:
# #     t1//=10
# #     digit=digit+1

# # t2=num
# # sum=0
# # while t2>0:
# #     rem=t2%10
# #     multiply=1
# #     for i in range(1,digit+1):
# #         multiply=multiply*rem

# #     sum=multiply+sum
# #     t2//=10
# # if sum==num:
# #     print("Its aarmstrong ")
# # else:
# #     print("Not armstrong")

# num=1331
# t1=num
# rev=0
# while t1>0:
#     digit=t1%10
#     rev=rev*10+digit
#     t1//=10
# if rev==num:
#     print("pallindrome")
# else:
#     print("Not a pallindrome")

x="kayam"

i=0
j=len(x)-1
check=True

while i<j:
    if x[i]!=x[j]:
        check=False
    i+=1
    j-=1
if check==True:
    print("It is pallindome")
else:
    print("It's Not a Pallindrome")