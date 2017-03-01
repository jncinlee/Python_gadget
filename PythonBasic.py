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



##24 dic
di = {}
