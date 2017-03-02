# -*- coding: utf-8 -*-
##5 While loop
condi = 1
while condi<10:
    print(condi),
    condi = condi+1
    
    
while True:
    print('I am True')



##6 For loop
example_list = [1,2,3,4,5,6,13,4,5,6,2]
for i in example_list:
    print i, 'inner of forloop'
print 'outer of forloop'

#print 1-9
for i in range(1,10):
    print i,
#print 0-9
for i in range(10):
    print i,
#print 1,3,5,7,9
for i in range(1,10,2):
    print i,
    
    
    
##7 If 
x,y,z=1,2,3
if x<y:
    print 'x ls th y'
if x<y<z:
    print 'x ls th y'  #also can ==, <=, >, !=
    
    

##8 If else
x,y,z=1,2,3 
if x>y:
    print 'x gt th y'
else:
    print 'x ls or eq to y'
    


##9 If elif else
x,y=2,2
if x>y:
    print 'x gt th y'
elif x<y:
    print 'x ls th y'
else:
    print 'x eq y'
    
    

##1011 Def function
a,b=1,2
def plusss(a,b):
    return a+b
plusss(a,b)

def pls():
    print 'this is'
    dfe = 1+3
    print dfe
pls()

def fun(a,b=3): #b=3 should be behind
    c=a*b
    print 'the c is',c
fun(3)



##1213 global,local variable
X=100 #capital for global var
c=None
def fun():
    a = 10 #local var
    global c #put the local var into global, but above need define c=None
    c = 20
    b = X
    return b+100
print(fun())
print X,a,c

APP=100
a=None
def fun1():
    global a #could put a to global
    a = 20
    return a+100
print APP
print 'a past',a
print fun1()
print 'a now',a



##14 install lib
##15 read write
text = 'My text.\n second line\n third line' #\n next line
print text

#write
my_file = open('C:\\Users\\jncinlee\\Desktop\\gitTUT\\myfile.txt','w') #w write, r read
my_file.write(text)
my_file.close()
#open > write > close

#write more by append
appendtext = '\n more thing'
my_file = open('C:\\Users\\jncinlee\\Desktop\\gitTUT\\myfile.txt','a') #w write, r read
my_file.write(appendtext)
my_file.close()

#read
fil = open('C:\\Users\\jncinlee\\Desktop\\gitTUT\\myfile.txt','r')
content = fil.read() #read all together
print(content)

fil = open('C:\\Users\\jncinlee\\Desktop\\gitTUT\\myfile.txt','r')
cont1 = fil.readline() #read one line
cont2 = fil.readline() #read second line
print(cont1, cont2)

fil = open('C:\\Users\\jncinlee\\Desktop\\gitTUT\\myfile.txt','r')
cont = fil.readlines() #read one line into a list
print(cont)



##18 class
class Calculator: #define a class contain many function
    name = 'good cal'
    price = 19      #extra def name in this class
    #function for this class
    def add(self,x,y): #self default para
        print(self.name) #if want to use the name inside class, use self.name
        result = x+y
        print(result)
    def min(self,x,y):
        result = x-y
        print(result)
    def times(self,x,y):
        print(x*y)
    def div(self,x,y):
        print(x/y)
        
cal = Calculator() #denote cal(individual) as this class(category), as np for numpy class
cal.name #call the name in this Calculator class
cal.price
cal.add(3,4) #call the add() function in Calculator class
Calculator().div(4,2) #could use as well



##19 initial in class
class Calculator: #define a class contain many function
    name = 'good cal'
    price = 19      #given price
    #function for this class
    def __init__(self, name, price, h, weight=56):
        self.name = name
        self.price = price   #price need to input when calling
        self.height = h
        self.w = weight #預設給定值56
        self.add(8,9)
    def add(self,x,y): #self default para
        print(self.name) #if want to use the name inside class, use self.name
        result = x+y
        print(result)
    def min(self,x,y):
        result = x-y
        print(result)
    def times(self,x,y):
        print(x*y)
    def div(self,x,y):
        print(x/y)

c=Calculator('bad',2,3,4) #就算在上面的given已經給過 在叫的時候還是要給一次
c=Calculator('bad',2,3)
c.height #會叫出三
c.h #沒有東西
c.w #叫出4



##20 input
inpu = input('Please give a number:') #return a str
print'This number is',inpu
print('This number is',inpu)

a = int(input('give a odd number:')) #return a str, change into int
if (a%2 ==0):
    print 'correct'
else:
    print 'you idiot'
    
    
    
##21 tuple could also iterate
a_tu = (1,3,4)
b_tu = 1,3,4
a_ls = [1,3,4]

for i in a_tu:
    print i
    
for i in range(len(a_tu)):
    print 'index:',i,'with element:',a_tu[i]  
    


##22 list
a=[1,23,2,5,3,6,4,23]
a.append(5)
print a

a.insert(1,9) #insert 9 in 1 position between 1,23
a.remove(23) #remove 23 at the first place
a[0]
a[-1] #last place
a[:3]
a
a[3:5]
a[-3:] #從後面算起來 倒數三位的東西
a[:-3] #到從後面數起來倒數三位的東西
a.index(23) #值23的所引位置
a[3]
a.count(23)
a.sort();print a
a.sort(reverse=True);print a



