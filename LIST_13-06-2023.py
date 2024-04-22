#1)print index number and element in the list
'''
li=["ant","money","nest","ball",22,35]
id_num=-1
for i in li:
    id_num+=1
    print(i," ",id_num)
    '''
#2)print even indexed element in list
'''
li=["ant","money","nest","ball",22,35]
print(li[::2])
'''
#4)print only extension in listli = ['gmail.com','yahoo.in','google.com']o/p expected com in com
'''
listli = ['gmail.com','yahoo.in','google.com']
for i in listli:
    b=i.split(".")
    print(b[1],end=" ")
'''
#5)find the largest number in the list
'''
li=[10,23,33,66,99,1,3]
print(max(li))
'''
#6)print chara) length char should be > 2
'''
li=["is","num",33,"int","a","mouse",969,"manga"]
for i in li:
    if len(str(i)) >2:
        print(i)
'''
#b) first and last charcter should be sameli = ['axa','amma','xyz','1221']op = 'axa' 'amma','1221'
'''
li = ['axa','amma','xyz','1221']
for i in li:
    a=i[0]
    b=i[-1]
    if a==b:
        print(i,end=",")
        '''
#8)Remove duplicate element available in list
'''
li=[8,1,8,5,9,1,0,5,6,3,4,9,3,8,2,3,6,3,1,12]
new_li=[]
for i in li:
    if i not in new_li:
        new_li.append(i)
print(new_li)
'''
    
        
#10)Print list in reverse order
'''
li=["ant","money","nest","ball",22,35]
new_li=[]
for i in range(len(li)):
    new_li.append(li.pop())
print(new_li)
'''

