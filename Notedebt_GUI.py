from tkinter import *
import tkinter.messagebox
from tkcalendar import Calendar
import datetime

#window setting
Mywindow = Tk()
Mywindow.title("Note Debet")
Mywindow.geometry("720x576")
timenow = datetime.datetime.now()
#funtion
def SaveNote():
    pass

def showAbout():
    tkinter.messagebox.showinfo("รายระเอียดโปรแกรม","เจ้าของ ธีรศักดิ์ จูมวันทา")

def Exit():
    confirm = tkinter.messagebox.askquestion("ออกโปรแกรม","ต้องการออกโปรแกรมหรือไม่ ? ")
    if confirm == "yes":
        Mywindow.destroy()
def showTime():
    date.config(text="Date is : "+ cal.get_date())    
#Lable
cal = Calendar(Mywindow, selectmode="day", year=timenow.year,month=timenow.month,day=timenow.day)
cal.grid(row=5,column=2)
lable1 = Label(Mywindow,text="Note Dabt",fg="yellow",bg="red",font=40).grid(row=0,column=0)

lable_Name = Label(Mywindow,text="ชื่อ",font=20).grid(row=1,column=1)
Name_text = StringVar()
My_text1 = Entry(Mywindow,textvariable=Name_text).grid(row=2,column=1)

lable_Number = Label(Mywindow,text="จำนวนเงิน",font=20).grid(row=1,column=2)
Price_text = StringVar()
My_text2 = Entry(Mywindow,textvariable=Price_text).grid(row=2,column=2)

lable_Dec = Label(Mywindow,text="คำอธิบาย",font=20).grid(row=3,column=1)
Dec_text = StringVar()
My_text3 = Entry(Mywindow,textvariable=Dec_text).grid(row=4,column=1)

lable_Date = Label(Mywindow,text="วันที่",font=20).grid(row=4,column=2)

date = Label(Mywindow,text="")
date.grid(row=6,column=2)

#Button
btn1 = Button(Mywindow,text="บันทึก",bg="blue",command=SaveNote).grid(row=10,column=1)
btn2 = Button(Mywindow,text="ยืนยัน",bg="red",command=showTime).grid(row=7,column=2)
#menu
menuitem = Menu()
menuitem.add_command(label="save")
menuitem.add_command(label="Exit",command=Exit)
Mymenu = Menu()
Mywindow.config(menu=Mymenu)
Mymenu.add_cascade(label="File",menu=menuitem)
Mymenu.add_cascade(label="About",command=showAbout)

Mywindow.mainloop()