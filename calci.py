from tkinter import *
root= Tk()
root.geometry("400x800")
root.title("calculator")
def click(event):
    global sval
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if sval.get().isdigit():
            value= int(sval.get())
        else:
            value = eval(sc.get())
        sval.set(value)
        sc.update()
    elif text=="C":
        sval.set("")
        sc.update()
    else:
        sval.set(sval.get() + text)
        sc.update()

sval=StringVar()
sval.set("")
sc=Entry(root,textvar=sval,font=('calibre',20))
sc.pack(fill=X,ipadx=40,ipady=40,pady=30,padx=12)

f=Frame(root,bg="skyblue",borderwidth=7,relief="groove")

a = ["+", "-", "*", "="]
start=0
end=4
for i in range(start, end, 1):
    b=Button(f,padx=15,pady=10,text=a[i:i+1],font=('lucida' ,20,'bold'))
    b.bind("<Button-1>",click)
    b.pack(side="left", pady=14, padx=12, )

f.pack(side=TOP,fill=Y)

f6=Frame(root,bg="skyblue",borderwidth=7,relief="groove")

a = ["%", "/", "()", "^"]
start=0
end=4
for i in range(start, end, 1):
    b=Button(f6,padx=15,pady=10,text=a[i:i+1],font=('lucida' ,20,'bold'))
    b.bind("<Button-1>",click)
    b.pack(side="left", pady=14, padx=12, )

f6.pack(side=TOP,fill=Y)


f1=Frame(root,bg="gray",borderwidth=7,relief="groove")
t = ["1", "2", "3", "4"]
start=0
end=4

for i in range(start,end,1):
    b=Button(f1,padx=15,pady=10,text=t[i:i+1],font=('lucida' ,20,'bold'))
    b.bind("<Button-1>",click)
    b.pack(side="left", pady=14, padx=12)


f1.pack(side=TOP)

f2=Frame(root,bg="gray",borderwidth=7,relief="groove")
n = ["5", "6", "7", "8"]
start=0
end=4
for i in range(start,end,1):
    b=Button(f2,padx=15,pady=10,text=n[i:i+1],font=('lucida' ,20,'bold'))
    b.bind("<Button-1>",click)
    b.pack(side="left", pady=14, padx=12)

f2.pack(side=TOP)


f4=Frame(root,bg="skyblue",borderwidth=7,relief="groove")

a = ["9", "0", "C", "."]
start=0
end=4
for i in range(start, end, 1):
    b=Button(f4,padx=15,pady=10,text=a[i:i+1],font=('lucida' ,20,'bold'))
    b.bind("<Button-1>",click)
    b.pack(side="left", pady=14, padx=12)

f4.pack(side=TOP,fill=Y)
root.mainloop()