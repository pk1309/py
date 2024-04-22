#1)add number from 15 to 25
'''
count=0
for i in range (15,25):
    count=count+i
print(count)
'''
#2)Enter 10 numbers count number of even numbers and odd numbers and sum of even and odd number
'''
even=0
odd=0
E_sum=0
O_sum=0

for i in range(10):
    n=int(input( "enter values: "))
    if n%2==0:
        even=even+1
        E_sum=E_sum+n

    else:
        odd=odd+1
        O_sum=O_sum+n
print(even)
print(odd)
print(E_sum)
print(O_sum)
'''
#3)input 5 numbers check its completerly divisible by 5 add those numbers
'''
total=0
for i in range (5):
    n=int(input("enter values "))
    total=total+n
print(total)
if total%5==0:
    print("divisible by 5")
else:
    print("not divisible by 5")
    
    '''

#4)input 5 subjects marks find total,average marks, if marks greater than 35 pass less than 35 fail count how many subjects are passes and how many are failed
'''
total_marks=0
pass_count=0
fail_count=0
for i in range(5):
    n=int(input("enter subject marks "))
    total_marks=total_marks+n
    if n >=35:
        pass_count=pass_count+1
    else :
        fail_count=fail_count+1
Avg=total_marks/5
print("total number of subjects passed ",pass_count)
print("total number of subjects failed ",fail_count)
print("total marks obtained  ",total_marks)
print("average marks are ",Avg)
'''

#5)input 5 numbers, if entered number is in the range of 25 to 75 then add those numbers else count the numbers which are not in range of 25 to 75

'''
c_sum=0
c_sum1=0
for i in range(5):
    n=int(input("enter your number  " ))
    if n >=25 and n<=75:
        c_sum=c_sum+n
    else:
        c_sum1=c_sum1+n
print("sum of numbers in range between 25 and 75 is  ",c_sum)
print("sum of numbers out of range ",c_sum1)

'''

#7)Convert Upper to lower lower to upper case in a string if it is a number or spl character print as it is
'''
a=input()
if a.isupper():
    print(a.lower())
elif a.islower():
    print(a.upper())
else:
    print(a)
    '''

#8)Based on the user input display the multiplication table
'''
number = int(input("enter table number: "))
stop=int(input("define your range: "))

for i in range(1, stop+1):
    result = number * i
    print(result)
'''











































