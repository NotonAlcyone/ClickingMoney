from tkinter import *
import os

root = Tk()


canvas =  Canvas(root, width = 1280, height = 720)


def reload():

	for i in range(0,len(button)):
		canvas.delete(button[i])


def buttonCall(parameter):
	print(str(parameter + 1) + " 번째 버튼이 눌림")

button = []
def makeButton(num):
	 
	for i in range(0,num):
		upgradeButton = Button(root,command = lambda i = i: buttonCall(i),text = "A")
		button.append(canvas.create_window(i*100+100,600,window = upgradeButton))




B = Button(root,command = reload,text = "A")
B_window = canvas.create_window(300,300,window = B)
canvas.pack()
makeButton(10)
root.mainloop()

