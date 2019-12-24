from tkinter import *
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import os
root=Tk()
def tri():
    f=first.get().upper()
    l=last.get().upper()
    br=var.get().upper()
    ad=aadhr.get()
    co=cours.get().upper()
    p=password.get()
    ft=father.get().upper()
    mo=mother.get().upper()
    import mysql.connector
    obj=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="college")
    c=obj.cursor()
    a="INSERT INTO admin(first_name,last_name,aadhar,course,branch,password,father_name,mother_name) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    b=(f,l,ad,co,br,p,ft,mo)
    c.execute(a,b)
    x="SELECT id FROM admin WHERE aadhar={}".format(ad)
    c.execute(x)
    y=c.fetchall()
    for i in y:
        Label(top,text="YOUR GENERATED STUDENT ROLL NO. IS!!",font=("callibri",15)).grid(row=8,column=1000)
        Label(top,text=i,font=("callibri",15)).grid(row=9,column=1000)
    obj.commit()

def clearfun():
    first.set("")
    last.set("")
    password.set("")
    aadhr.set("0")
    father.set("")
    mother.set("")
    cours.set("")

def fun():
    global top
    top=Toplevel()
    top.geometry("1366x768")
    top.title("New Account")
    top.focus_force()
    global first
    global last
    global var
    global aadhr
    global cours
    global password
    global father
    global mother
    father=StringVar()
    mother=StringVar()
    cours=StringVar()
    var = StringVar()
    var.set("BRANCH")
    aadhr=IntVar(top)
    first=StringVar() # in gui programming we use StringVar for holding a string value. similarly, IntVar(), DoubleVar(),BooleanVar() are used.
    last=StringVar()
    password=StringVar()
    Label(top,text="FIRST NAME",font=("callibri",15)).grid(row=0,column=1000)
    Button(top,text="BACK",command=call).grid(row=1,column=1002,sticky=E,padx=500)
    Entry(top,textvariable=first).grid(row=0,column=1001)
    Label(top,text="LAST NAME",font=("callibri",15)).grid(row=1,column=1000)
    Entry(top,textvariable=last).grid(row=1,column=1001)
    Label(top,text="AADHAR CARD",font=("callibri",15)).grid(row=2,column=1000)
    e1=Entry(top,textvariable=aadhr)
    e1.grid(row=2,column=1001)
    Label(top,text="COURSE",font=("callibri",15)).grid(row=3,column=1000)
    Entry(top,textvariable=cours).grid(row=3,column=1001)
    option = OptionMenu(top, var, "C.S/I.T", "MECH", "ELECTRICAL", "CIVIL")
    option.grid(row=4,column=1001)
    Label(top,text="FATHER'S NAME",font=("callibri",15)).grid(row=5,column=1000)
    Entry(top,textvariable=father).grid(row=5,column=1001)
    Label(top,text="MOTHER'S NAME",font=("callibri",15)).grid(row=6,column=1000)
    Entry(top,textvariable=mother).grid(row=6,column=1001)
    Label(top,text="SET PASSWORD",font=("callibri",15)).grid(row=7,column=1000)
    Entry(top,textvariable=password).grid(row=7,column=1001)
    Label(top,text="** 8 CHARACTERS ONLY",font=("callibri",15)).grid(row=7,column=1002)
    Button(top,text="SUBMIT",command=tri).grid(row=8,column=1000)
    Button(top,text="RESET",command=clearfun).grid(row=8,column=1001)
