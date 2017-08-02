from tkinter import *
import os


canvasSizeX = 1280
canvasSizeY = 720
totalButtonNum = 10
buttonSpace = 95
root = Tk()
canvas =  Canvas(root, width = canvasSizeX, height = 720)

def reload():
	for i in range(0,len(button)):
		canvas.delete(button[i])

def buyCall(parameter):
	global crystal
	payAmount = 100
	if crystal > payAmount:
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
	if buttonCrystal[num] == True :
		upgradeButton = Button(root,compound = CENTER, command = lambda i = num: buttonCall(num),text = str(level[num]) + "레벨")

	else:
		upgradeButton = Button(root,compound = CENTER, command = lambda i = num: buyCall(num),text = "Buy")
	button.append(canvas.create_window(num * buttonPoint + buttonPoint, 600,window = upgradeButton))


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
	goldText = canvas.create_text(100, 100, text = gold)

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
	crystalText = canvas.create_text(200,100, text = "크리스탈: "+ str(crystal))



canvas.pack()
setButton(totalButtonNum)
goldSystem()
crystalSystem("FTW")
root.mainloop()

## makebutton 과 buttonCall 부분의 버튼 생성 부분 합치기

