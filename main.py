from tkinter import *
import os
import json

imagePath = {}
canvasSizeX = 1280
canvasSizeY = 720
totalButtonNum = 10
buttonSpace = 95
resourceY = 30
goldX = 100
crystalX = 200

imageFolder = "Resources/"
root = Tk()
canvas =  Canvas(root, width = canvasSizeX, height = 720)


def imageLoader(path):
	if path in imagePath:
		return imagePath[path]
	else:
		imagePath[path] = PhotoImage(file = imageFolder + path)
		return imagePath[path]

def reload():
	for i in range(0,len(button)):
		canvas.delete(button[i])

def buyCall(parameter):
	global crystal
	payAmount = 100
	if crystal >= payAmount:
		buttonCrystal[parameter] = True
		print("구매가 완료되었습니다!")
		crystal -= payAmount
		crystalRefresh()
		canvas.delete(button[parameter])
		buttonPrint(parameter)
	else:
		print("크리스탈이 없어요!")

def buttonCall(parameter):
	global gold

	payAmount = level[parameter] * 10 # 지불가격
	if gold >= payAmount:
		level[parameter] += 1
		print(str(parameter + 1) + " 번째 버튼이 눌려" + str(level[parameter] ) + " 레벨이 되었습니다.")
		gold -= payAmount
		goldRefresh()
		canvas.delete(button[parameter])
		buttonPrint(parameter)
	else:
		print("돈이 부족해요")

level = []
button = []
buttonCrystal = []
def makeButton(num):
	 for i in range(0,num):
	 	buttonPrint(i)

def buttonPrint(num):
	buttonPoint = canvasSizeX / (totalButtonNum+1)
	buttonYPos = num * buttonPoint + buttonPoint
	if buttonCrystal[num] == True :
		upgradeButton = Button(root,compound = CENTER, command = lambda i = num: buttonCall(num),text = str(level[num]) + "레벨\n"+str(level[num]*10) +"G",image = imageLoader("button3.png"),relief=FLAT)

	else:
		upgradeButton = Button(root,compound = CENTER, command = lambda i = num: buyCall(num),image = imageLoader("buying button2.png"),relief=FLAT )
	if num  < totalButtonNum/2:
		buttonXPos = canvasSizeX - 400
		button.append(canvas.create_window(buttonXPos, buttonYPos,window = upgradeButton))

	else:
		buttonXPos = canvasSizeX - 200
		buttonYPos = (num- totalButtonNum/2 )*buttonPoint + buttonPoint
		button.append(canvas.create_window(buttonXPos, buttonYPos,window = upgradeButton))
		

def saver():
	global crystal
	global gold
	global level
	global buttonCrystal	
	file = open("save.txt","w+")
	savelist = [str(crystal)+"\n"+str(gold)+"\n"+str(level)+"\n"+str(buttonCrystal)+"\n"+str(char)]
	file.writelines(savelist)
	file.close()
def loader():
	global crystal
	global gold
	global level
	global buttonCrystal
	global char
	if os.path.isfile("save.txt"):
		file = open("save.txt","r")
		data = file.readlines()
		crystal = int(data[0])
		gold = int(data[1])
		level = eval(data[2])
		buttonCrystal = eval (data[3])
		if str(data[4]) == "True":
			char = True
		else:
			char = False
		global startButton
		canvas.delete(startButton[0])
		canvas.delete(startButton[1])
		
		goldSystem()
		crystalRefresh()
		makeButton(totalButtonNum)
		uiBuild()

def setButton(num):
	for i in range(0,num):
		level.append(1) #시작레벨은 1
		if i > 4:
			buttonCrystal.append(False)
		else :
			buttonCrystal.append(True)
	makeButton(num)


gold = 0
goldText = None
def goldSystem():
	global gold
	tmp = goldAmount()
	gold += tmp
	goldRefresh()
	canvas.after(1000,goldSystem)
	print("현 골드는 " + str(gold) + " 입니다")

def goldAmount():
	goldUp = 10
	for i in range(0,len(level)):
		goldUp += level[i]
	return goldUp

def goldRefresh():
	global goldText
	global gold
	if goldText != None:
		canvas.delete(goldText)
	goldText = canvas.create_text(goldX, resourceY, text = gold)

crystal = 0
crystalText = None
def crystalSystem(stat):
	global crystal
	if stat == "PTW":
		crystal = 1000 #과금러
	elif stat == "FTW":
		crystal = 0 #무과금
	crystalRefresh()

def crystalRefresh():
	global crystal
	global crystalText

	if crystalText != None:
		canvas.delete(crystalText)
	crystalText = canvas.create_text(crystalX,resourceY, text = str(crystal))


char = False
def charBuy():
	global crystal
	global charButton
	global char
	global total
	if crystal >= 500 and char == False:
		char = True
		crystal -= 500
		crystalRefresh()
		canvas.delete(charButton)
		canvas.delete(total)
		total = canvas.create_image(400,500,image = imageLoader("f178.png"))
	else:
		print("out of crystal")

def uiBuild():
	global charButton
	global total
	global char
	if char == False:
		total = canvas.create_image(400,500,image = imageLoader("f177.png"))
		button = Button(root,command = charBuy,text = "캐릭터 구매")
		charButton = canvas.create_window(150,150,window = button)
	elif char == True:
		total = canvas.create_image(400,500,image = imageLoader("f178.png"))

	canvas.create_image(canvasSizeX/2,29,image = imageLoader("upperbar.png"))
	canvas.create_image(crystalX - 40,resourceY, image = imageLoader("diamond.png"))
	canvas.create_image(goldX  - 50,resourceY, image =  imageLoader("gold.png"))
	button2 = Button(root,command = saver,text = "저장")
	canvas.create_window(500,150,window = button2)	



startButton = []
def gameSet(mode):
	global startButton
	canvas.delete(startButton[0])
	canvas.delete(startButton[1])

	uiBuild()
	setButton(totalButtonNum)
	goldSystem()
	crystalSystem(mode)


def mainScene():
	button = Button(root,compound = CENTER, command = lambda:gameSet("PTW"),text = "유과금")
	button2 = Button(root,compound = CENTER, command = lambda:gameSet("FTW"),text= "무과금")
	startButton.append(canvas.create_window((canvasSizeX/2)-100, canvasSizeY/2,window = button))
	startButton.append (canvas.create_window((canvasSizeX/2)+100, canvasSizeY/2,window = button2))
	button3 = Button(root,command = loader,text = "띠용")
	canvas.create_window(500,150,window = button3)	


canvas.pack()
mainScene()
root.mainloop()

## makebutton 과 buttonCall 부분의 버튼 생성 부분 합치기

