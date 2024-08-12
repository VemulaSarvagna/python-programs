n=int(input("enter a number:"))
count=0
for i in range(2,n):
    if(n%i==0):
        count+=1
if(count==0):
    print("It is prime number")
else:
    print("It is not prime number")
