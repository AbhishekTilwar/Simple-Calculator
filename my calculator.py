
from tkinter import *
r=Tk()

r.title("my calculator")
operator=""
def click(n):
    global operator
    operator=operator+ str(n)
    t.set(operator)
def clear():
        global operator
        operator=""
        t.set(operator)   
def equal():
    try:
        global operator
        sumup=str(eval(operator))
        t.set(sumup)
    except:
        t.set("error")
t=StringVar()
rs1=Entry(r,bd=4,borderwidth=6,bg="powder blue",fg="dark blue",font=('arial',20,'bold'),justify=RIGHT,textvariable=t).grid(row=0,column=0,columnspan=4,padx=16,pady=8)
ce=Button(r,text="CE",bg="light blue",fg="dark blue",bd=3,width=43,command=clear).grid(row=2,column=0,columnspan=4,padx=15,pady=6)#clear
de=Button(r,text=".",bg="light blue",fg="dark blue",bd=5,width=7,command=lambda:click(".")).grid(row=6,column=0)#decimal
b1=Button(r,text="1",bd=5,width=7,bg="light blue",fg="dark blue",command=lambda:click(1)).grid(row=3,column=0)
b2=Button(r,text="2",bd=5,width=7,bg="light blue",fg="dark blue",command=lambda:click(2)).grid(row=3,column=1)
b3=Button(r,text="3",bd=5,width=7,bg="light blue",fg="dark blue",command=lambda:click(3)).grid(row=3,column=2)
b4=Button(r,text="4",bd=5,width=7,bg="light blue",fg="dark blue",command=lambda:click(4)).grid(row=4,column=0)
b5=Button(r,text="5",bd=5,width=7,bg="light blue",fg="dark blue",command=lambda:click(5)).grid(row=4,column=1)
b6=Button(r,text="6",bd=5,width=7,bg="light blue",fg="dark blue",command=lambda:click(6)).grid(row=4,column=2)
b7=Button(r,text="7",bd=5,width=7,bg="light blue",fg="dark blue",command=lambda:click(7)).grid(row=5,column=0)
b8=Button(r,text="8",bd=5,width=7,bg="light blue",fg="dark blue",command=lambda:click(8)).grid(row=5,column=1)
b9=Button(r,text="9",bd=5,width=7,bg="light blue",fg="dark blue",command=lambda:click(9)).grid(row=5,column=2)
b0=Button(r,text="0",bd=5,width=7,bg="light blue",fg="dark blue",command=lambda:click(0)).grid(row=6,column=1)
add=Button(r,text="+",bd=5,width=7,bg="powder blue",fg="dark blue",command=lambda:click("+")).grid(row=3,column=3)#addition button
sub=Button(r,text="-",bd=5,width=7,bg="powder blue",fg="dark blue",command=lambda:click("-")).grid(row=4,column=3)#substraction button
mult=Button(r,text="*",bd=5,width=7,bg="powder blue",fg="dark blue",command=lambda:click("*")).grid(row=5,column=3)#multiplication button
div=Button(r,text="/",bd=5,width=7,bg="powder blue",fg="dark blue",command=lambda:click("/")).grid(row=6,column=3)#division button
bE=Button(r,text="=",bd=5,width=7,bg="powder blue",fg="dark blue",command=equal).grid(row=6,column=2)            #equal button
r.bind("<Return>", equal)
r.mainloop()

