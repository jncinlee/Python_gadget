##3 Matplotlib plot
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)
y = 2*x+1
y = x**2
plt.plot(x,y)
plt.show()



##4 figure
#show in other window
x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

plt.figure() #in first fig
plt.plot(x,y1)

plt.figure(num=3, figsize=(8,5)) #in third fig
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=10,linestyle='--')

plt.show()



##5 axis, more than one plot in one figure
x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

plt.figure(num=3, figsize=(8,5)) #in third fig
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.,linestyle='--')

plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('x')
plt.ylabel('y haha')

newticks=np.linspace(-1,2,5)
plt.xticks(newticks)

plt.yticks([-2,-1.8,-1,1.2,3],
        [r'$really\ bad$',r'$bad$',r'$normal$',r'$good \alpha$',r'$very good$'])

plt.show()



##6 axis, position
x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

plt.figure(num=3, figsize=(8,5)) #in third fig
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.,linestyle='--')

plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('x')
plt.ylabel('y haha')

newticks=np.linspace(-1,2,5)
plt.xticks(newticks)
plt.yticks([-2,-1.8,-1,1.2,3],
        [r'$really\ bad$',r'$bad$',r'$normal$',r'$good \alpha$',r'$very good$'])

#gca = get current axis
ax = plt.gca()
ax.spines['right'].set_color('none') #right disappear
ax.spines['top'].set_color('none') #top disappear
ax.xaxis.set_ticks_position('bottom') #tick below axis
ax.yaxis.set_ticks_position('left') #tick left of axis
ax.spines['bottom'].set_position(('data',0)) #set bottom axis at -1
ax.spines['left'].set_position(('data',0.1)) #set left axis at 0
#'data' could change to 'outward' or 'axes' on proportion

plt.show()


##7 legend
x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

plt.figure(num=3, figsize=(8,5)) #in third fig
plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('x')
plt.ylabel('y haha')

newticks=np.linspace(-1,2,5)
plt.xticks(newticks)
plt.yticks([-2,-1.8,-1,1.2,3],
        [r'$really\ bad$',r'$bad$',r'$normal$',r'$good \alpha$',r'$very good$'])

l1,=plt.plot(x,y2,label='up')
l2,=plt.plot(x,y1,color='red',linewidth=1.,linestyle='--',label='down')

#legend
plt.legend(handles=[l1,l2],labels=['aa','bb'],loc='best') #lower right
#when use handles, need l1, in objective
#can show only one as well
#plt.legend(handles=[l1,],labels=['aa',],loc='best') #lower right

plt.show()



##8 annotation
x = np.linspace(-3,3,50)
y = 2*x+1

plt.figure(num=3, figsize=(8,5)) #in third fig
plt.scatter(x,y)

#gca = get current axis
ax = plt.gca()
ax.spines['right'].set_color('none') #right disappear
ax.spines['top'].set_color('none') #top disappear
ax.xaxis.set_ticks_position('bottom') #tick below axis
ax.yaxis.set_ticks_position('left') #tick left of axis
ax.spines['bottom'].set_position(('data',0)) #set bottom axis at -1
ax.spines['left'].set_position(('data',0.1)) #set left axis at 0
#'data' could change to 'outward' or 'axes' on proportion

x0=1
y0=2*x0+1
plt.scatter(x0,y0,s=50,color='b')
plt.plot([x0,x0],[y0,0],'k--',lw=2.5)

#m1
plt.annotate(r'$2x+1=%s$' %y0, xy=(x0,y0),
               xycoords='data',xytext=(+30,-30),
               textcoords='offset points',
               fontsize=16,
               arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))
#m2
plt.text(-3.7,3,r'$This\ is\ text. \mu\ \sigma_i \alpha_t$',
        fontdict={'size':16,'color':'r'})
plt.show()



##9 tick 
x = np.linspace(-3,3,50)
y = 0.1*x
plt.figure(figsize=(8,5)) #in third fig
plt.plot(x,y,lw=10)
plt.ylim(-2,2)

#gca = get current axis
ax = plt.gca()
ax.spines['right'].set_color('none') #right disappear
ax.spines['top'].set_color('none') #top disappear
ax.xaxis.set_ticks_position('bottom') #tick below axis
ax.yaxis.set_ticks_position('left') #tick left of axis
ax.spines['bottom'].set_position(('data',0)) #set bottom axis at -1
ax.spines['left'].set_position(('data',0.1)) #set left axis at 0

#take label out, set individually
for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white',edgecolor='None',alpha=0.7)) #alpha transparent 0.7 not see tru

plt.show()



##10 scatterplot
n=1024
x=np.random.uniform(0,1,n)
y=np.random.uniform(0,1,n)
T=np.arctan2(y,x) #for color

plt.scatter(x,y,c=T,s=75,alpha=.5)
#plt.scatter(np.arange(5),np.arange(5))
plt.xlim(0,1)
plt.ylim(0,1)
plt.xticks()
plt.yticks() #set blank for ticks
plt.show()



##11 bar
n=12
X=np.arange(n)
y1=(1-X/float(n))*np.random.uniform(0.5,1.,n)
y2=(1-X/float(n))*np.random.uniform(0.5,1.,n)

plt.bar(X,+y1,facecolor='#9999ff',edgecolor='white')
plt.bar(X,-y2,facecolor='#ff9999',edgecolor='white')

for x,y in zip(X,y1):
    plt.text(x+0.4,y+0.05,'%.2f'%y,ha='center',va='bottom') #ha,va horizon vertical align

