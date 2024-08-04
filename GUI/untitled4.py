from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

pro=Tk()
pro.title("main page")
lbl=Label(pro,text="Library Management System",fg= "white",bg="purple",font="Tahoma 20 bold",width=37)
lbl.grid(row=0,column=2,)
pro.geometry("1250x750+300+300")

frame=Frame(pro)

def fun():
    pro.destroy()





def return_book():
       lbl1=Label(frame,text="student id",fg="white",bg="black",font=("Tahoma 12 bold"))
       lbl1.grid(row=0,column=0,pady=10,padx=10)
       text=Entry(frame)
       text.grid(row=0,column=1,pady=10,padx=10)
       lbl2=Label(frame,text="book id",fg="white",bg="black",font=("Tahoma 12 bold"))
       lbl2.grid(row=1,column=0,pady=10,padx=10)
       txt2=Entry(frame)
       txt2.grid(row=1,column=1,pady=10,padx=10)
       lbl3=Label(frame,text="borrow date",fg="white",bg="black",font=("Tahoma 12 bold"))
       lbl3.grid(row=2,column=0,pady=10,padx=10)
       txt3=Entry(frame)
       txt3.grid(row=2,column=1,pady=10,padx=10)
       lbl4=Label(frame,text="due date",fg="white",bg="black",font=("Tahoma 12 bold"))
       lbl4.grid(row=3,column=0,pady=10,padx=10)
       txt4=Entry(frame)
       txt4.grid(row=3,column=1,pady=10,padx=10)
       lbl5=Label(frame,text="The period of delay",fg="white",bg="black",font=("Tahoma 12 bold"))
       lbl5.grid(row=4,column=0,pady=10,padx=10)
       txt5=Entry(frame)
       txt5.grid(row=4,column=1,pady=10,padx=10)
       btn=Button(frame,text="quit",fg="blue",bg="red",font=("Tahoma",12,"bold"))
       btn.grid()
       btn2=Button(frame,text="submit",fg="black",bg="green",font=("Tahoma",12,"bold"))
       btn2.grid(row=5,column=1,pady=10,padx=10)
       btn3=Button(frame,text="update",fg="black",bg="green",font=("Tahoma",12,"bold"))
       btn3.grid()
       btn4=Button(frame,text="delete",fg="black",bg="green",font=("Tahoma",12,"bold"))
       btn4.grid(row=6,column=1,pady=10,padx=10)
      
      







def borrow_book():
       lbl1=Label(frame,text="student id",fg="white",bg="black",font=("Tahoma 12 bold"))
       lbl1.grid(row=0,column=0,pady=10,padx=10)
       text=Entry(frame)
       text.grid(row=0,column=1,pady=10,padx=10)
       lbl2=Label(frame,text="book id",fg="white",bg="black",font=("Tahoma 12 bold"))
       lbl2.grid(row=1,column=0,pady=10,padx=10)
       txt2=Entry(frame)
       txt2.grid(row=1,column=1,pady=10,padx=10)
       lbl3=Label(frame,text="borrow date",fg="white",bg="black",font=("Tahoma 12 bold"))
       lbl3.grid(row=2,column=0,pady=10,padx=10)
       txt3=Entry(frame)
       txt3.grid(row=2,column=1,pady=10,padx=10)
       lbl4=Label(frame,text="due date",fg="white",bg="black",font=("Tahoma 12 bold"))
       lbl4.grid(row=3,column=0,pady=10,padx=10)
       txt4=Entry(frame)
       txt4.grid(row=3,column=1,pady=10,padx=10)
       btn=Button(frame,text="quit",fg="blue",bg="red",font=("Tahoma",12,"bold"))
       btn.grid()
       btn2=Button(frame,text="submit",fg="black",bg="green",font=("Tahoma",12,"bold"))
       btn2.grid(row=4,column=1,pady=10,padx=10)
       btn3=Button(frame,text="update",fg="black",bg="green",font=("Tahoma",12,"bold"))
       btn3.grid()
       btn4=Button(frame,text="delete",fg="black",bg="green",font=("Tahoma",12,"bold"))
       btn4.grid(row=6,column=1,pady=10,padx=10)





