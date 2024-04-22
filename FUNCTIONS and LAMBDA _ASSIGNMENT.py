# 1)Write a function that accepts two strings and returns True if the two strings are anagrams of each other.
'''
def anna (st,st2):
    a=sorted(st.lower())
    b=sorted(st2.lower())
    if len(a)==len(b):
        if a==b:
            return True
    else:
        return False
        
            
st=input("enter first string: ")
st2=input("enter second string: ")

result=anna(st,st2)
print(result)
'''
#3)Write a method that returns the last digit of an integer. For example, the call
# of get_last_digit(3572) should return
'''
def digi (num):
        a=num%10
        return a
num=int(input())
print(digi(num))

'''
#6) li =[1,2,3,4,5,6] write a function to group even and odd numbers in a list
'''
def group(l):
    for i in range(2):
        nl.append([])
    for j in (l):
        if j%2==0:
            nl[0].append(j)
        else:
            nl[1].append(j)
    print(nl)

l=[1,2,3,4,5,6]
nl=[]
group(l)
'''
#8)Write a function which returns the sum of lengths of all the iterables
#total_length([1, 2, 3], (4, 5))
#output = 5
'''
def total_length(s):
    total=0
    a=list(s)
    for i in range(len(a)):
        total+=int(len(a[i]))
    print(total)
        
s=([1, 2, 3], (4, 5))
total_length(s)
'''
#9)Write a program to print all the number which are ending with 5
'''
def ending(numbers):
    for i in numbers:
        if int(i)%5==0:
            print(i,end=" ")
numbers = ['1', '12', '123', '12345', '125', '905', '55', '5', '95655', '55555']
ending(numbers)
'''




########################lambda##################################

#1)WAP to return a string only if string starting with vowel
'''
def vowel(li):
    if li [0]in "AEIOUaeiou":
        return li
li = ['apple','gmail','yahoo','instagram','facebook']

res=filter(vowel,li)
print(list(res))
'''
#2)WAP to convert all the negative number in the list to positive number
'''
l=[-1,-2,-3,-4,-5]

def negative (i):
    if i<0:
        return i*-1
    else:
        return i
result=map(negative,l)
print(list(result))

'''
#5)we have a list of fruits, and your task is to output only those 
#names which have the character “g” in their name.
'''
fruits = ['mango', 'apple', 'orange', 'cherry', 'grapes']
def ch(fruits):
    if 'g' in fruits:
        return fruits
res=filter(ch,fruits)
print(list(res))
'''























                           
            
