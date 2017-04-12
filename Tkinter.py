##GUI interface easy for ppl

#apply on Python3

##2 Label Button
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x100')

var = tk.StringVar()#label show a var
#label
l = tk.Label(window, textvariable = var, bg = 'blue',
             font = ('Arial',12), width=15, height=2)
             #on window, master, 15 width of words
l.pack() #place at up down right left
#l.place() #place at a point

on_hit = False
def hit_me():
    global on_hit
    if on_hit==False:
        on_hit=True
        var.set('you hit me')
    else:
        on_hit=False
        var.set('')

#button
b = tk.Button(window,text='hit me', width=15,
              height=2, command=hit_me)
              #botton with action hit_me
b.pack()

#renew window in a loop
window.mainloop()



##3 Entry text
#enter text in window, slightly different

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

#entry
e = tk.Entry(window,show=None) #enter as pw show='*', as one show='1' XD
e.pack()

def insert_pt():
    var = e.get() #take about value
    t.insert('insert',var) #as insert format to any assign point with var

def insert_end():
    var = e.get()
    t.insert('end',var) #as end format

def insert_fs():
    var = e.get()
    t.insert(2.2,var) #assign 1 line 2 position
    
#button
b1 = tk.Button(window,text='insert pt', width=15,
              height=1, command=insert_pt)
b1.pack()
b2 = tk.Button(window,text='insert end', width=15,
              height=1, command=insert_end)
b2.pack()
b3 = tk.Button(window,text='insert first line second posi', width=15,
              height=1, command=insert_fs)
b3.pack()

#text
t = tk.Text(window, height=2)
t.pack()

#renew window in a loop
window.mainloop()



##4 Listbox
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

var1 = tk.StringVar()
l = tk.Label(window,bg='yellow',width=4, textvariable=var1)
l.pack()

def print_select():
    value = lb.get(lb.curselection()) #mouse select one from list lb
    var1.set(value)
    
#button
b1 = tk.Button(window,text='print selection', width=15,
              height=1, command=print_select)
b1.pack()

#list
var2 = tk.StringVar()
var2.set((11,22,33,44))
lb = tk.Listbox(window,listvariable = var2)
list_items = [1,2,3,4]
for i in list_items: #could iterate in list
    lb.insert('end',i)
lb.insert(1,'first') #could insert with index
lb.insert(2,'second')
lb.delete(2)
lb.pack()



##5 Radio button
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

var = tk.StringVar()
l = tk.Label(window,bg='yellow',width=20,text = 'empty')
l.pack()

def print_select():
    l.config(text= 'you have choose '+var.get()) #change above parameter config, ex text

r1 = tk.Radiobutton(window,text='Opt A',
                    variable=var, value='A', #give var as 'A'
                    command=print_select)
r1.pack()
r2 = tk.Radiobutton(window,text='Opt B',
                    variable=var, value='B', #give var as 'A'
                    command=print_select)
r2.pack()
r3 = tk.Radiobutton(window,text='Opt C',
                    variable=var, value='C', #give var as 'A'
                    command=print_select)
r3.pack()



##6 Scale
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

l = tk.Label(window,bg='yellow',width=20,text = 'empty')
l.pack()

def print_select(v):
    l.config(text= 'you have choose '+v) #change above parameter config, ex text

s = tk.Scale(window, label='try me', from_=1, to=10, orient=tk.HORIZONTAL,
             length=200, showvalue=1, tickinterval=3, resolution=.01,
             command=print_select) #here has default value v
s.pack()
window.mainloop()



##7 Checkbotton could select all multiple
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

l = tk.Label(window,bg='yellow',width=20,text = 'empty')
l.pack()

def print_select():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love only Python')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')

var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window,text='Python',variable=var1,onvalue=1,offvalue=0,
                    command=print_select)
c2 = tk.Checkbutton(window,text='C++',variable=var2,onvalue=1,offvalue=0,
                    command=print_select)
c1.pack()
c2.pack()

window.mainloop()



##8 Canvas
#for
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('400x400')

canvas=tk.Canvas(window,bg='blue',height=200,width=400)
image_file=tk.PhotoImage(file='cc.png')
image=canvas.create_image(10,10,anchor='nw',image=image_file) #NW, N, NE, E...
x0,y0,x1,y1=50,50,80,80
line=canvas.create_line(x0,y0,x1,y1)
oval=canvas.create_oval(x0,y0,x1,y1,fill='red')
rec=canvas.create_rectangle(5,2,20,30,fill='green')
arc=canvas.create_arc(143,153,211,61,fill='blue',start=0,extent=37)
canvas.pack()

def mov():
    canvas.move(rec, 0, 2) #right 0, down 2
b = tk.Button(window,text='move',command=mov).pack()

window.mainloop()




##9 Manual
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('400x400')

counter=0
def do_job():
    global counter
    l.config(text='do ' +str(counter))
    counter+=1
    
l=tk.Label(window,text='',bg='yellow')
l.pack()

menubar=tk.Menu(window) #window的
filemenu=tk.Menu(menubar,tearoff=0) #定出第一個
menubar.add_cascade(label='File',menu=filemenu) #連上去
filemenu.add_command(label='New',command=do_job) #第一按鈕
filemenu.add_command(label='Open',command=do_job) #第二按鈕
filemenu.add_command(label='Save',command=do_job)

