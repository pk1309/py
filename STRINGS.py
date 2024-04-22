'''
a=input("enter your string ")
b=len(a)

if b%2==0:
    print("given string is symmetrical")
else:
    print("given string is not symmetrical")
'''
'''
a=input()
b=len(a)//2
c=a[:b]
d=a[b:]
print(c+d.upper())
'''
'''
a=input()
print(a.capitalize()[:-1]+a.upper()[-1])
    
'''
'''
capital="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower=capital.lower()
A1=input()
if A1.isupper():
    if A1 in capital:
        a=capital.find(A1)
        print(capital[:a])
elif A1.islower():
    if A1 in lower:
        a=lower.find(A1)
        print(lower[:a])
else:
    print("charater not belong to alphabet")
'''



'''
a= input("enter your sentence ")
b=int(input("enter your string length "))
c=a.split()
for i in c:
    d=len(i)
    if d>b:
       print(i)
       
'''


        
    
    












































