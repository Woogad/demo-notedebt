from tkinter import *
import tkinter.messagebox
from tkcalendar import Calendar
import datetime
from Updatetoexcel import *

#window setting
Mywindow = Tk()
Mywindow.title("Note Debet")
Mywindow.geometry("720x576")
timenow = datetime.datetime.now()

#funtion
def SaveNote():
    name = Name_text.get()
    price = Price_text.get()
    dec = Dec_text.get()    
    date = cal.get_date()
    pay = ""
    if Pay_status.get() == 1: 
        pay = "จ่ายแล้ว"
    else:
        pay = "ยังไม่จ่าย"

    ex = {"ชื่อ":[name],"คำอธิบาย":[dec],"จำนวนเงิน": [price],"วันที่":[date],"สถานะการจ่าย":[pay]}
    up = Updatetoexcel(ex)
    up.GetToExcelData()
    namein.delete(0,END)
    numberin.delete(0,END)
    decin.delete(0,END)
    Pay_status.set(0)
    Date.config(text="")

def showAbout():
    tkinter.messagebox.showinfo("รายระเอียดโปรแกรม","เจ้าของ ธีรศักดิ์ จูมวันทา")

def Exit():
    confirm = tkinter.messagebox.askquestion("ออกโปรแกรม","ต้องการออกโปรแกรมหรือไม่ ? ")
    if confirm == "yes":
        Mywindow.destroy()
def showTime():
    Date.config(text="Date is : "+ cal.get_date())    

#Lable
cal = Calendar(Mywindow, selectmode="day", year=timenow.year,month=timenow.month,day=timenow.day)
cal.grid(row=5,column=2)
lable1 = Label(Mywindow,text="Note Dabt",fg="yellow",bg="red",font=40).grid(row=0,column=0)

lable_Name = Label(Mywindow,text="ชื่อ",font=20).grid(row=1,column=1)
Name_text = StringVar()
namein = Entry(Mywindow,textvariable=Name_text)
namein.grid(row=2,column=1)

lable_Number = Label(Mywindow,text="จำนวนเงิน",font=20).grid(row=1,column=2)
Price_text = StringVar()
numberin = Entry(Mywindow,textvariable=Price_text)
numberin.grid(row=2,column=2)

lable_Dec = Label(Mywindow,text="คำอธิบาย",font=20).grid(row=3,column=1)
Dec_text = StringVar()
decin = Entry(Mywindow,textvariable=Dec_text)
decin.grid(row=4,column=1)

lable_Date = Label(Mywindow,text="วันที่",font=20).grid(row=4,column=2)

Date = Label(Mywindow,text="")
Date.grid(row=6,column=2)

Pay_status = IntVar()
Pay_status.set(0)

#Button
btn1 = Button(Mywindow,text="บันทึก",bg="blue",command=SaveNote).grid(row=10,column=1)
btn2 = Button(Mywindow,text="ตรวจสอบวัน",bg="red",command=showTime).grid(row=7,column=2)
Radiobutton(text="ยังไม่จ่าย",variable=Pay_status,value=0).grid(row=7,column=3)
Radiobutton(text="จ่ายแล้ว",variable=Pay_status,value=1).grid(row=7,column=4)
#menu
menuitem = Menu()
menuitem.add_command(label="save")
menuitem.add_command(label="Exit",command=Exit)
Mymenu = Menu()
Mywindow.config(menu=Mymenu)
Mymenu.add_cascade(label="File",menu=menuitem)
Mymenu.add_cascade(label="About",command=showAbout)

Mywindow.mainloop()