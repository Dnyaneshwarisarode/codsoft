from tkinter import *
win=Tk()
def add():
    a=int(e1.get())
    b=int(e2.get())
    c=a+b
    l4.config(text=""+str(c))

def sub():
    a=int(e1.get())
    b=int(e2.get())
    c=a-b
    l4.config(text=""+str(c))

def mul():
    a=int(e1.get())
    b=int(e2.get())
    c=a*b
    l4.config(text=""+str(c))

def div():
    a=int(e1.get())
    b=int(e2.get())
    c=a/b
    l4.config(text=""+str(c))

win.title('calculator')
win.geometry('500x500')
f1=('arial',15,'bold')
l1=Label(win,bd=3,text='enter 1st no',font=f1)
l1.place(x=50,y=50)
e1=Entry(win,bd=3,font=f1)
e1.place(x=200,y=50)
l2=Label(win,bd=3,text='enter 2st no',font=f1)
l2.place(x=50,y=100)
e2=Entry(win,bd=3,font=f1)
e2.place(x=200,y=100)

l3=Label(win,bd=3,text='result',font=f1)
l3.place(x=50,y=150)
l4=Label(win,text='-------',bd=3,font=f1)
l4.place(x=200,y=150)

b1=Button(win,text='add',font=f1,command=add)
b1.place(x=50,y=200)

b2=Button(win,text='sub',font=f1,command=sub)
b2.place(x=120,y=200)

b3=Button(win,text='mul',font=f1,command=mul)
b3.place(x=190,y=200)

b4=Button(win,text='div',font=f1,command=div)
b4.place(x=260,y=200)

b5=Button(win,text='exit',font=f1,command=quit)
b5.place(x=330,y=200)

win.mainloop()




