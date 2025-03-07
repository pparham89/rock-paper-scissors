from tkinter import *
from tkinter import messagebox
import sqlite3
win = Tk()
con = sqlite3.connect('c:/Users/89parham/Documents/contact1.db')
cur=con.cursor()
cur.execute('create table if not exists persons (id integer primary key ,fname txt,lname txt,password txt,course txt )')

def search(password):
    cur.execute('select * from result where fname =?',(password,))
    return cur.fetchall()
def select ():
    d=cur.execute('select * from persons ')
    return d.fetchall()
#========================================
def exit ():
    win.destroy()
def delete ():
    ent_sign.delete(0,END)
    ent_course.delete(0,END)
    ent_family.delete(0,END)
    ent_name.delete(0,END)
    ent_pass.delete(0,END)
def insert ():
    fname=ent_name.get()
    lname=ent_family.get()
    password=ent_pass.get()
    course=ent_course.get()
    cur.execute('insert into persons values (null,?,?,?,?)',(fname,lname,password,course) )
    con.commit()

def show ():
    lst_main.delete(0,END)
    cur.execute('select * from persons ')
    w=cur.fetchall()
    for i in w:
        str(i).split(' ')
        e=(f'{i[0]},{i[1]},{i[2]},{i[3]},{i[4]}')

        lst_main.insert(END,e)
def w ():
    win.destroy()
    win1=Tk()
    lbl=Label(text='welcome')
    lbl.pack()
    win1.mainloop()
def clear ():
    index=lst_main.curselection()
    i=str(lst_main.get(index)).split(',')
    print(i)
    id=int(i[0])
    lst_main.delete(index)
    cur.execute('delete  from persons where id=?  ',(id,))
    con.commit()
def singn ():
    password=int(ent_sign.get())
    selectt=cur.execute('select * from persons where  password=? ',( password, ))
    p=selectt.fetchall()
    for i in p:
        if i !=[]:
            if (i[3])==int(password):
                w()
            else:
                messagebox.showerror('خطا','کاربری با این رمز وجود ندارد')
#========================================
win.geometry("500x350")
win.title("فرم ثبت نام")
win.resizable(0,0)
#========================================

#========================================
lbl_name = Label(win,text="نام:",font="_MRT_khodkar 12 bold")
lbl_name.place(x=40,y=8)

lbl_family = Label(win,text="نام خانوادگی:",font="_MRT_khodkar 12 bold")
lbl_family.place(x=250,y=8)

lbl_course = Label(win,text="نام دوره:",font="_MRT_khodkar 12 bold")
lbl_course.place(x=30,y=68)

lbl_pass = Label(win,text="رمز  ورود:",font="_MRT_khodkar 12 bold")
lbl_pass.place(x=265,y=68)


ent_name = Entry(win)
ent_name.place(x=80,y=20)

ent_family = Entry(win)
ent_family.place(x=330,y=20)

ent_course = Entry(win)
ent_course.place(x=80,y=80)

ent_pass = Entry(win)
ent_pass.place(x=330,y=80)

ent_sign = Entry(win)
ent_sign.place(x=100,y=313,width=300)

lst_main = Listbox(win,height=5,width=77)
lst_main.place(x=20,y=120)


btn_insert = Button(win,text="اضافه کردن",width=10,command=insert)
btn_insert.place(x=45,y=220)

btn_clear = Button(win,text="خالی کردن ورودیها",width=12,command=delete)
btn_clear.place(x=150,y=220)

btn_delete = Button(win,text="حذف کردن",width=10,command=clear)
btn_delete.place(x=255,y=220)

btn_fetch = Button(win,text="ورود به سامانه",width=10,command=singn)
btn_fetch.place(x=360,y=220)

btn_exit = Button(win,text="خروج",width=20,command=exit)
btn_exit.place(x=95,y=260)

btn_show = Button(win,text=" مشاهده همه",width=20,command=show)
btn_show.place(x=255,y=260)

lbl_sign = Label(win,text=":رمز ورود",font="_MRT_khodkar 12 bold")
lbl_sign.place(x=400,y=310)

#================================================

win.mainloop()