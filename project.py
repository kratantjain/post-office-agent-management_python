from Tkinter import *
from tkMessageBox import *
import sqlite3
con=sqlite3.Connection("postofficeDB")
cur=con.cursor()
cur.execute('create table if not exists post(accno number(10),accname varchar2(20),denom number(7),mupto number(60),duedate date)')

def po1():
    global po
    po=Tk()
    po.geometry('1024x600')
    po.configure(bg='blue')
    po.title('POAS')
    pic=PhotoImage(file="poas.gif")
    Label(po,image=pic).grid(row=0,column=0,rowspan=10,columnspan=10)
    abt=PhotoImage(file="aboutus.gif")
    cntct=PhotoImage(file="contactus.gif")
    logof=PhotoImage(file="logof.gif")
    adcli=PhotoImage(file="addclient.gif")
    sr=PhotoImage(file="search.gif")
    modi=PhotoImage(file="modify.gif")
    backi=PhotoImage(file="backup.gif")
    Button(po, text="",command=logoff,image=logof,bg='black').grid(row=0, column=4)
    Button(po, text="",command=addclient,image=adcli,bg='black').grid(row=0, column=0)
    Button(po, text="",command=modify,image=modi,bg='black').grid(row=0, column=1)
    Button(po, text="",command=search,image=sr,bg='black').grid(row=0, column=2)
    
    Button(po, text="",command=backup,image=backi,bg='black').grid(row=6, column=2,sticky='S')
    Button(po, text=" ",command=contact,image=cntct,bg='black').grid(row=6, column=0,sticky='S')
    Button(po, text=" ",command=about,image=abt,bg='black').grid(row=6, column=4,sticky='S')
    po.mainloop()
    
def logoff():
    con.commit()
    po.destroy()
    logon()
def backup():
    con.commit()
    showinfo('Backup','Backed up Successfully please re-Login')
    po.destroy()
    logon()
def about():
    po.destroy()
    abt=Tk()
    abt.title("about")
    pic=PhotoImage(file="abg.gif")
    Label(abt,image=pic).grid(row=0,column=0,rowspan=10,columnspan=10)
    me=PhotoImage(file="me.gif")
    sir=PhotoImage(file="sir.gif")
    def me1():
        Label(abt,text='Kratant Jain,Application Developer',bg='red').grid(row=2,column=0)
    def sir1():
        Label(abt,text='Dr. Mahesh Kumar, Advisor',bg='red').grid(row=2,column=4)
    Button(abt,text=' ',command=me1,image=me,bg='black').grid(row=1,column=0)
    Button(abt,text=' ',command=sir1,image=sir,bg='black').grid(row=1,column=4)
    Label(abt,text='POAS Version :-',bg='brown4').grid(row=4,column=2)
    Label(abt,text='0.1',bg='saddle brown').grid(row=4,column=3)
    Label(abt,text='Credit goes  To:-',bg='dark slate gray').grid(row=5,column=0,sticky='W')
    Label(abt,text='Dr. Mahesh Kumar, Kratant Jain, Shubham Verma\n Komal Sodhi, Ankita Agnihotri',bg='pink').grid(row=6,column=0,sticky='E')
    def exitc():
        abt.destroy()
        po1()
    Button(abt,text='close',command=exitc,bg='saddle brown').grid(row=8,column=5)
    abt.mainloop()
def contact():
    po.destroy()
    cont=Tk()
    cont.title('Contact')
    pic=PhotoImage(file="contactbackg.gif")
    Label(cont,image=pic).grid(row=0,column=0,rowspan=10,columnspan=10)
    Label(cont,text='For Any Help Contact Through Given Below Details',bg='yellow green').grid(row=3)
    Label(cont,text='Kratant Jain, Devlopment Manager',bg='yellow green').grid(row=4)
    Label(cont,text='Email :-',bg='yellow green').grid(row=5,column=0)
    Label(cont,text='kratantjain@gmail.com',bg='yellow green').grid(row=5,column=1)
    Label(cont,text='Phone(office)',bg='yellow green').grid(row=6,column=0)
    Label(cont,text='+919760479001',bg='yellow green').grid(row=6,column=1)
    def exitc():
        cont.destroy()
        po1()
    Button(cont,text='close',command=exitc,bg='yellow green').grid(row=7,column=1)
    cont.mainloop()
