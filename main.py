from tkinter import*

root=Tk()
root.geometry("1000x550")
root.title("Bill Management")
root.resizable(False,False)

def Reset():
    #print()
    entry_dosa.delete(0,END)
    entry_Cookies.delete(0,END)
    entry_Coffee.delete(0,END)
    entry_Cokacola.delete(0,END)
    entry_Nodules.delete(0,END)
    entry_Biriani.delete(0,END)
    entry_Speed.delete(0,END)
    entry_Sandwise.delete(0,END)


def Total():
    #print()
    try:a1=int(dosa.get())
    except:a1=0

    try:a2=int(Cookies.get())
    except:a2=0

    try:a3 = int(Coffee.get())
    except:a3=0

    try:a4=int(Cokacola.get())
    except:a4=0

    try:a5=int(Nodules.get())
    except:a5=0

    try:a6=int(Biriani.get())
    except:a6=0

    try:a7=int(Speed.get())
    except:a7=0

    try:a8= int(Sandwise.get())
    except:a8=0


    #define cost of each item quantity
    c1=70*a1
    c2=80*a2
    c3=30*a3
    c4=110*a4
    c5=60*a5
    c6=120*a6
    c7=30*a7
    c8=100*a8

    lbl_total=Label(f2,font=("aria",20,"bold"),text="Total",width=16,fg="lightyellow",bg="black")
    lbl_total.place(x=0,y=50)

    entry_total=Entry(f2,font=("aria",20,"bold"),textvariable=Total_bill,bd=6,width=15,bg="lightgreen")
    entry_total.place(x=20,y=100)

    totalcost=c1+c2+c3+c4+c5+c6+c7+c8
    string_bill="Rs",str("%.2f" %totalcost)
    Total_bill.set(string_bill)




Label(text="BILL MANAGEMENT SYSTEM",bg="black",fg="white",font=("calibri",33),width="300",height="2").pack()

#Menu Card
f=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=120)
Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)
Label(f,font=("Lucida Calligrapy",15,"bold"),text="Dosa.....Rs.70/plate",fg="black",bg="lightgreen").place(x=10,y=80)
Label(f,font=("Lucida Calligrapy",15,"bold"),text="Cookies.....Rs.80/plate",fg="black",bg="lightgreen").place(x=10,y=110)
Label(f,font=("Lucida Calligrapy",15,"bold"),text="Coffee.....Rs.30/cup",fg="black",bg="lightgreen").place(x=10,y=140)
Label(f,font=("Lucida Calligrapy",15,"bold"),text="Cokacola.....Rs.110/botol",fg="black",bg="lightgreen").place(x=10,y=170)
Label(f,font=("Lucida Calligrapy",15,"bold"),text="Nodules.....Rs.60/plate",fg="black",bg="lightgreen").place(x=10,y=200)
Label(f,font=("Lucida Calligrapy",15,"bold"),text="Biriani.....Rs.120/plate",fg="black",bg="lightgreen").place(x=10,y=230)
Label(f,font=("Lucida Calligrapy",15,"bold"),text="Speed.....Rs.30/botol",fg="black",bg="lightgreen").place(x=10,y=260)
Label(f,font=("Lucida Calligrapy",15,"bold"),text="Sandwise.....Rs.100/plate",fg="black",bg="lightgreen").place(x=10,y=290)

#Bill
f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text="Bill",font=("calibri",20),bg="lightyellow")
Bill.place(x=120,y=10)

#Entry work
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

dosa=StringVar()
Cookies=StringVar()
Coffee=StringVar()
Cokacola=StringVar()
Nodules=StringVar()
Biriani=StringVar()
Speed=StringVar()
Sandwise=StringVar()
Total_bill=StringVar()

#Label
lbl_dosa=Label(f1,font=("aria",20,"bold"),text="Dosa",width=12,fg="blue4")
lbl_Cookies=Label(f1,font=("aria",20,"bold"),text="Cookies",width=12,fg="blue4")
lbl_Coffee=Label(f1,font=("aria",20,"bold"),text="Coffee",width=12,fg="blue4")
lbl_Cokacola=Label(f1,font=("aria",20,"bold"),text="Cokacola",width=12,fg="blue4")
lbl_Nodules=Label(f1,font=("aria",20,"bold"),text="Nodules",width=12,fg="blue4")
lbl_Biriani=Label(f1,font=("aria",20,"bold"),text="Biriani",width=12,fg="blue4")
lbl_Speed=Label(f1,font=("aria",20,"bold"),text="Speed",width=12,fg="blue4")
lbl_Sandwise=Label(f1,font=("aria",20,"bold"),text="Sandwise",width=12,fg="blue4")

lbl_dosa.grid(row=1,column=0)
lbl_Cookies.grid(row=2,column=0)
lbl_Coffee.grid(row=3,column=0)
lbl_Cokacola.grid(row=4,column=0)
lbl_Nodules.grid(row=5,column=0)
lbl_Biriani.grid(row=6,column=0)
lbl_Speed.grid(row=7,column=0)
lbl_Sandwise.grid(row=8,column=0)

#Entry
entry_dosa=Entry(f1,font=("aria",20,"bold"),textvariable=dosa,bd=6,width=8,bg="lightpink")
entry_Cookies=Entry(f1,font=("aria",20,"bold"),textvariable=Cookies,bd=6,width=8,bg="lightpink")
entry_Coffee=Entry(f1,font=("aria",20,"bold"),textvariable=Coffee,bd=6,width=8,bg="lightpink")
entry_Cokacola=Entry(f1,font=("aria",20,"bold"),textvariable=Cokacola,bd=6,width=8,bg="lightpink")
entry_Nodules=Entry(f1,font=("aria",20,"bold"),textvariable=Nodules,bd=6,width=8,bg="lightpink")
entry_Biriani=Entry(f1,font=("aria",20,"bold"),textvariable=Biriani,bd=6,width=8,bg="lightpink")
entry_Speed=Entry(f1,font=("aria",20,"bold"),textvariable=Speed,bd=6,width=8,bg="lightpink")
entry_Sandwise=Entry(f1,font=("aria",20,"bold"),textvariable=Sandwise,bd=6,width=8,bg="lightpink")


entry_dosa.grid(row=1,column=1)
entry_Cookies.grid(row=2,column=1)
entry_Coffee.grid(row=3,column=1)
entry_Cokacola.grid(row=4,column=1)
entry_Nodules.grid(row=5,column=1)
entry_Biriani.grid(row=6,column=1)
entry_Speed.grid(row=7,column=1)
entry_Sandwise.grid(row=8,column=1)


#buttons
btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("arial",16,"bold"),width=10,text="Reset",command=Reset)
btn_reset.grid(row=9,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,"bold"),width=10,text="Total",command=Total)
btn_total.grid(row=9,column=1)


root.mainloop()
