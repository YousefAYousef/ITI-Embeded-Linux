import math
from tkinter import *
import time
from threading import *
from pygame import mixer

running = False
hours=0
minutes=0
seconds = 0
counter_m=0
counter_c=0


board=Tk()
board.title("score board")
board.geometry('380x500')
mixer.init()

def start():
	global running
	if not running:
		update()
		running = True

def update():
	global hours, minutes, seconds
	seconds += 1
	if seconds == 60:
		minutes += 1
		seconds = 0
	if minutes == 60:
		hours += 1
		minutes = 0
		
	if seconds>9:
		seconds_string=str(seconds)
	else:
		seconds_string='0'+str(seconds)
		
	if minutes>9:
		minutes_string=str(minutes)
	else:
		minutes_string='0'+str(minutes)
		
	if hours>9:
		hours_string=str(hours)
	else:
		hours_string='0'+str(hours)
		
	stopwatch_label=Label(board,text=hours_string + ':' + minutes_string + ':' + seconds_string,font=('Arial', 20))
	stopwatch_label.place(x=0,y=0)
	stopwatch_label.after(1000, update)




	
def click_mor():
	global counter_m
	counter_m=counter_m+1
	score_s="cor:"+str(counter_c)+"   mor:" +str(counter_m)
	score=Label(board , text = score_s)
	score.place(x=150,y=300)
	mixer.music.play(loops=0)

def click_cor():
	global counter_c
	counter_c=counter_c+1
	score_s="cor:"+str(counter_c)+"   mor:" +str(counter_m)
	score=Label(board , text = score_s)
	score.place(x=150,y=300)
	mixer.music.play(loops=0)

mor=PhotoImage(file="morroco.png")
cor=PhotoImage(file="croatia.png")

mor=mor.subsample(12,12)
cor=cor.subsample(20,20)

b1=Label(board , text = "Morocoo")
b2=Label(board , text = "Croatia")

mor_1 = Label(board ,image=mor)
cor_1 = Label(board ,image=cor)

mor_b=Button(board , text = "Morocoo",command=click_mor)
cor_b=Button(board , text = "Croatia",command=click_cor)

score_s="cor:"+str(counter_c)+"   mor:" +str(counter_m)
score=Label(board , text = score_s)
score.place(x=150,y=300)

mor_1.place(x=90,y=100)
cor_1.place(x=290,y=100)
b1.place(x=80,y=120)
b2.place(x=280,y=120)
mor_b.place(x=80,y=140)
cor_b.place(x=280,y=140)


stopwatch_label = Label(board,text='00:00:00', font=('Arial', 20))
stopwatch_label.place(x=0,y=0)

start_button = Button(board, text='start', height=1, width=3, command=start)
start_button.place(x=0,y=30)

quit_button = Button(board, text='quit', height=1, width=3, command=board.quit)
quit_button.place(x=30,y=30)


board.mainloop()
	