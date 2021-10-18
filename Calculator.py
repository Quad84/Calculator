from tkinter import *
import tkinter.messagebox
#__________________________________#


#----------------------------
# Telegram ID : @AL13A_7    |
# --Alisa Alikhani--        |
# GitHub: github.com/Quad84 |
#----------------------------


#__________________________________#
root = Tk()
root.title("Quad Calculator")
root.geometry("350x450")
root.resizable(width=False,height=False)
root.configure(bg="gray")
#__________________________________#
javab = Frame(root, width=350, height=100, bg="gray")
javab.pack(side=TOP , pady=30)

fas = Frame(root, bg="gray")
fas.pack(side=TOP, pady=1)

keyy = Frame(root, bg="gray")
keyy.pack(side=TOP)

fo = Frame(root, bg="gray")
fo.pack(side=TOP)

eg = Frame(root, bg="gray")
eg.pack(side=TOP)

en = Frame(root, bg="gray")
en.pack(side=TOP)

sns = Frame(root, bg="gray")
sns.pack(side=TOP)
    
#___________________________________________#
def errorMsg(ms):
    if ms == 'error':
        tkinter.messagebox.showerror('Error', 'something went wrong')
    
    elif ms == 'ZeroDivisionError':
        tkinter.messagebox.showerror('Division Error', 'Can Not Divide By 0')

kol = StringVar()
kol2 = StringVar()
res = StringVar()
expression = ""
expression2 = ""
select_input = 1
oper = ""

def select_num1():
    tkinter.messagebox.showinfo('Developer Info', 'Name: Alisa\n\nFamily: Alikhani\n\nTelegram: @AL13A_7\n\nGithub: github.com/Quad84')  

def opp(op):
    global expression
    global expression2
    global select_input
    global oper

    oper = op
    kol2.set("")
    expression2 = ""
    select_input = 2

def show_res():
    global select_input
    if oper == "+":
        try:
            plusres = float(kol.get()) + float(kol2.get())
            res.set(plusres)
            select_input = 1
        except ValueError:
            tkinter.messagebox.showerror('Error', 'something went wrong')              
    elif oper == "-":
        try:
            plusres = float(kol.get()) - float(kol2.get())
            res.set(plusres)
            select_input = 1
        except ValueError:
            tkinter.messagebox.showerror('Error', 'something went wrong')  
    elif oper == "*":
        try:
            plusres = float(kol.get()) * float(kol2.get())
            res.set(plusres)
            select_input = 1
        except ValueError:
            tkinter.messagebox.showerror('Error', 'something went wrong')    
    elif oper == "/":
        try:
            plusres = float(kol.get()) / float(kol2.get())
            res.set(plusres)
            select_input = 1
        except ZeroDivisionError:
            tkinter.messagebox.showerror('Division Error', 'Can Not Divide By 0')
        except ValueError:
            tkinter.messagebox.showerror('Error', 'something went wrong')              

def set_number(number):
    global expression
    global expression2
    global select_input

    expression = expression + str(number)
    expression2 = expression2 + str(number)

    if select_input == 1:
        expression2 = ""
        kol.set(expression)

    elif select_input == 2:
        expression = ""
        kol2.set(expression2)

def clear():
    global expression
    global expression2
    global select_input
    select_input = 1
    expression = ""
    expression2 = ""
    kol.set("")
    kol2.set("")
    res.set("")
    
#______________________________________
    
zero0 = Button(keyy,text="7",width=5 , height=2,highlightbackground="gray",command=lambda:set_number(7))
zero0.pack(side=LEFT, padx=10, pady=10)

one1 = Button(keyy,text="8",width=5 , height=2,highlightbackground="gray",command=lambda:set_number(8))
one1.pack(side=LEFT, padx=10, pady=10)

tow2 = Button(keyy,text="9",width=5 , height=2,highlightbackground="gray",command=lambda:set_number(9))
tow2.pack(side=LEFT, padx=10, pady=10)

three3 = Button(keyy,text="+",width=5 , height=2,highlightbackground="gray",command=lambda:opp("+"))
three3.pack(side=LEFT, padx=10, pady=10)

four4 = Button(fo,text="4",width=5 , height=2,highlightbackground="gray",command=lambda:set_number(4))
four4.pack(side=LEFT, padx=10, pady=10)

five5 = Button(fo,text="5",width=5 , height=2,highlightbackground="gray",command=lambda:set_number(5))
five5.pack(side=LEFT, padx=10, pady=10)

six6 = Button(fo,text="6",width=5 , height=2,highlightbackground="gray",command=lambda:set_number(6))
six6.pack(side=LEFT, padx=10, pady=10)

seven7 = Button(fo,text="_",width=5 , height=2,highlightbackground="gray",command=lambda:opp("-"))
seven7.pack(side=LEFT, padx=10, pady=10)

eghit8 = Button(eg,text="1",width=5 , height=2,highlightbackground="gray",command=lambda:set_number(1))
eghit8.pack(side=LEFT, padx=10, pady=10)

nine9 = Button(eg,text="2",width=5 , height=2,highlightbackground="gray",command=lambda:set_number(2))
nine9.pack(side=LEFT, padx=10, pady=10)

pluss = Button(eg,text="3",width=5 , height=2,highlightbackground="gray",command=lambda:set_number(3))
pluss.pack(side=LEFT, padx=10, pady=10)

minee = Button(eg,text="×",width=5 , height=2,highlightbackground="gray",command=lambda:opp("*"))
minee.pack(side=LEFT, padx=10, pady=10)

zarbb = Button(en,text="Clear",width=5 , height=2,highlightbackground="gray",command=lambda:clear())
zarbb.pack(side=LEFT, padx=10, pady=10)

tags = Button(en,text="0",width=5 , height=2,highlightbackground="gray",command=lambda:set_number(0))
tags.pack(side=LEFT, padx=10, pady=10)

moss = Button(en,text="=",width=5 , height=2,highlightbackground="gray",command=lambda:show_res())
moss.pack(side=LEFT, padx=10, pady=10)

cls = Button(en,text="÷",width=5 , height=2,highlightbackground="gray",command=lambda:opp("/"))
cls.pack(side=LEFT, padx=10, pady=10)

sn = Button(sns,text="Developer Info",width=15 , height=2,highlightbackground="gray",command=lambda:select_num1())
sn.pack(side=LEFT, padx=10, pady=10)
#____________________________________________________

Emp1 = Entry(javab, width=40 , textvariable=kol)
Emp1.place(x=55,width=100,height=35)

Emp2 = Entry(javab, width=40 , textvariable=kol2)
Emp2.place(x=190 ,width=100,height=35)

Endres = Entry(javab, width=100 , textvariable=res)
Endres.place(x=55 , y=50 ,width=235,height=35)
#____________________________________________________
root.mainloop()