def search():
    global search
    po.destroy()
    srch=Tk()
    global s
    srch.title('Search')
    srch.configure(bg='red')
    j=PhotoImage(file="j.gif")
    Label(srch,image=j).grid(row=0,column=0,rowspan=10,columnspan=10)
    Label(srch,text='Detail finding  portal',font='Harrington 14 bold',bg='blue').grid(row=1,column=0)
    Label(srch,text='Enter the account no.',font='Harrington 10 bold',bg='blue').grid(row=2,column=0)
    s=Entry(srch,bg='LightCyan4')
    s.grid(row=2,column=1)
    Button(srch, text='ok',font='Harrington 10 bold',command=find,bg='blue').grid(row=3, column=3)
    def exitc():
        srch.destroy()
        po1()
    Button(srch,text='close',font='Harrington 10 bold',command=exitc,bg='blue').grid(row=5,column=1)
    srch.mainloop()
def find():
    k=int(s.get())
    print k
    global a
    cur.execute('select * from post where accno=(?)',(k,))
    a=cur.fetchone()
    print a
    amount=str(int(a[2])*int(a[3]))
    print amount
    showinfo('Info',message='Account no. - '+str(a[0])+'\nAccount name - '+ a[1] +'\nDenomination - '+str(a[2])+'\nTotal amount paid - '+amount+'\nDue date - '+a[4])
    
def modify():
    global s
    global modify
    po.destroy()
    modify=Tk()
    modify.title('Modify')
    pic=PhotoImage(file="modif.gif")
    Label(modify,image=pic).grid(row=0,column=0,rowspan=14,columnspan=10)
    Label(modify,text='Modification portal',font='Harrington 14 bold',bg='dark olive green').grid(row=0)
    Label(modify,text='Enter the account no.',font='Harrington 10 bold',bg='dark olive green').grid(row=1,column=0)
    s=Entry(modify,bg='orange2')
    s.grid(row=1,column=1)
    Button(modify, text='check',font='Harrington 10 bold',command=find,bg='dark olive green').grid(row=2, column=3)
    v=IntVar()
    Label(modify,text='Select the one which u wanna modify',font='Harrington 10 bold',bg='dark olive green').grid(row=3,column=0)
    Radiobutton(modify,text='Account no',font='Harrington 10 bold',variable=v,value=1,bg='dark olive green').grid(row=4,column=1)
    Radiobutton(modify,text='Account name',font='Harrington 10 bold',variable=v,value=2,bg='dark olive green').grid(row=5,column=1)
    Radiobutton(modify,text='Denomination',font='Harrington 10 bold',variable=v,value=3,bg='dark olive green').grid(row=6,column=1)
    Radiobutton(modify,text='Months Paid upto',font='Harrington 10 bold',variable=v,value=4,bg='dark olive green').grid(row=7,column=1)
    Radiobutton(modify,text='Next Installment Due',font='Harrington 10 bold',variable=v,value=5,bg='dark olive green').grid(row=8,column=1)

    def update():
        global l
        if v.get()==1:
            Label(modify,text='Enter the account no. to which u wanna modify- ',font='Harrington 10 bold',bg='dark sea green').grid(row=10,column=0,sticky='EW')
            m='acno'
            l=Entry(modify)
            l.grid(row=10,column=1)
        if v.get()==2:
            Label(modify,text='Enter the account name to which u wanna modify- ',font='Harrington 10 bold',bg='dark sea green').grid(row=10,column=0,sticky='EW')
            l=Entry(modify)
            l.grid(row=10,column=1)

        if v.get()==3:
            Label(modify,text='Enter the denomination to which u wanna modify- ',font='Harrington 10 bold',bg='dark sea green').grid(row=10,column=0,sticky='EW')
            l=Entry(modify)
            l.grid(row=10,column=1)

        if v.get()==4:
            Label(modify,text='Enter the months paid upto to which u wanna modify- ',bg='dark sea green').grid(row=10,column=0,sticky='EW')
            l=Entry(modify)
            l.grid(row=10,column=1)

        if v.get()==5:
            Label(modify,text='Enter the next due date to which u wanna modify- ',font='Harrington 10 bold',bg='dark sea green').grid(row=10,column=0,sticky='EW')
            l=Entry(modify)
            l.grid(row=10,column=1)
    def done():
        if v.get()==1:
            m=(int(l.get()),a[0])
            print m
            cur.execute('update post set accno =(?) where accno=(?)',m)
            con.commit()
            showinfo(title='Modify Result',message='Modification Successful')
        if v.get()==2:
            m=(str(l.get()),a[0])
            print m
            cur.execute('update post set accname =(?) where accno=(?)',m)
            showinfo(title='Modify Result',message='Modification Successful')
            con.commit()
        if v.get()==3:
            m=(int(l.get()),a[0])
            print m
            cur.execute('update post set denom =(?) where accno=(?)',m)
            showinfo(title='Modify Result',message='Modification Successful')
            con.commit()

        if v.get()==4:
            m=(int(l.get()),a[0])
            print m
            cur.execute('update post set mupto =(?) where accno=(?)',m)
            showinfo(title='Modify Result',message='Modification Successful')
            con.commit()
        if v.get()==5:
            m=(str(l.get()),a[0])
            print m
            cur.execute('update post set duedate =(?) where accno=(?)',m)
            showinfo(title='Modify Result',message='Modification Successful')
            con.commit()
    Button(modify,text='Done',font='Harrington 10 bold',command=done,bg='sienna3').grid(row=11,column=1)       
    Button(modify,text='Next',font='Harrington 10 bold',command=update,bg='sienna3').grid(row=9,column=1)
    def exitc():
        modify.destroy()
        po1()
    Button(modify,text='close',font='Harrington 10 bold',command=exitc,bg='DarkOrange1').grid(row=12,column=2)
    modify.mainloop()
	

