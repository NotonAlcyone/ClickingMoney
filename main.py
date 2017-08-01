from tkinter import *
import os

root = Tk()


canvas =  Canvas(root, width = 1280, height = 720)


def reload():

	for i in range(0,len(button)):
		canvas.delete(button[i])


def buttonCall(parameter):
	level[parameter] += 1
	print(str(parameter + 1) + " 번째 버튼이 눌려" + str(level[parameter] ) + " 레벨이 되었습니다.")

	canvas.delete(button[parameter])
	upgradeButton = Button(root,command = lambda i = parameter: buttonCall(parameter),text = str(level[parameter]))
	button[parameter] = canvas.create_window(parameter*100+100,600, window = upgradeButton)


level = []
button = []
def makeButton(num):
	 
	for i in range(0,num):
		upgradeButton = Button(root,command = lambda i = i: buttonCall(i),text = str(level[i]))
		button.append(canvas.create_window(i*100+100,600,window = upgradeButton))


def setButton(num):
	for i in range(0,num):
		level.append(1)
	makeButton(num)

B = Button(root,command = reload,text = "A")
B_window = canvas.create_window(300,300,window = B)
canvas.pack()
setButton(10)
root.mainloop()

