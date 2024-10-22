from tkinter import *
from tkinter import messagebox
import random
import time

window=Tk()

window.geometry("700x500")
window.title("TYPING SPEED CHECKER")

def game(event,f):
    start=time.time()
    
    def score(event):
        user_para=var2.get()
        end=time.time()

        def mistake(para,user_para):
            error=0
            for i in range(len(para)):
                try:
                    if para[i]!=user_para[i]:
                        error+=1
                except:
                    error+=1
            return error
        

        def time_taken(start,end):
            return round(end-start,2)
        t=time_taken(start,end)

        def wpm(time_taken,start,end,user_para):
            a=user_para.split()
            return round((len(a)/time_taken(start,end))*60,2)
        w=wpm(time_taken,start,end,user_para)

        def accuracy(mistake,para,user_para):
            return round(((len(para)-mistake(para,user_para))/len(para))*100)
        acc=accuracy(mistake,para,user_para)
    

        f2.pack_forget()
        f3=Frame(window,borderwidth=5,background="yellow",relief=SUNKEN,pady=10)
        f3.pack(side="top",fill="both",expand=True)
        if w>30:
            l3=Label(f3,text=f"WOW Too Quick {var1.get()}",background="yellow",font="Tw_Cen_MT 30 bold",fg="red").pack(pady=10,fill=X)
        elif w>20:
            l3=Label(f3,text=f"Excelent {var1.get()}",background="yellow",font="Tw_Cen_MT 30 bold",fg="red").pack(pady=10,fill=X)
        else:
            l3=Label(f3,text=f"WellDone {var1.get()}",background="yellow",font="Tw_Cen_MT 30 bold",fg="red").pack(pady=10,fill=X)

        l4=Label(f3,text=f"Total Time => {t}sec",font="Tahoma 20 bold",background="silver",fg="white",relief=SUNKEN,borderwidth=6).pack(pady=10)
        l5=Label(f3,text=f"Words Per Minute => {w}words/min",font="Tahoma 20 bold",background="silver",fg="white",relief=SUNKEN,borderwidth=6).pack(pady=10)
        l6=Label(f3,text=f"Accuracy => {acc}%",font="Tahoma 20 bold",background="silver",fg="white",relief=SUNKEN,borderwidth=6).pack(pady=10)

        btn3=Button(f3,text="TRY AGAIN",borderwidth=5,background="skyblue",font="Tahoma 30 bold")
        btn3.bind("<Button-1>",lambda event:game(event,f3))
        btn3.pack(pady=20)


    if not var1.get():
        messagebox.showerror("Error","Input can't be empty")
    else:
        paragraph=["Python is a programming language that is interpreted,\n object-oriented, and considered to be high-level too." , "Python is one of the easiest yet most useful programming\n languages which is widely used in the software industry." , "People use Python for Competitive Programming,\n Web Development, and creating software." , "Due to its easiest syntax, it is recommended for beginners\n who are new to the software engineering field." , "Its demand is growing at a very rapid pace due to its vast\n use cases in Modern Technological fields like\n Data Science, Machine learning, and Automation Tasks." , "For many years now, it has been ranked among the top\n Programming languages used for multiple tasks." , "Python is a set of instructions that we give in the form of a\n Program to our computer to perform any specific task."]
        para=paragraph[random.randrange(len(paragraph))]
        
        f.pack_forget()
        
        f2=Frame(window,borderwidth=5,background="black",relief=GROOVE,pady=80)
        
        l2=Label(f2,text=para,font="Leelawadee 17 bold",fg="purple",bg="black").pack(pady=30)

        var2=StringVar()
        b=Entry(f2,textvariable=var2,width=50,font="Leelawadee 17 bold",fg="black")
        b.focus_set()
        b.bind("<Return>",score)
        b.pack(pady=30)
        f2.pack(side="top",fill="both",expand=True)
        
    
        
head=Label(text="TYPING MASTER",font="Impact 50 bold italic underline",background="silver",borderwidth=7,relief=SUNKEN)
head.pack(side="top",fill=X)


f1=Frame(window,borderwidth=5,background="black",relief=GROOVE,pady=80)
f1.pack(side="top",fill="both",expand=True)

l1=Label(f1,text="Enter Your Name",font="perpetua 25 bold",bg="black",fg="white").pack(pady=20)

var1=StringVar()
name=Entry(f1,textvariable=var1,font="Wingdings_2 25",fg="red")
name.bind("<Return>",lambda event:game(event,f1))
name.pack()

btn1=Button(f1,text="START",fg="black",background="skyblue",font="perpetua 25 bold",borderwidth=4)
btn1.bind("<Button-1>",lambda event: game(event,f1))
btn1.pack(pady=20)

window.mainloop()