#X=np.arange(n) 
for x,y in zip(X,y2):
    plt.text(x+0.4,-y-0.05,'%.2f'%y,ha='center',va='top') 
    
plt.xlim(-.5,n)
plt.ylim(-1.25,1.25)
plt.xticks()
plt.yticks() #set blank for ticks
plt.show()



##11 contour
def f(x,y):
    return(1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
    
n=256
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)
X,Y=np.meshgrid(x,y) #mesh in a grid

#fill color
plt.contourf(X,Y,f(X,Y),10,alpha=0.75,cmap=plt.cm.hot) 
#fill contour,cmap= cm.hot corresponding color in map plt.cm.cool

#drwa contour line
C = plt.contour(X,Y,f(X,Y),10,colors='k',lw=.5)
#8 divide as 8 section

#contour label
plt.clabel(C,inline=1,fontsize=10)
#inline=0 cut thru

plt.xticks()
plt.yticks() #set blank for ticks
plt.show()



##13 image
a=np.random.uniform(0,1,9).reshape(3,3)
print(a)

plt.imshow(a,interpolation='nearest',cmap='bone',origin='upper')
#upper=small value black, lower=small value white
#interporation='nearest', 'none'
plt.colorbar(shrink=0.9) #shrink 90%

plt.xticks()
plt.yticks()
plt.show()



##14 3d
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

#x,y
X,Y= np.arange(-4,4,0.25),np.arange(-4,4,0.25)
X,Y= meshgrid(X,Y)
#z
R=np.sqrt(X**2+Y**2)
Z=np.sin(R)

ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))
#rstride=5 loss cross

ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')
#zdir from direction compression on surface, offset=to which z=-2
ax.set_zlim(-2,2)

plt.show()



##15 subplot tradition
#2x2
plt.figure()

plt.subplot(2,2,1) #divide 2 low 2 col
plt.plot([0,1],[0,1])

plt.subplot(2,2,2) #divide 2 low 2 col
plt.plot([0,1],[0,2])

plt.subplot(2,2,3) #divide 2 low 2 col
plt.plot([0,1],[0,3])

plt.subplot(224) #divide 2 low 2 col
plt.plot([0,1],[0,4])

plt.show()

#upper larger
plt.figure()

plt.subplot(2,1,1) #divide 2 low 2 col
plt.plot([0,1],[0,1])

plt.subplot(2,3,4) #divide 2 low 2 col
plt.plot([0,1],[0,2])

plt.subplot(2,3,5) #divide 2 low 2 col
plt.plot([0,1],[0,3])

plt.subplot(236) #divide 2 low 2 col
plt.plot([0,1],[0,4])

plt.show()



##16 subplot m1m2m3
#m1 subplot2grid
plt.figure()
ax1=plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1) #col span 3 unit
ax1.plot([1,2],[1,2])
ax1.set_xticks(())
ax1.set_title('ax1')

ax2=plt.subplot2grid((3,3),(1,0),colspan=2,rowspan=1) 
ax3=plt.subplot2grid((3,3),(1,2),rowspan=2) 
ax4=plt.subplot2grid((3,3),(2,0)) 
ax5=plt.subplot2grid((3,3),(2,1)) 

#m2 gridspec
import matplotlib.gridspec as gridspec
plt.figure()
gs=gridspec.GridSpec(3,3)
ax1 = plt.subplot(gs[0,:]) #0row,all col
ax2 = plt.subplot(gs[1,:2]) #1row, till 2col
ax3 = plt.subplot(gs[1:,2]) #from 1 row, 2col
ax4 = plt.subplot(gs[-1,0]) #last row, 0col
ax5 = plt.subplot(gs[-1,-2])

#m3 def substruc
f,((ax11,ax12),(ax21,ax22))=plt.subplots(2,2,sharex=True,sharey=True)
ax11.scatter([1,2],[1,2])
ax11.set_title('haha')

f.main('a')
plt.tight_layout()
plt.show()



##17 plot in a plot
fig =plt.figure()
x=np.arange(7)
y=[1,2,3,2,5,8,5]
left,bottom,width,height=.1,.1,.8,.8
ax1=fig.add_axes([left,bottom,width,height]) #arg percentage to overall
ax1.plot(x,y,'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('tt')

left,bottom,width,height=.2,.6,.25,.25
ax2=fig.add_axes([left,bottom,width,height]) 
#arg percentage to overall
ax2.plot(x,y,'b')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('s1')

plt.axes([.6,.2,.25,.25]) #below all follow the ax3
plt.plot(y[::-1],x,'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('s2')



##18 secondary axis
x=np.arange(0,10,0.1)
y1=0.05*x**2
y2=-1*y1

fig,ax1=plt.subplots() #set a x1, y1
ax2 = ax1.twinx() #same as x1 but mirror to y1 as y2
ax1.plot(x,y1,'g-')
ax2.plot(x,y2,'b--')
ax1.set_xlabel('x')
ax1.set_ylabel('y1',color='g')
ax2.set_ylabel('y2',color='b')



#19 animate plot
from matplotlib import animation
fig,ax=plt.subplots()

x=np.arange(0,2*np.pi,0.01)
line, =ax.plot(x,np.sin(x)) #choose only first position

def animate(i):
    line.set_ydata(np.sin(x+i/10))
    return line,

def init():
    line.set_ydata(np.sin(x))
    return line,
    
ani = animation.FuncAnimation(fig=fig,func=animate, 
            frames=100,init_func=init,interval=20,blit=True) 
#varyu with time, frame=100 grid repeat, 20s interval, blit=change all plot
plt.show()
