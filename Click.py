from tkinter import *

root=Tk()
root.title("Count Click")
root.geometry("300x200+1100+500")
root.resizable(False, False)
 
 
Today = Label(root, text="TODAY").place(x=130, y=30)
Click=Label(root, text="Clicked : ").place(x=100, y=70)
Click=Label(root, text="Total : ").place(x=100, y=90)   




root.mainloop()