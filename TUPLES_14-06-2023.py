#1)Print sum of elements in tuple
'''
tu=("123",2,6,6.9,"abc","6")
count=0
for i in tu:
  if isinstance(i,(int,float)):
    count=count+i
  elif i.isdigit():
    count=count+int(i)
print(count)
'''
#2)Print elements inside the tuple in reverse order
'''
tu=(5,14,15,18,21,25)
print(tu[::-1])
or 
tu=(5,14,15,18,21,25)
new_tu=[]
a=list(tu)
for i in range(len(a)):
  new_tu.append(a.pop())
print(tuple(new_tu))
'''
#4)tu = (5,14,15,18,21,25) if num devisible by both 3 and 5 print that number
'''
tu=(5,14,15,18,21,25)
for i in tu:
  if i%3==0 and i%5==0:
    print(i,"divisible by both 3 and 5")
'''
#5)Print Highest and lowerst number in tuple
'''
tu = (50, 10, 60, 70, 50)
max_num=tu[0]
min_num=tu[0]
for i in tu:
  if i>max_num:
    max_num=i
  elif i<min_num:
    min_num=i
print("the lowest number in tuple is ",min_num)
print("the heighest number in tuple is ",max_num)
'''
#6)Print even indexed elements in the tuple
'''
tu = (5,14,15,18,21,25)
print(tu[::2])
'''
#7)tuple1 = (50, 10, 60, 70, 50) find number of occurrence of 50
'''
tuple1 = (50, 10, 60, 70, 50)
count=0
for i in tuple1:
  if i==50:
    count+=1
print("the number of occurrence of 50 is ",count)
'''
#8)print if the element is starting with vowel files = ("Amazon", "flipkart", "walmart", "gmail", "yahoo")
'''
files = ("Amazon", "flipkart", "walmart", "gmail", "yahoo")
for i in files:
  if i[0] in "AEIOU" or i[0] in "aeiou":
    print(i)
'''
#9)tu = ("python", "dad", "hai", "malayalam", "madam", "mom") print polindrome in tuple
'''
tu = ("python", "dad", "hai", "malayalam", "madam", "mom")
for i in tu:
  if i==i[::-1]:
    print(i)
'''
#10)Check if all items in the tuple are the sametu = (33,33,33,33)
'''
tu=(33,33,33,33)
i=tu[0]
for j in range(0,len(tu)):
  if i==tu[j]:
    print("yes")
'''