submenu=tk.Menu(filemenu)
filemenu.add_cascade(label='Import',menu=submenu,underline=0)
submenu.add_command(label='Sub1',command=do_job)

filemenu.add_separator()
filemenu.add_command(label='Exit',command=window.quit)

editmenu=tk.Menu(menubar,tearoff=0) #定出第二個
menubar.add_cascade(label='Edit',menu=editmenu) #連上去
editmenu.add_command(label='Cut',command=do_job) #第一按鈕
editmenu.add_command(label='Copy',command=do_job) #第二按鈕
editmenu.add_command(label='Paste',command=do_job)

window.config(menu=menubar)

window.mainloop()



##10 Frame window in a window
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

tk.Label(window,text='on the window').pack()

fm=tk.Frame(window)
fm.pack()
fm_l=tk.Frame(fm,) #sub left frame on frame
fm_r=tk.Frame(fm)
fm_l.pack(side='left') #base on frame
fm_r.pack(side='right')
        
tk.Label(fm_l,text='fm_l 1').pack()
tk.Label(fm_l,text='fm_l 2').pack()
tk.Label(fm_r,text='fm_r 1').pack()

window.mainloop()



##11 Messagebox
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

def hit():
    #tk.messagebox.showinfo(title='hi',message='hahhaha')
    #tk.messagebox.showwarning(title='hi',message='small wrong')
    #tk.messagebox.showerror(title='hi',message='no run anymore')
    #print(tk.messagebox.askquestion(title='hi',message='hahhaha')) #return yes/no
    #if return=='yes': #continue do something after yes/no....
    #print(tk.messagebox.askyesno(title='hi',message='hahhaha')) #return T/F
    #print(tk.messagebox.asktrycancel(title='hi',message='hahhaha')) #return T/F
    print(tk.messagebox.askokcancel(title='hi',message='hahhaha')) #return yes/no
  
tk.Button(window, text='hitme',command=hit).pack()

window.mainloop()



##12 Pack grid place
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

#m1 pack
tk.Label(window,text=1).pack(side='top') #bottom left right

#m2 grid
for i in range(4):
    for j in range(3):
        tk.Label(window,text=(i,j)).grid(row=i,column=j,padx=10,pady=12) #extend padx ipadx

#m3 place
tk.Label(window,text=1).place(x=10,y=100,anchor='nw')

window.mainloop()



131415 Ex1
####import tkinter as tk
####import pickle
####
####window = tk.Tk()
####window.title('Welcome')
####window.geometry('450x300')
####
#####image
####canvas=tk.Canvas(window,height=200,width=500)
####image_file=tk.PhotoImage(file='cc.png')
####image=canvas.create_image(0,0,anchor='nw',image=image_file)
####canvas.pack(side='top')
####
#####labelx2 entryx2
####tk.Label(window,text='User name').place(x=50,y=200)
####tk.Label(window,text='User name').place(x=50,y=230)
####
####var_username = tk.StringVar() #set var for user name
####var_username.set('example@mail.com') #give default
####e_username=tk.Entry(window,textvariable=var_username)
####e_username.place(x=160,y=200)
####
####var_pw = tk.StringVar()
####e_pw=tk.Entry(window,textvariable=var_pw,show='*')
####e_pw.place(x=160,y=230)
####
#####login function
####def usr_login():
####    usr_name=var_username.get()
####    usr_pwd=
####
####
#####login signup button
####btn_login = tk.Button(window, text='Login', command=usr_login)
####btn_login.place(x=170, y=290)
####btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
####btn_sign_up.place(x=270, y=290)
####
####
####window.mainloop()

import tkinter as tk
from tkinter import messagebox  # import this to fix messagebox error
import pickle

window = tk.Tk()
window.title('Welcome to Mofan Python')
window.geometry('450x300')

# welcome image
canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(0,0, anchor='nw', image=image_file)
canvas.pack(side='top')

# user information
tk.Label(window, text='User name: ').place(x=50, y= 150)
tk.Label(window, text='Password: ').place(x=50, y= 190)

var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)

def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome', message='How are you? ' + usr_name)
        else:
            tk.messagebox.showerror(message='Error, your password is wrong, try again.')
    else:
        is_sign_up = tk.messagebox.askyesno('Welcome',
                               'You have not signed up yet. Sign up today?')
        if is_sign_up:
            usr_sign_up()

def usr_sign_up():
    def sign_to_Mofan_Python():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
        #compare new pw with pw confirm
        if np != npf:
            tk.messagebox.showerror('Error', 'Password and confirm password must be the same!')
        #already user    
        elif nn in exist_usr_info:
            tk.messagebox.showerror('Error', 'The user has already signed up!')
        #new user saving
        else:
            exist_usr_info[nn] = np
            with open('usrs_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
            tk.messagebox.showinfo('Welcome', 'You have successfully signed up!')
            window_sign_up.destroy()
            
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    new_name.set('example@python.com')
    tk.Label(window_sign_up, text='User name: ').place(x=10, y= 10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Confirm password: ').place(x=10, y= 90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)

    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_Mofan_Python)
    btn_comfirm_sign_up.place(x=150, y=130)

# login and sign up button
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=170, y=230)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=270, y=230)

window.mainloop()