def sub():
    sem1=sem.get()
    if(sem1==3):
        Label(page,text="SUBJECTS:",font=("callibri",15,"underline")).grid(row=16,column=1,sticky=W)
        Label(page,text="Mathematics(M 301)",font=("callibri",15)).grid(row=17,column=1,sticky=W)
        Label(page,text="Data Structure And Algorithms(CS 302)",font=("callibri",15)).grid(row=18,column=1,sticky=W)
        Label(page,text="Circut Theory And Networks(EE 301)",font=("callibri",15)).grid(row=19,column=1,sticky=W)
        Label(page,text="Computer Organisation(CS 303)",font=("callibri",15)).grid(row=20,column=1,sticky=W)
        Label(page,text="Digital Electronics And Logic Design(EC 312)",font=("callibri",15)).grid(row=21,column=1,sticky=W)
        Label(page,text="Principles Of Programming Language(CS 301)",font=("callibri",15)).grid(row=22,column=1,sticky=W)
        Label(page,text="PRACTICALS:",font=("callibri",15,"underline")).grid(row=16,column=3,sticky=W)
        Label(page,text="Data Structure Lab(CS 392)",font=("callibri",15)).grid(row=17,column=3,sticky=W)
        Label(page,text="Digital Electronics And Logic Design(EC 382)",font=("callibri",15)).grid(row=18,column=3,sticky=W)
        Label(page,text="Lab(CS 391)",font=("callibri",15)).grid(row=19,column=3,sticky=W)
        Label(page,text="Programming Practice Lab(EE 391)",font=("callibri",15)).grid(row=20,column=3,sticky=W)
    else:
        Label(page,text="WRONG SEM ENTERED",font=("callibri",15)).grid(row=16,column=1,sticky=W)
def analyse():
    pp=pwd.get()
    import mysql.connector
    obj=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="college")
    c=obj.cursor()
    mysl="SELECT * FROM admin WHERE id='{}' ".format(pp)
    c.execute(mysl)
    ans=c.fetchall()
    for k in ans:
        Label(page,text=k[1],font=("callibri",15)).grid(row=3,column=2,sticky=W)
        Label(page,text=k[2],font=("callibri",15)).grid(row=4,column=2,sticky=W)
        Label(page,text=k[7],font=("callibri",15)).grid(row=5,column=2,sticky=W)
        Label(page,text=k[8],font=("callibri",15)).grid(row=6,column=2,sticky=W)
        Label(page,text=k[3],font=("callibri",15)).grid(row=7,column=2,sticky=W)
        Label(page,text=k[4],font=("callibri",15)).grid(row=8,column=2,sticky=W)
        Label(page,text=k[5],font=("callibri",15)).grid(row=9,column=2,sticky=W)
    Label(page,text="Enter semester",font=("callibri",15)).grid(row=15,column=1,sticky=W,pady=50)
    global sem
    sem=IntVar()
    Entry(page,textvariable=sem).grid(row=15,column=2)
    Button(page,text="ENTER",command=sub).grid(row=15,column=3)
