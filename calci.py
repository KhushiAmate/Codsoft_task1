from tkinter import *

class Calci:
    def __init__(self,master):
        master.title("SIMPLE CALCULATOR")
        master.geometry("480x470")
        master.config(bg="black")

        self.equation=StringVar()
        self.entry_val=''
        Entry(width=20,bg="#fff",font=("arial",30,'bold'),textvariable=self.equation).place(x=20,y=10)

        Button(width=10,height=2,text='(',relief='flat',bg="white",command=lambda:self.show("("),font=("arial",15,"bold")).place(x=20 ,y=80)
        Button(width=10,height=2,text=')',relief='flat',bg="white",command=lambda:self.show(")"),font=("arial",15,"bold")).place(x=120 ,y=80)
        Button(width=10,height=2,text='%',relief='flat',bg="white",command=lambda:self.show("%"),font=("arial",15,"bold")).place(x=220 ,y=80)
        Button(width=10,height=2,text='c',relief='flat',bg="white",font=("arial",15,"bold"),command=self.clear).place(x=320 ,y=80)

        Button(width=10,height=2,text='1',relief='flat',bg="white",command=lambda:self.show(1),font=("arial",15,"bold")).place(x=20 ,y=155)
        Button(width=10,height=2,text='2',relief='flat',bg="white",command=lambda:self.show(2),font=("arial",15,"bold")).place(x=120 ,y=155)
        Button(width=10,height=2,text='3',relief='flat',bg="white",command=lambda:self.show(3),font=("arial",15,"bold")).place(x=220 ,y=155)
        Button(width=10,height=2,text='*',relief='flat',bg="white",command=lambda:self.show("*"),font=("arial",15,"bold")).place(x=320 ,y=155)

        Button(width=10,height=2,text='4',relief='flat',bg="white",command=lambda:self.show(4),font=("arial",15,"bold")).place(x=20 ,y=230)
        Button(width=10,height=2,text='5',relief='flat',bg="white",command=lambda:self.show(5),font=("arial",15,"bold")).place(x=120 ,y=230)
        Button(width=10,height=2,text='6',relief='flat',bg="white",command=lambda:self.show(6),font=("arial",15,"bold")).place(x=220 ,y=230)
        Button(width=10,height=2,text='-',relief='flat',bg="white",command=lambda:self.show("-"),font=("arial",15,"bold")).place(x=320 ,y=230)

        Button(width=10,height=2,text='7',relief='flat',bg="white",command=lambda:self.show(7),font=("arial",15,"bold")).place(x=20 ,y=305)
        Button(width=10,height=2,text='8',relief='flat',bg="white",command=lambda:self.show(8),font=("arial",15,"bold")).place(x=120 ,y=305)
        Button(width=10,height=2,text='9',relief='flat',bg="white",command=lambda:self.show(9),font=("arial",15,"bold")).place(x=220 ,y=305)
        Button(width=10,height=2,text='0',relief='flat',bg="white",command=lambda:self.show(0),font=("arial",15,"bold")).place(x=320,y=305)

        Button(width=10,height=2,text='=',relief='flat',bg="white",font=("arial",15,"bold"),command=self.solve).place(x=20 ,y=380)
        Button(width=10,height=2,text='.',relief='flat',bg="white",command=lambda:self.show("."),font=("arial",15,"bold")).place(x=120 ,y=380)
        Button(width=10,height=2,text='+',relief='flat',bg="white",command=lambda:self.show("+"),font=("arial",15,"bold")).place(x=220 ,y=380)
        Button(width=10,height=2,text='/',relief='flat',bg="white",command=lambda:self.show("/"),font=("arial",15,"bold")).place(x=320 ,y=380)

    def clear(self):
        self.entry_val=''
        self.equation.set(self.entry_val)

    def show(self,val):
        self.entry_val+=str(val)
        self.equation.set(self.entry_val)

    def solve(self):
        res=eval(self.entry_val)
        self.equation.set(res)  

window=Tk()
calci=Calci(window)
window.mainloop()    