##23 multi list
a = [1,2,3,4,5]
md = [[1,2,3],
      [2,3,4],
      [4,5,6]]
print md[0][1],md[2][1]



##24 dic key:value
di = {'apple':1,'orange':3,2:4,4:'b'}
print di[4] #print the value of key 4
print di['orange'] 

del di['orange'] #delete the entry
print di

di[1]=20 #add key 1 with value 20
print di #without order

def qq(x):
    print 'QQ'+ x
dic = {'apple':[4,2],'orange':3,2:{'a':3},4:'b',5:qq} # 字典鐘的字典 字典鐘的function
dic[5]('kiss my ass') #call the func in dic
dic['apple'][1] #call the list in dic
dic[2]['a'] #call the dic value in dic



##25 import
import time
print time.localtime()

import time as t #abbreviate as t
print t.localtime()

from time import time, localtime #only 2 function
print localtime() #could write directly
print time()

from time import * #import all function, could type directly
print time()



##26 build self block, script
#create m1.py contain function 'printdata'
#save it within same wd
import m1 #could only call in within same wd
m1.printdata('good')
#or put m1.py into site-package folder



##27 continue break
a = True
while a:
    b = int(input('type something:'))
    if b==1:
        a = False #這邊false以後 會印下面still在驗證whileloop在跳出到finish
    else:
        pass
    print 'still in whileloop'
print 'finish'
    
while True:
    b = int(input('type something:'))
    if b==1:
        break #停止whileloop 值接到底finish
    else:
        pass
    print 'still in whileloop'
print 'finish'

while True:
    b = int(input('type something:'))
    if b==1:
        continue #忽略下面語句回到while去
    else:
        pass
    print 'still in whileloop'
print 'finish'



##28 try
#for try and error
try:
    file = open('eee','r+')
except Exception as e: #這邊是上面不能直行 改存取錯誤
    print e

try:
    file = open('eee','r+') #要是讀加寫
except Exception as e:
    print 'no such a eee file'
    resp = raw_input('do you want create new file?') 
    ####something wrong here in py2.7 use raw_input() instead of input()
    if resp == 'y':
        file = open('eee','w')
    else:
        pass #到此處例錯誤訊息方法
else: #沒有走到except那邊 表示沒有錯誤
    file.write('write something in eee')
    file.close()
    
    

##29 zip lambda map
#zip: combine more list together for iterate
a=[1,2,3]
b=[4,5,6]
c = zip(a,b) 
print c  

for i,j in zip(a,b): #in c 也可以
    print i,j

list(zip(a,a,b)) #multiple zip

#lambda: write function in one line
def fun1(x,y):
    return x+y

fun2 = lambda x,y: x+y
fun1(2,3)
fun2(2,3)

#map: function plus para
map(fun1,[1],[2]) #值接輸出會是object
list(map(fun1,[1],[2]))

list(map(fun1,[1,3],[2,5])) #多重輸入1+2, 3+5 各自加自己的



##30 copy deepcopy
import copy
a = [1,2,3]
b = a #所引一樣 不同變量
id(b)
id(a) #id same, if change b, also change a
b[0] = 11
a
a[1] = 22
b

#斷開鎖鍊
c = copy.copy(a)
id(c) #id different from a
c[1] = 294
print a, c

#但不完全斷開list in list copy.copy() no use
a = [1,2,[3,4]] #but this
d = copy.copy(a) 
#就算用copy還是只有最外層 裡面那層的id還是一樣 被凍到還是會一起動
id(a) == id(d) #False
id(a[2]) == id(d[2]) #True

a[0] = 111
print a, d

a[2][0] = 333 #change the inner list, change all together
print a, d
        
#完全斷開鎖鍊
a = [1,2,[3,4]] #but this
d = copy.deepcopy(a) 
        
a[2][0] = 333 #change the inner list, change only a now
print a, d



##31 threading
#匹量處理
#一次處例全部 或試分五部分 每個一個threading
#optimize calculation

##32 multiprocess
#多核處理
#most python use 1 core
#threading still in one core

##33 tkinter
#GUI graph user interface
#function application, welcome window...etc, lead user to his window
#ex calculator interface



##34 pickle
#keep result, machine etc..
import pickle
dic = {'da':11,2:[23,4],'23':{1:2,'d':'std'}}

#open>dump>close
file = open('pk_example.pickle','wb') #open for writing
pickle.dump(dic,file) #dump the file
file.close() #close

#add more to existing file
file = open('pk_example.pickle','rb')
dic1 = pickle.load(file)
file.close()
print dic1

#add2 without closing it, in case forget
with open('pk_example.pickle','rb') as file:
    dic1 = pickle.load(file)
print dic1



##35 set diff
cha = ['a','a','b','b','b','c']
print(set(cha)) #set no order

sentence = 'Welcome world!'
print set(sentence) #tear apart the string, keep capital, space

print set([cha,sentence]) #not work, only list or string

cha_set = set(cha)
cha_set.add('x') #add element 'x' to a set
cha_set.add('a') #make no diff, already exist, not ['a','x']
cha_set.clear() #empty the set
cha_set.remove('x') #remove the element 'x'
cha_set.discard('y') #discard 'y', even 'y' not exist
print cha_set

set1 = cha_set
set2 = set(['a','b','o'])
print set2.difference(set1) #find different
print set2.intersection(set1) #find same