def addclient():
    global insert
    po.destroy()
    insert=Tk()
    pic=PhotoImage(file="add.gif")
    Label(insert,image=pic).grid(row=0,column=0,rowspan=10,columnspan=10)
    insert.title('Insert Details Of Client')
    Label(insert,text='Account No. ',bg='dodger blue').grid(row=0,column=0, sticky='w')
    acno=Entry(insert,bg='dodger blue')
    acno.grid(row=0,column=1)
    Label(insert,text='Account Name ',bg='dodger blue').grid(row=1,column=0, sticky='w')
    acname=Entry(insert,bg='dodger blue')
    acname.grid(row=1,column=1)
    Label(insert,text='Denomination ',bg='dodger blue').grid(row=2,column=0, sticky='w')
    denom=Entry(insert,bg='dodger blue')
    denom.grid(row=2,column=1)
    Label(insert,text='Months Paid Upto',bg='dodger blue').grid(row=3,column=0, sticky='w')
    mpo=Entry(insert,bg='dodger blue')
    mpo.grid(row=3,column=1)
    Label(insert,text='Next RD Installment Due Date',bg='dodger blue').grid(row=4,column=0, sticky='w')
    duedate=Entry(insert,bg='dodger blue')
    duedate.grid(row=4,column=1)
    def done():
          tup=(int(acno.get()),str(acname.get()),int(denom.get()),int(mpo.get()),str(duedate.get()))
          cur.execute('insert into post values(?,?,?,?,?)',tup)
          con.commit()
          showinfo('Inserted Record',tup)
          insert.destroy()
          po1()
    Button(insert,text='DONE',command=done,bg='dodger blue').grid(row=5,column=2)
    def exitc():
        insert.destroy()
        po1()
    Button(insert,text='close',command=exitc,bg='dodger blue').grid(row=5,column=0)
    
    insert.mainloop()
def paswrd_checker():
    if pswrd.get()=='kratant':
        login.destroy()
        po1()
    else:
        showerror('Error','Wrong Credential')

def logon():
    global pswrd
    global login
    login=Tk()
    login.title('POAS Login')
    login.geometry('1024x600')
    pic=PhotoImage(file="kj.gif")
    pic1=Label(login,image=pic)
    pic1.grid(row=0,column=0,rowspan=10,columnspan=10)
    Button(login,text='  close  ',bg='red',command=login.destroy).grid(row=0,column=2,sticky='E')
    Label(login,text='KRATANT JAIN',font='Harrington 15 bold',bd=12,bg='red').grid(row=0,column=0,sticky='W')
    Label(login,text='151308',font='Harrington 15 bold',bd=12,bg='red').grid(row=1,column=0,sticky='W')
    Label(login,text='B3',font='Harrington 15 bold',bd=12,bg='red').grid(row=2,column=0,sticky='W')
    Label(login,text='CSE',font='Harrington 15 bold',bd=12,bg='red').grid(row=3,column=0,sticky='W')
    Label(login,text='kratantjain@gmail.com',font='Harrington 15 bold',bd=12,bg='red').grid(row=4,column=0,sticky='W')
    Button(login,text='Login',command=paswrd_checker,font='Harrington 20 bold',bd=10,bg='red').grid(row=5,column=5,sticky=E+W+N+S,columnspan=3)
    pswrd=Entry(show='*',bg='red')
    pswrd.grid(row=8,column=5,sticky=E+W+N+S,columnspan=3,rowspan=1)
    login.mainloop()

logon()
