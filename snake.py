from tkinter import *
from tkinter import messagebox
import random

woot = Tk()
woot.geometry('900x600')
woot.config(bg = '#2F2F2F')

def Open_Game():
	global TitleLbl, StartBut, QuitBut
	TitleLbl.place_forget()
	StartBut.place_forget()
	QuitBut.place_forget()
	Start_Game()

# Defining Needed Variables

TitleLbl = Label(woot, bg = '#2F2F2F',text = 'PYTHON', font = ('Abel',90,'bold'), fg = '#3C8D16')
TitleLbl.place(x = 200,y = 76)

StartBut = Button(woot,bg='green',text='Play game',font=('Abel',20,'bold'),command=Open_Game)
StartBut.place(x=360,y=280)

QuitBut=Button(woot,bg='black',fg='white',text='Quit Game',font=('Abel',20,'bold'),command=woot.destroy)
QuitBut.place(x=360,y=380)

MainCan=Canvas(woot,bg='#353535')

t = 100
x = 20
y = 0
TAILS = []
coords = []
way = 'Right'
rect1 = 0
score = 0
ScoreLbl = Label(woot,bg='black',text='Score  ' + str(score),font=('Abel',20,'bold'),fg='lightgrey')

rect = MainCan.create_rectangle(140,140,160,160,fill='green',outline='#353535')

cololors = ['orange','red','purple','yellow','blue','brown']
food = MainCan.create_rectangle(0,0,0,0,fill=random.choice(cololors))

# Defining Needed Functions

def Food():
	global rect, MainCan, food, cololors
	
	#Generating Food
	wx = random.randint(0,42)
	wy = random.randint(0,25)
	food = MainCan.create_rectangle(wx*20,wy*20,wx*20+20,wy*20+20,fill=random.choice(cololors),outline='#353535')

def Start_Game():
	global rect, MainCan, TAILS, coords, ScoreLbl

	woot.config(bg='black')
	MainCan.place(x=20,y=20,height=520,width=860)
	ScoreLbl.place(x=380,y=550)

	TAILS.append(rect)
	coords.append(MainCan.coords(rect))

	timer()
	Food()

def Grow():
	global rect, t, TAILS, score, ScoreLbl

	#Growing Tails
	rect1 = MainCan.create_rectangle(-40, -20, -40, -20, fill = 'green', outline = '#353535')
	TAILS.append(rect1)
	coords.append(MainCan.coords(rect1))

	# Score and Speed
	score += 1
	ScoreLbl.config(text='Score  ' + str(score),font=('Abel',20,'bold'),fg='lightgrey')
	if (t > 19):
		t -= 1

def timer():
	global x, t, y, rect, food, score, way, TAILS, MainCan, rect1, coords

	MainCan.move(rect,x,y)
	coords[0]=MainCan.coords(rect)

	# Losing
	for i in range(1,len(TAILS)):
		if(coords[0]==coords[i]):
			woot.quit()
			messagebox.showinfo('You Lost!','You lost!\nYour score is ' + str(score))

	# Eating Food
	if(MainCan.coords(rect)==MainCan.coords(food)):
		MainCan.delete(food)
		Food()
		Grow()

	# Tails Following the Snake
	for i in range(1,len(TAILS)):
		MainCan.coords(TAILS[i],coords[i-1][0],coords[i-1][1],coords[i-1][2],coords[i-1][3])
		coords[i-1]=MainCan.coords(TAILS[i-1])

	# Teleportation if Snake is on edge of screen
	if(coords[0][2]>860):
		MainCan.coords(rect,0,coords[0][1],20,coords[0][3])
	elif(coords[0][0]<0):
		MainCan.coords(rect,840,coords[0][1],860,coords[0][3])
	elif(coords[0][3]>520):
		MainCan.coords(rect,coords[0][0],0,coords[0][2],20)
	elif(coords[0][1]<0):
		MainCan.coords(rect,coords[0][0],500,coords[0][2],520)
	
	woot.after(t,timer)

def moveRect(e):
	global x, y, way

	# Direction of Snake
	if(e.keysym=='Up' and way!='Down'):
		x=0
		y=-20
		way='Up'
	if(e.keysym=='Down' and way!='Up'):
		x=0
		y=20
		way='Down'
	if(e.keysym=='Left' and way!='Right'):
		x=-20
		y=0
		way='Left'
	if(e.keysym=='Right' and way!='Left'):
		x=20
		y=0
		way='Right'

woot.bind('<Key>',moveRect)

mainloop()