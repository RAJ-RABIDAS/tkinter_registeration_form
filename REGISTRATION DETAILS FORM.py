# PROGGRAMED BY: RAJ RABIDAS, CLASS= 12 A

from tkinter import *
import datetime


import csv

           
def view_details():
      f= open("work.csv","r")
      file= csv.reader(f)
      
      for i in file:
            print("%10s | %20s | %20s | %5s | %8s | %5s | % 15s"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))

def save_info():
      e= datetime.datetime.now()
      date= "%s/%s/%s"%(e.day,e.month,e.year)
      time= "%s:%s:%s"%(e.hour,e.minute,e.second)
      name_info= name.get()
      classnm_info= classnm.get()
      
      countrynm_info =countrynm.get()
      rollno_info=rollno.get()
      age_info= age.get()
      print("Registration Done:",name_info,countrynm_info,age_info)
      f= open("work.csv","a",newline="")
      write= csv.writer(f)
      write.writerow([date,name_info,countrynm_info,classnm_info,rollno_info,age_info,time])
      f.close()
            
app= Tk()
app.geometry("600x600")
app.title("data entry")
heading= Label(text="Data Entry Software",fg="black",bg="green",width="500",height="3",font="20")
heading.pack()
name= Label(text="Name:")
countrynm= Label(text= "SCHOOL NAME:")
classnm= Label(text="CLASS:")
rollno= Label(text="ROLL NO:")
age= Label(text="AGE:")

name.place(x=15,y=70)
countrynm.place(x=15,y=140)
classnm.place(x=15,y=210)
rollno.place(x=15,y=280)

age.place(x=15,y=350)


name= StringVar()
countrynm=StringVar()
age = IntVar()
classnm= IntVar()
rollno= IntVar()
      

name_entry= Entry(textvariable=name,width="30")
countrynm_entry= Entry(textvariable=countrynm,width="30")
age_entry= Entry(textvariable=age,width="30")
rollno_entry= Entry(textvariable=rollno,width= "30")
classnm_entry= Entry(textvariable=classnm,width= "30")


name_entry.place(x=15,y=100)
countrynm_entry.place(x=15,y=180)
classnm_entry.place(x=15,y=240)
rollno_entry.place(x=15,y=300)
age_entry.place(x=15,y=370)

button1= Button(app,text="SUBMIT DATA",command=save_info,width= "15",height= "2", bg= "blue")
button2= Button(app,text="EXIT",command=quit,width="15",height="2",bg="red")
button3= Button(app,text="VIEW DATA",command=view_details,height= "2", bg= "grey")
button3.place(x=290,y=430)

button2.place(x=150,y=430)
button1.place(x=15,y=430)
mainloop()
