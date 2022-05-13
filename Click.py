
from tkinter import *
from tkinter import filedialog

root=Tk()
root.title("Count Click")
root.geometry("300x200+1100+500")
root.resizable(False, False)
Clk = 0        
# file = open('C:/Users/we202/Documents/GitHub/DevApp/count.txt', 'w')
# Clk2 = file
# file.close
# print(Clk2)
Click=Label(root, text="Clicked : ").place(x=100, y=70)
Click2=Label(root, text="Total : ").place(x=100, y=90)

#클릭시 카운트 올라감
def clickevent(self):
    global Clk 
    # global Clk2
    Clk += 1
    # Clk2 += 1
    global Click
    Click=Label(root, text="Clicked : "+str(Clk)).place(x=100, y=70)
    Click2=Label(root, text="Total : "+str(Clk)).place(x=100, y=90)   
    
#세이브파일 생성 기능 추가 예정    
def Save():
    filename = filedialog.asksaveasfilename(initialdir="/", title="Select file",
    filetypes=(("TXT files", "*.txt"),("all files", "*.*")))
    



#위젯    
Today = Label(root, text="TODAY").place(x=130, y=30)
root.bind("<Button-1>", clickevent)

Save = Button(root, text="save", command=Save).place(x=10,y=10) 



root.mainloop()