def perform():
    p2=pwd.get()
    page1=Toplevel()
    page1.geometry("1366x768")
    page1.title("Student analysis")
    Label(page1,text="STUDENT ANALYSIS BASED ON THEIR PERFORMANCE",font=("forte",20,"underline")).grid(row=1,column=1,columnspan=2,sticky=NSEW)
    Button(page1,text="BACK",command=match).grid(row=1,column=5,stick=E)
    Label(page1,text="INTERNALS:",font=("algerian",18,"underline")).grid(row=3,column=1,sticky=NSEW,columnspan=5)
    Label(page1,text="SUBJECTS:-",font=("callibri",15,"underline")).grid(row=4,column=1,sticky=W)
    Label(page1,text="Mathematics(M 301):",font=("callibri",15)).grid(row=5,column=1,sticky=W)
    Label(page1,text="Data Structure And Algorithms(CS 302):",font=("callibri",15)).grid(row=6,column=1,sticky=W)
    Label(page1,text="Circut Theory And Networks(EE 301):",font=("callibri",15)).grid(row=7,column=1,sticky=W)
    Label(page1,text="Computer Organisation(CS 303):",font=("callibri",15)).grid(row=8,column=1,sticky=W)
    Label(page1,text="Digital Electronics And Logic Design(EC 312):",font=("callibri",15)).grid(row=9,column=1,sticky=W)
    Label(page1,text="Principles Of Programming Language(CS 301):",font=("callibri",15)).grid(row=10,column=1,sticky=W)
    Label(page1,text="PRACTICALS:-",font=("callibri",15,"underline")).grid(row=4,column=3,sticky=W)
    Label(page1,text="Data Structure Lab(CS 392):",font=("callibri",15)).grid(row=5,column=3,sticky=W)
    Label(page1,text="Digital Electronics And Logic Design(EC 382):",font=("callibri",15)).grid(row=6,column=3,sticky=W)
    Label(page1,text="Lab(CS 391):",font=("callibri",15)).grid(row=7,column=3,sticky=W)
    Label(page1,text="Programming Practice Lab(EE 391):",font=("callibri",15)).grid(row=8,column=3,sticky=W)
    import mysql.connector
    obj2=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="college")
    c2=obj2.cursor()
    sql2="SELECT * FROM marks WHERE roll_no='{}' ".format(p2)
    c2.execute(sql2)
    y2=c2.fetchall()
    e=[]
    for l in y2:
        Label(page1,text=l[1],font=("callibri",15)).grid(row=5,column=2,sticky=W)
        Label(page1,text=l[2],font=("callibri",15)).grid(row=6,column=2,sticky=W)
        Label(page1,text=l[3],font=("callibri",15)).grid(row=7,column=2,sticky=W)
        Label(page1,text=l[4],font=("callibri",15)).grid(row=8,column=2,sticky=W)
        Label(page1,text=l[5],font=("callibri",15)).grid(row=9,column=2,sticky=W)
        Label(page1,text=l[6],font=("callibri",15)).grid(row=10,column=2,sticky=W)
        Label(page1,text=l[7],font=("callibri",15)).grid(row=5,column=5,sticky=W)
        Label(page1,text=l[8],font=("callibri",15)).grid(row=6,column=5,sticky=W)
        Label(page1,text=l[9],font=("callibri",15)).grid(row=7,column=5,sticky=W)
        Label(page1,text=l[10],font=("callibri",15)).grid(row=8,column=5,sticky=W)
        i=1
        while(i<=6):
            e.append(l[i])
            i+=1
        f=plt.Figure(figsize=(3,3), dpi=100)
        a=f.add_subplot(111)
        bar1=FigureCanvasTkAgg(f,page1)
        bar1.get_tk_widget().grid(row=17,column=1)
        a.plot(e)
    z=[]
    j=7
    for m in y2:
        while(j<=10):
            z.append(m[j])
            j+=1
    f1=plt.Figure(figsize=(3,3), dpi=100)
    a1=f1.add_subplot(111)
    bar2=FigureCanvasTkAgg(f1,page1)
    bar2.get_tk_widget().grid(row=17,column=3)
    a1.plot(z)

  
def match():
    r=roll.get()
    pw=passwd.get()
    import mysql.connector
    obj1=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="college")
    c1=obj1.cursor()
    sql1="SELECT id,password FROM admin WHERE id='{}' or password='{}' ".format(r,pw)
    c1.execute(sql1)
    y1=c1.fetchall()
    for j in y1:
        if(j[0]==r and j[1]==pw):
            global page
            global pwd
            pwd=IntVar()
            page=Toplevel()
            page.geometry("1366x768")
            page.title("Student detail")
            Label(page,text="STUDENT DETAILS",font=("forte",20,"underline")).grid(row=1,column=1,sticky=NSEW,columnspan=3)
            Button(page,text="BACK",relief=RAISED,command=call).grid(row=1,column=6,sticky=E,padx=50)
            Button(page,text="NEXT PAGE",relief=RAISED,command=perform).grid(row=1,column=6,sticky=E,padx=100)
            Label(page,text="Enter Student Roll No.",font=("callibri",15)).grid(row=2,column=1,sticky=W)
            Entry(page,textvariable=pwd).grid(row=2,column=2)
            Button(page,text="ENTER",command=analyse).grid(row=2,column=3)
            Label(page,text="First_name:",font=("callibri",15)).grid(row=3,column=1,sticky=W)
            Label(page,text="Last_name:",font=("callibri",15)).grid(row=4,column=1,sticky=W)
            Label(page,text="Father's name:",font=("callibri",15)).grid(row=5,column=1,sticky=W)
            Label(page,text="Mother's name:",font=("callibri",15)).grid(row=6,column=1,sticky=W)
            Label(page,text="Aadhar card:",font=("callibri",15)).grid(row=7,column=1,sticky=W)
            Label(page,text="Course:",font=("callibri",15)).grid(row=8,column=1,sticky=W)
            Label(page,text="Branch:",font=("callibri",15)).grid(row=9,column=1,sticky=W)
        else:
            Label(level,text="Incorrect Id or Password.. Please enter again!!",font=("callibri",15)).grid(row=670,column=1000)

