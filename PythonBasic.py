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
    
    
    
#7 If 
x,y,z=1,2,3
if x<y:
    print 'x ls th y'
if x<y<z:
    print 'x ls th y'  #also can ==, <=, >, !=
    
    

#8 If else
x,y,z=1,2,3 
if x>y:
    print 'x gt th y'
else:
    print 'x ls or eq to y'
    


#9 If elif else
x,y=2,2
if x>y:
    print 'x gt th y'
elif x<y:
    print 'x ls th y'
else:
    print 'x eq y'
    
    

#10 Def function
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



#12 global,local variable
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



#13
