from tkinter import *
import random
master = Tk()
master.geometry("700x700")

def temp_counter():
	newrand = random.randint(50 , 100)
	temp_Label.config(text = newrand)
	temp_Label.after(300 , temp_counter)

def Humidity_counter():
	newrand = random.randint(20 , 80)
	Hum_label.config(text = newrand)
	Hum_label.after(300 , Humidity_counter)
	
def openWindow2():
	newWindow2 = Toplevel(master)
	newWindow2.title("TEMPRETURE")
	newWindow2.geometry("500x500")
	newWindow2.configure(bg='LightSalmon')
	photo1 = PhotoImage(file = 'temp.png') 
	lb2 = Label(newWindow2, image = photo1).pack()
	newWindow2.mainloop()
	
def openWindow3():
	newWindow3 = Toplevel(master)
	newWindow3.title("Day")
	newWindow3.configure(bg='LightSalmon')
	newWindow3.geometry("500x500")
	Label(newWindow3).pack()
	photo_day = PhotoImage(file = 'day.png') 
	lb3 = Label(newWindow3, image = photo_day).pack()
	newWindow3.mainloop()

	
def openWindow4(): 
	newWindow4 = Toplevel(master)
	newWindow4.title("Humidity")
	newWindow4.geometry("500x500")
	newWindow4.configure(bg='LightSalmon')
	Label(newWindow4, text ="humidity Mesure").pack()
	photo_humidety = PhotoImage(file = 'humidity.png') 
	lb4 = Label(newWindow4, image = photo_humidety).pack()
	newWindow4.mainloop()


label = Label(master,text ="")
Home_photo = PhotoImage(file = 'home.png') 
lb2 = Label(master, image = Home_photo).pack()
label.pack()

btn1 = Button(master, background="LightSalmon" ,  text = "TEMPRETURE" ,height= 2, width=10 , command = openWindow2)
btn1.place(x=100, y=400) 

btn3 = Button(master , background="LightSalmon"  , text = "Humidity", height= 2, width=10  , command = openWindow4)
btn3.place(x=100, y=470)

btn2 = Button(master, background="LightSalmon" , text = "Day", height= 2, width=50,  command = openWindow3)
btn2.place(x=200, y=540)

temp_Label = Label(master)
temp_Label.pack()
temp_Label.place(x=230, y=405) 
temp_counter()

Hum_label = Label(master)
Hum_label.pack()
Hum_label.place(x=230, y=475) 
Humidity_counter()

mainloop()