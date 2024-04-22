#1) Remove the element from the set set_ = {"python", "dad", "hai", "malayalam", "madam", "mom"}key = "hai"
'''
set_={"python", "dad", "hai", "malayalam", "madam", "mom"}
set_.remove('hai')
print(set_)
'''
#2)Display non common element from 2 set
'''
set_1 = {"python", "dad", "hai", "malayalam", "madam", "mom"}
set_2 = {"python", "dad", "hello","hai", "malayalam", "madam", "mom","c++"}
print(set_1.symmetric_difference(set_2))
'''
#3)Remove duplicate customer details and display final customer details by considering 2 sets
'''
set1 = {'Rama','Dinga','Seetha','Radha'}
set2 = {'Rama','swapna','Seetha','swathi'}
set1.update(set2)
print(set1)
'''
#4)find common elements in three list using sets
'''
num1 = [1, 5, 10, 20, 40, 80]
num2 = [6, 7, 20, 80, 100]
num3 = [3, 4, 15, 20, 30, 70, 80, 120]
print(set(num1).intersection(set(num2).intersection(set(num3))))
'''
#5)Find minimum and maximum in value in set
'''
set1={3, 4, 15, 20, 30, 70, 80, 120}

print("the maximum value in set is ",max(set1))
print("the minimum value in set is ",min(set1))

or

l=list(set1)
max_num=l[0]
min_num=l[0]
for i in l:
  if i>max_num:
    max_num=i
  elif i<min_num:
    min_num=i
print("the maximum value in set is ",max_num)
print("the minimum value in set is ",min_num)
'''
#6)write a program to print strings in the set
'''
set1={"hi","hello","123",5,6.3,"6.33","social"}
for i in set1:
  if isinstance(i,str):
    print(i)
'''

#8)Output : Missing values in list1 = {8, 7}          
#Additional values in list1 = {1, 2, 3}          
#Missing values in list2 = {1, 2, 3} 
#Additional values in list2 = {7, 8} 
'''
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]
a=set(list1).union(set(list2))
print("Missing values in list1 = ",a.difference(set(list1)))
print("Additional values in list1 = ",a.difference(set(list2)))
b=set(list2).difference(list1)
print("Missing values in list2 = ",b)
c=set(list1).difference(list2)
print("Additional values in list2 = ",c)
'''