def add_student():
       lbl1=Label(frame,text="student id",fg="white",bg="black",font=("Tahoma 12 bold"))
       lbl1.grid(row=0,column=0,pady=10,padx=10)
       text=Entry(frame)
       text.grid(row=0,column=1,pady=10,padx=10)
       lbl2=Label(frame,text="student name",fg="white",bg="black",font=("Tahoma 12 bold"))
       lbl2.grid(row=1,column=0,pady=10,padx=10)
       txt2=Entry(frame)
       txt2.grid(row=1,column=1,pady=10,padx=10)
       lbl3=Label(frame,text="father name",fg="white",bg="black",font=("Tahoma 12 bold"))
       lbl3.grid(row=2,column=0,pady=10,padx=10)
       txt3=Entry(frame)
       txt3.grid(row=2,column=1,pady=10,padx=10)
       lbl4=Label(frame,text="age",fg="white",bg="black",font=("Tahoma 12 bold"))
       lbl4.grid(row=3,column=0,pady=10,padx=10)
       txt4=Entry(frame)
       txt4.grid(row=3,column=1,pady=10,padx=10)
       lbl5=Label(frame,text="Academic section",fg="white",bg="black",font=("Tahoma 12 bold"))
       lbl5.grid(row=4,column=0,pady=10,padx=10)
       txt5=Entry(frame)
       txt5.grid(row=4,column=1,pady=10,padx=10)
       btn=Button(frame,text="quit",fg="blue",bg="red",font=("Tahoma",12,"bold"))
       btn.grid()
       btn2=Button(frame,text="submit",fg="black",bg="green",font=("Tahoma",12,"bold"))
       btn2.grid(row=5,column=1,pady=10,padx=10)
       btn3=Button(frame,text="update",fg="black",bg="green",font=("Tahoma",12,"bold"))
       btn3.grid()
       btn4=Button(frame,text="delete",fg="black",bg="green",font=("Tahoma",12,"bold"))
       btn4.grid(row=6,column=1,pady=10,padx=10)


def add_book():
       lbl1=Label(frame,text="book id",fg="white",bg="black",font=("Tahoma 12 bold"))
       lbl1.grid(row=0,column=0,pady=10,padx=10)
       text=Entry(frame)
       text.grid(row=0,column=1,pady=10,padx=10)
       lbl2=Label(frame,text="book name",fg="white",bg="black",font=("Tahoma 12 bold"))
       lbl2.grid(row=1,column=0,pady=10,padx=10)
       txt2=Entry(frame)
       txt2.grid(row=1,column=1,pady=10,padx=10)
       lbl3=Label(frame,text="publisher",fg="white",bg="black",font=("Tahoma 12 bold"))
       lbl3.grid(row=2,column=0,pady=10,padx=10)
       txt3=Entry(frame)
       txt3.grid(row=2,column=1,pady=10,padx=10)
       lbl4=Label(frame,text="price",fg="white",bg="black",font=("Tahoma 12 bold"))
       lbl4.grid(row=3,column=0,pady=10,padx=10)
       txt4=Entry(frame)
       txt4.grid(row=3,column=1,pady=10,padx=10)
       lbl5=Label(frame,text="publisher year",fg="white",bg="black",font=("Tahoma 12 bold"))
       lbl5.grid(row=4,column=0,pady=10,padx=10)
       txt5=Entry(frame)
       txt5.grid(row=4,column=1,pady=10,padx=10)
       btn=Button(frame,text="quit",fg="blue",bg="red",font=("Tahoma",12,"bold"),command=pro.destroy)
       btn.grid()
       btn2=Button(frame,text="submit",fg="black",bg="green",font=("Tahoma",12,"bold"),command=book)
       btn2.grid(row=5,column=1,pady=10,padx=10)
       btn3=Button(frame,text="update",fg="black",bg="gereen",font=("Tahoma",12,"bold"))
       btn3.grid()
       btn4=Button(frame,text="delete",fg="black",bg="green",font=("Tahoma",12,"bold"))
       btn4.grid(row=6,column=1,pady=10,padx=10)
       
       tree=treeview(root,)
       
       
def book():
    
    book_id=text.get()
    name=txt2.get()
    publisher=txt3.get()
    price=txt4.get()
    p_year=txt5.get()
    if txt2!=txt3:
       messagebox.showinfo("Info","Saved successfully")
    

btn=Button(pro,text="New Student",fg="blue",bg="black",font=("Tahoma",12,"bold"),command=add_student)
btn.grid(row=2,column=0,padx=40,pady=10,ipady=5)


btn=Button(pro,text="New Book",fg="blue",bg="black",font=("Tahoma",12,"bold"),command=add_book)
btn.grid(row=2,column=1,padx=40,pady=10,ipady=5)

btn=Button(pro,text="borrow book",fg="blue",bg="black",font=("Tahoma",12,"bold"),command=borrow_book)
btn.grid(row=2,column=2,padx=40,pady=10,ipady=5)

btn=Button(pro,text="Return Book",fg="blue",bg="black",font=("Tahoma",12,"bold"),command=return_book)
btn.grid(row=2,column=3,padx=40,pady=10,ipady=5)

btn=Button(pro,text="LogOut",fg="blue",bg="black",font=("Tahoma",12,"bold"),command=fun)
btn.grid(row=2,column=4,padx=40,pady=10,ipady=5)
frame.place(anchor='center',relx=0.5,rely=0.4)

pro.mainloop()