def updation():
             r_no=rollno.get()
             M=maths.get()
             D=ds.get()
             N=net.get()
             CO=coa.get()
             DL=dld.get()
             PP=ppl.get()
             DS_LAB=ds_lab.get()
             DLD_LAB=dld_lab.get()
             L=lab.get()
             P_LAB=p_lab.get()
             import mysql.connector
             obj=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="college")
             c=obj.cursor()
             a="INSERT INTO marks VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
             b=(r_no,M,D,N,CO,DL,PP,DS_LAB,DLD_LAB,L,P_LAB)
             c.execute(a,b)
             obj.commit()

                   
def clearr():
    rollno.set("0")
    maths.set("0")
    ds.set("0")
    net.set("0")
    coa.set("0")
    dld.set("0")
    ppl.set("0")
    ds_lab.set("0")
    dld_lab.set("0")
    lab.set("0")
    p_lab.set("0")

def match2():
    t_id=teacher_id.get()
    t_pwd=teacher_pwd.get()
    import mysql.connector
    obj1=mysql.connector.connect(host="localhost",user="root",passwd="tanya1703",database="college")
    c1=obj1.cursor()
    sql1="SELECT id,password FROM teacher WHERE id='{}' or password='{}' ".format(t_id,t_pwd)
    c1.execute(sql1)
    y1=c1.fetchall()
    for j in y1:
        if(j[0]==t_id and j[1]==t_pwd):
             global t_page
             t_page=Toplevel()
             t_page.geometry("1366x768")
             t_page.title("MARKS UPDATION")
             global rollno
             rollno=IntVar()
             Label(t_page,text="MARKS UPDATION(BY TEACHERS ONLY)",font=("algerian",20,"underline")).grid(row=0,column=0,columnspan=2,sticky=NSEW)
             Label(t_page,text="ENTER STUDENT ROLL NO. FOR ENTERING MARKS:",font=("callibri",12)).grid(row=2,column=0,pady=20,sticky=W)
             Entry(t_page,textvariable=rollno).grid(row=2,column=1,sticky=W)
             global maths
             global ds
             global net
             global coa
             global dld
             global ppl
             global ds_lab
             global dld_lab
             global lab
             global p_lab
             maths=IntVar()
             ds=IntVar()
             net=IntVar()
             coa=IntVar()
             dld=IntVar()
             ppl=IntVar()
             ds_lab=IntVar()
             dld_lab=IntVar()
             lab=IntVar()
             p_lab=IntVar()
             Label(t_page,text="SUBJECTS:-",font=("callibri",15,"underline")).grid(row=4,column=0,sticky=W)
             Label(t_page,text="Mathematics(M 301):",font=("callibri",15)).grid(row=5,column=0,sticky=W)
             Label(t_page,text="Data Structure And Algorithms(CS 302):",font=("callibri",15)).grid(row=6,column=0,sticky=W)
             Label(t_page,text="Circut Theory And Networks(EE 301):",font=("callibri",15)).grid(row=7,column=0,sticky=W)
             Label(t_page,text="Computer Organisation(CS 303):",font=("callibri",15)).grid(row=8,column=0,sticky=W)
             Label(t_page,text="Digital Electronics And Logic Design(EC 312):",font=("callibri",15)).grid(row=9,column=0,sticky=W)
             Label(t_page,text="Principles Of Programming Language(CS 301):",font=("callibri",15)).grid(row=10,column=0,sticky=W)
             Label(t_page,text="PRACTICALS:",font=("callibri",15,"underline")).grid(row=11,column=0,sticky=W,pady=20)
             Label(t_page,text="Data Structure Lab(CS 392):",font=("callibri",15)).grid(row=12,column=0,sticky=W)
             Label(t_page,text="Digital Electronics And Logic Design(EC 382):",font=("callibri",15)).grid(row=13,column=0,sticky=W)
             Label(t_page,text="Lab(CS 391):",font=("callibri",15)).grid(row=14,column=0,sticky=W)
             Label(t_page,text="Programming Practice Lab(EE 391):",font=("callibri",15)).grid(row=15,column=0,sticky=W)
             Entry(t_page,textvariable=maths).grid(row=5,column=1,sticky=W)
             Entry(t_page,textvariable=ds).grid(row=6,column=1,sticky=W)
             Entry(t_page,textvariable=net).grid(row=7,column=1,sticky=W)
             Entry(t_page,textvariable=coa).grid(row=8,column=1,sticky=W)
             Entry(t_page,textvariable=dld).grid(row=9,column=1,sticky=W)
             Entry(t_page,textvariable=ppl).grid(row=10,column=1,sticky=W)
             Entry(t_page,textvariable=ds_lab).grid(row=12,column=1,sticky=W)
             Entry(t_page,textvariable=dld_lab).grid(row=13,column=1,sticky=W)
             Entry(t_page,textvariable=lab).grid(row=14,column=1,sticky=W)
             Entry(t_page,textvariable=p_lab).grid(row=15,column=1,sticky=W)
             Button(t_page,text="SUBMIT",command=updation).grid(row=16,column=0,columnspan=2,pady=20)
             Button(t_page,text="RESET",command=clearr).grid(row=16,column=1,columnspan=2)
             Button(t_page,text="NEXT PAGE",command=match).grid(row=16,column=2,columnspan=2)
             
        else:
              Label(level,text="Incorrect Id or Password.. Please enter again!!",font=("callibri",15)).grid(row=670,column=1000)

