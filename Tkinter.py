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



##4

