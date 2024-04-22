#2)create a dictionary with duplicate items and its count pair
'''
names = ["apple", "google", "gmail", "yahoo", "gmail", "apple", "gmail", "google"]
new_names=[]
d={}
for i in names:
  if i not in new_names:
    new_names.append(i)

count=[]
for i in range(len(new_names)):
  c=names.count(new_names[i])
  count.append(c)

for i in range(len(new_names)):
  if i < len(count):
    d[new_names[i]]=count[i]
print(d)
'''
#9)Find sum of all the values in a dictionary 
'''
d= {'a': 100, 'b':200, 'c':300}
sum_values=0
for i in d.values():
  sum_values+=i
print(sum_values)
'''
#6)create a dictionary with duplicate word with count pair 
'''
string = "python is a language python program is easy"
lstr=string.split()
dup=[]
d={}
for i in lstr:
  if lstr.count(i)>1 and i not in dup:
    dup.append(i)

count=[]
for i in range(len(dup)):
  c=lstr.count(dup[i])
  count.append(c)

for i in range(len(dup)):
  if i < len(count):
    d[dup[i]]=count[i]
print(d)
'''
#4)Create a dictionary for the range 10 store n as key square of n as value
'''
n=int(input("enter your range: "))
d={}
for i in range(1,n):
  d[i]=i**2
print(d)
'''
#7) Create a dictionary by using two lists
'''
l1 = ['a','b','c','d']
l2 = [1,2,3,4]
d={}
for i in range(len(l1)):
  if i<len(l2):
    d[l1[i]]=l2[i]
print(d)
'''
#3)Flip key and value pair in a dictionary
'''
d= {'a': 100, 'b':200, 'c':300}
new_d={}
for key,value in d.items():
  new_d[value]=key
print(new_d)
'''  
#1)Reverse the values in the dictionary if the value is of type string 
'''
d = {"a": "hello", "b": 100, "c": 10.2, "d": "world","e":'121'}    
valule_l=[]
new_d={}
Reverse_str=[]

for i in d.values():
  if isinstance(i,str):
    valule_l.append(i)
    Reverse_str.append(i[::-1])
key_l=[]
for i in range(len(valule_l)):
  for key in d:
    if d[key]==valule_l[i]:
      key_l.append(key)

for i in range(len(key_l)):
  if i<len(Reverse_str):
    new_d[key_l[i]]=Reverse_str[i]

    
for keys in d:
  if keys in new_d:
    d[keys]==new_d[keys]
print(d)
'''


























