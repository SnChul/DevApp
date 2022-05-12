
from tkinter import *


root=Tk()
root.title("Count Click")
root.geometry("300x200+1100+500")
root.resizable(False, False)

Clk = 0        

def clickevent(self):
    global Clk 
    Clk += 1
    global Click
    Click=Label(root, text="Clicked : "+str(Clk)).place(x=100, y=70)
    Click2=Label(root, text="Total : "+str(Clk)).place(x=100, y=90)   
def Save(self):
    print("saved")    
Today = Label(root, text="TODAY").place(x=130, y=30)
root.bind("<Button-1>", clickevent)
Click=Label(root, text="Clicked : ").place(x=100, y=70)
Click2=Label(root, text="Total : ").place(x=100, y=90)
Save = Button(root, text="save", command=Save).place(x=10,y=10) 


root.mainloop()