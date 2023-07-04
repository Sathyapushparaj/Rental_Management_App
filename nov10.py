#showing numbers from  -10 to -1 using for loop
for i in range(-10,0):
    print(i)
#excution of for loop
counter=0
while counter<=9:
    counter = counter+2
    print("counter")
else:
    print("done the loop")

#fibonic series
nterm=int(input("how many term:"))
n1,n2=0,1

count=0
if nterm <=0:
    print("enter the possitive integer")
elif nterm ==1:
    print("fibonacci series upto",nterm,":")
    print(n1)
else:
    print("fibonacci series:")
    while count < nterm:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
#calculate cube numbers
n=1
for i in range(1,15):
    n=i*i*i
    print("curent number is:",i," and the cube is:",n)

#ssplit string on hyphens
str="my college life is beautifull"
print(str[0:2])
print(str[2:10])
print(str[11:15])
print(str[16:18])
print(str[18:19])
print(str[19:30])