def clear():
    roll.set("0")
    passwd.set("")
    teacher_id.set("0")
    teacher_pwd.set("")

def call():
    global roll
    global passwd
    global teacher_id
    global teacher_pwd
    global level
    roll=IntVar()
    passwd=StringVar()
    teacher_id=IntVar()
    teacher_pwd=StringVar()
    level=Toplevel()
    level.geometry("1366x768")
    level.title("login page")
    Label(level,text="LOGIN PAGE",font=("callibri",20,"underline")).grid(row=0,column=3,columnspan=6,sticky=NSEW,pady=20)
    Label(level,text="STUDENT ROLLNO.",font=("callibri",15)).grid(row=1,column=0) #side attribute is working using tkinter
    Entry(level,textvariable=roll).grid(row=1,column=1)
    Label(level,text="PASSWORD",font=("callibri",15)).grid(row=2,column=0)
    Entry(level,textvariable=passwd,show="*").grid(row=2,column=1)
    Label(level,text="TEACHER ID",font=("callibri",15)).grid(row=1,column=5)
    Entry(level,textvariable=teacher_id).grid(row=1,column=6)
    Label(level,text="PASSWORD",font=("callibri",15)).grid(row=2,column=5)
    Entry(level,textvariable=teacher_pwd,show="*").grid(row=2,column=6)
    Button(level,text="SUBMIT",command=match).grid(row=3,column=1,columnspan=2)
    Button(level,text="RESET",command=clear).grid(row=3,column=2,columnspan=2)
    Button(level,text="SUBMIT",command=match2).grid(row=3,column=5,columnspan=6)
    Button(level,text="RESET",command=clear).grid(row=3,column=6,columnspan=6)
    l1=Label(level,text="Create new Account, if dont have any!!",font=("callibri",15,"underline"))
    l1.grid(row=4,column=0)
    l1.bind("<Button-1>",lambda t:fun())
root.geometry("1366x768")
Label(root,text="WELCOME",fg="blue",font=("forte",24,"underline")).pack()
img = ImageTk.PhotoImage(Image.open("acet.jpg"))
panel = Label(root, image = img)
panel.pack()
Label(root,text="ALIGARH COLLEGE OF ENGINEERING AND TECHNOLOGY",fg="blue",font=("forte",24)).pack(pady=40)
Label(root,text="ENTER TO LOGIN!!",font=("forte",20)).pack()
b1=Button(root,text="ENTER",height=1,width=10,bg="light grey",command=call)
b1.pack()
root.mainloop()
