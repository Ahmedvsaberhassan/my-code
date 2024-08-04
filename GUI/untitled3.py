from tkinter import *
from tkinter import messagebox
from subprocess import call
#import webbrowser
root= Tk()
root.title("Login")
root.geometry("1250x750+300+300")

frame=Frame(root)

   
     

def fun():
    root.destroy()

    
def check_info():
    txt_user='ahmed saber'
    txt_password='01021292349'
    Username=text.get()
    Password=text2.get()
    
    if Username!=txt_user and Password!=txt_password:
        messagebox.showerror("Error","Invalid Username or Password")
    else:
        root.destroy()
        import untitled1
        
        call(["python","untitled1.py"])
        
lbl1=Label(root,text="Library Management System",fg="white",bg="purple",font="Tahoma 20 bold",width=80)
#lbl1.pack(pady=30,side="top")
lbl1.grid(row=0,column=6)
lbl1=Label(frame,text="Username",fg="white",bg="black",font="Tahoma 12 bold")
#lbl1.pack(pady=20,side="left",anchor="nw",ipady=5)
lbl1.grid(row=0,column=0,padx=10,pady=10)
text=Entry(frame)
text.grid(row=0,column=1,padx=10,pady=10)
#text.pack(pady=20,padx=20,side="left",anchor="nw",ipady=5)
lbl2=Label(frame,text="Password",fg="white",bg="black",font="Tahoma 12 bold")
lbl2.grid(row=1,column=0,padx=10,pady=10)
#lbl2.pack(pady=20,padx=20,side="left",anchor="nw",ipady=5)
text2=Entry(frame,show='*')
text2.grid(row=1,column=1,padx=10,pady=10)
#text2.pack(pady=20,padx=20,side="left",anchor="nw",ipady=5)
button2=Button(frame,text="close",fg="blue",bg="red",font=("Tahoma",12,"bold"),command=fun)
button2.grid(row=2,column=0,columnspan=1,padx=10,pady=10)
#button2.pack(pady=10,padx=20,side="right")
button=Button(frame,text="Enter",fg="blue",bg="green",font=("Tahoma",12,"bold"),command=check_info)
button.grid(row=2,column=2,columnspan=3,padx=10,pady=10)
#button.pack(pady=10,padx=20,side="left")

frame.place(anchor='center',relx=0.5,rely=0.5)
#lbl=Label(root,text="left",fg="red",bg="black",width=20,font=("Tahoma",14,"bold"))
#lbl.pack(side=LEFT)
#lbl2=Label(root,text="right",fg="red",bg="black",width=20,font=("Tahoma",14,"bold"))
#lbl2.pack(side=RIGHT)

#def displayname():
 #   messagebox.showerror("error","wrong password")

#btn=Button(root,text="open",command=displayname,fg="black",bg="white",width=20,font=("Tahoma",14,"bold"))
#btn.pack()  
root.mainloop()
