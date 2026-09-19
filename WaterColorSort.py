import turtle, random, copy
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
#----------FunctionsSetup----------
def createCoordinates():
    global gutter,bottleEdgesquareSize,chooseMode,coordinates,startingX,startingY
    coordinates = []
    colorSquare.goto(startingX,startingY)
    for i in range(round(mode[chooseMode]/2-0.1)+1):
        temp = []
        for j in range(4):
            temp.append(colorSquare.pos())
            colorSquare.sety(colorSquare.ycor()-squareSize)
        colorSquare.goto(colorSquare.xcor()+gutter+bottleEdge*2+squareSize,startingY)
        coordinates.append(temp)
    colorSquare.goto(startingX,startingY-4*squareSize-gutter-bottleEdge-bottleEdgeTop)
    for i in range(round(mode[chooseMode]/2-0.1)):
        temp = []
        for j in range(4):
            temp.append(colorSquare.pos())
            colorSquare.sety(colorSquare.ycor()-squareSize)
        colorSquare.goto(colorSquare.xcor()+gutter+bottleEdge*2+squareSize,startingY-4*squareSize-gutter-bottleEdge-bottleEdgeTop)
        coordinates.append(temp)
    generateColor()
    myWin.update()
    return
def generateColor():
    global chooseMode,bottle,tempLevel
    colorData = (random.sample(color,mode[chooseMode]-2))
    colorLeft = [4]*(mode[chooseMode]-2)
    bottle = []
    for i in range(len(coordinates)):
        while True:
            temp = []
            tempColorLeft = colorLeft.copy()
            tempColorData = colorData.copy()
            for j in range(len(coordinates[i])):
                if colorData != [0]*(mode[chooseMode]-2):
                    usableColor = []
                    colorSquare.goto(coordinates[i][j])
                    for k in colorData:
                        if isinstance(k,str):
                            usableColor.append(k)
                    currColor = random.choice(usableColor)
                    colorSquare.color(currColor)
                    colorSquare.stamp()
                    colorLeft[colorData.index(currColor)] -= 1
                    temp.append(color.index(currColor))
                    if colorLeft[colorData.index(currColor)] <= 0:
                        colorData[colorData.index(currColor)] = 0
                else:
                    temp.append(-1)
            if temp[0] == temp[1] and temp[0] == temp[2] and temp[0] == temp[3] and temp!= 4*[-1]:
                colorLeft = tempColorLeft.copy()
                colorData = tempColorData.copy()
                continue
            else:
                break
        bottle.append(temp)
    tempLevel = copy.deepcopy(bottle)
    myWin.update()
    return
def clickBottle(x,y):
    global tempBottle,tempRedo,wait
    if IfWin is False:
        if wait is False:
            chooseBottle = whichBottle(x,y)
            if chooseBottle != -1:
                if bottleState[chooseBottle] == 0:
                    glowSquare.goto(bottleCoordinate[chooseBottle])
                    glowSquare.stamp()
                    tempBottle.append(chooseBottle)
                    bottleState[chooseBottle] = 1
                elif bottleState[chooseBottle] == 1:
                    glowSquare.clear()
                    bottleState[chooseBottle] = 0
                    tempBottle.remove(chooseBottle)
                if bottleState.count(1) == 2:
                    tempRedo = copy.deepcopy(bottle)
                    colorToPour = []
                    colorToAdd = []
                    pourWater(colorToPour,colorToAdd)
                    animation(colorToPour,colorToAdd)
                    ifWin()
                    glowSquare.clear()
                    for i in tempBottle:
                        bottleState[i] = 0
                    tempBottle = []
                myWin.update()
    else:
        leftBoundary = 0-100/2
        rightBoundary = 0+100/2
        topBoundary = (-20)+50/2
        bottomBoundary = (-20)-50/2
        if leftBoundary <= x <= rightBoundary and bottomBoundary <= y<= topBoundary:
            NextLevel()
    return
def pourWater(colorToPour,colorToAdd):
    if bottle[tempBottle[-1]].count(-1) >= 1 and bottle[tempBottle[0]] != [-1]*4:
        for i in range(len(bottle[tempBottle[-1]])-1,-1,-1):
            if bottle[tempBottle[-1]][i] == -1:
                lastBlank = i
                break
        for i in range(len(bottle[tempBottle[0]])):
            if bottle[tempBottle[0]][i] != -1:
                currColor = i
                break
        if (bottle[tempBottle[-1]].count(-1) == 4 or bottle[tempBottle[-1]][lastBlank+1] == bottle[tempBottle[0]][currColor]) and bottle[tempBottle[0]][currColor] != -1:
            bottle[tempBottle[-1]][lastBlank] = bottle[tempBottle[0]][currColor]
            bottle[tempBottle[0]][currColor] = -1
            colorToPour.append(currColor)
            colorToAdd.append(lastBlank)
            if currColor != 3 and bottle[tempBottle[0]][currColor+1] == bottle[tempBottle[-1]][lastBlank]:
                pourWater(colorToPour,colorToAdd)
    return
def whichBottle(x,y):
    global bottleLength,bottleWidth
    for i in range(len(bottleCoordinate)):
        leftBoundary = bottleCoordinate[i][0]-bottleWidth/2
        rightBoundary = bottleCoordinate[i][0]+bottleWidth/2
        topBoundary = bottleCoordinate[i][1]+bottleLength/2
        bottomBoundary = bottleCoordinate[i][1]-bottleLength/2
        if leftBoundary <= x <= rightBoundary and bottomBoundary <= y<= topBoundary:
            return i
    return -1
def animation(colorToPour,colorToAdd):
    global squareSize,wait,lastBlank,currColor
    if not colorToPour or not colorToAdd:
        return
    wait = True
    animationSquare.color("white")
    animationSquare.goto(coordinates[tempBottle[0]][colorToPour[0]][0], coordinates[tempBottle[0]][colorToPour[0]][1]+squareSize/2)
    for i in range(len(colorToPour)):
        for j in range(37):
            animationSquare.stamp()
            animationSquare.sety(animationSquare.ycor()-1)
            myWin.update()
    animationSquare.color(color[bottle[tempBottle[-1]][colorToAdd[0]]])
    animationSquare.goto(coordinates[tempBottle[-1]][colorToAdd[0]][0], coordinates[tempBottle[-1]][colorToAdd[0]][1]-squareSize/2)
    for i in range(len(colorToAdd)):
        for j in range(37):
            animationSquare.stamp()
            animationSquare.sety(animationSquare.ycor()+1)
            myWin.update()
    colorSquare.color("white")
    colorSquare.goto(coordinates[tempBottle[0]][colorToPour[0]])
    for i in range(len(colorToPour)):
        colorSquare.stamp()
        colorSquare.sety(colorSquare.ycor()-squareSize)
    colorSquare.color(color[bottle[tempBottle[-1]][colorToAdd[0]]])
    colorSquare.goto(coordinates[tempBottle[-1]][colorToAdd[0]])
    for i in range(len(colorToAdd)):
        colorSquare.stamp()
        colorSquare.sety(colorSquare.ycor()+squareSize)
    animationSquare.clear()
    myWin.update()
    wait = False
    return
def Redo(x,y):
    global ifRedo,bottle
    if len(tempRedo) > 0:
        if ifRedo is True:
            for i in range(len(tempRedo)):
                for j in range(len(tempRedo[i])):
                    if bottle[i][j] != tempRedo[i][j]:
                        colorSquare.goto(coordinates[i][j])
                        if tempRedo[i][j] != -1:
                            colorSquare.color(color[tempRedo[i][j]])
                            colorSquare.stamp()
                        else:
                            colorSquare.color("white")
                            colorSquare.stamp()
            bottle = copy.deepcopy(tempRedo)
            ifRedo = False
            redoSquare.shape(redoDark)
    myWin.update()
    return
def Restart(x,y):
    global ifRedo,ifEmpty,bottle,tempBottle,bottleState,chooseMode
    for i in range(len(tempLevel)):
        for j in range(len(tempLevel[i])):
            if bottle[i][j] != tempLevel[i][j]:
                colorSquare.goto(coordinates[i][j])
                if tempLevel[i][j] != -1:
                    colorSquare.color(color[tempLevel[i][j]])
                    colorSquare.stamp()
                else:
                    colorSquare.color("white")
                    colorSquare.stamp()
    if len(bottleCoordinate) > mode[chooseMode]:
        bottleSquare.goto(bottleCoordinate[-1])
        bottleSquare.shape(notuseBottle)
        bottleSquare.stamp()
        del bottleCoordinate[-1]
        del coordinates[-1]
    bottle = copy.deepcopy(tempLevel)
    tempBottle = []
    bottleState = mode[chooseMode]*[0]
    glowSquare.clear()
    ifRedo = True
    redoSquare.shape(redo)
    ifEmpty = True
    emptySquare.shape(empty)
    myWin.update()
    return
def Empty(x,y):
    global ifEmpty,gutter,squareSize
    if ifEmpty is True:
        bottleSquare.shape(bottleImage)
        bottleSquare.goto(bottleCoordinate[-1][0]+gutter+squareSize*1.5-2,bottleCoordinate[-1][1])
        bottleSquare.stamp()
        bottleCoordinate.append(bottleSquare.pos())
        colorSquare.goto(coordinates[-1][0][0]+gutter+bottleEdge*2+squareSize,coordinates[-1][0][1])
        temp = []
        for i in range(4):
            temp.append(colorSquare.pos())
            colorSquare.sety(colorSquare.ycor()-squareSize)
        coordinates.append(temp)
        bottleState.append(0)
        bottle.append([-1,-1,-1,-1])
        ifEmpty = False
        emptySquare.shape(emptyDark)
    myWin.update()
    return
def ifWin():
    global turtleSize,levelSquare,IfWin
    for i in bottle:
        for j in i:
            if j != i[0]:
                return
    IfWin = True
    whiteBackgroundSquare.stamp()
    congratsSquare.stamp()
    levelSquare.stamp()
    myWin.update()
    return
def NextLevel():
    global bottle,bottleState,chooseMode,ifRedo,ifEmpty,IfWin,tempRedo
    colorSquare.clear()
    glowSquare.clear()
    tempRedo = []
    if len(bottleCoordinate) > mode[chooseMode]:
        bottleSquare.goto(bottleCoordinate[-1])
        bottleSquare.shape(notuseBottle)
        bottleSquare.stamp()
        del bottleCoordinate[-1]
        del coordinates[-1]
    bottleState = [0]*mode[chooseMode]
    ifRedo = True
    redoSquare.shape(redo)
    ifEmpty = True
    emptySquare.shape(empty)
    whiteBackgroundSquare.clear()
    congratsSquare.clear()
    levelSquare.clear()
    generateColor()
    IfWin = False
    myWin.update()
    return
#----------ChooseMode----------
mode = [7,11,15]
chooseMode = input("Choose your mode(enter the number): (0)easy (1)hard (2)expert!")
while True:
    if chooseMode in ("0","1","2"):
        break
    print("Invalid input! Please enter a valid integer between 0 and 2.")
    chooseMode = input("Choose your mode(enter the number): (0)easy (1)medium (2)hard!")
chooseMode = int(chooseMode)
#----------VariablesSetup----------
gutter = 50
bottleEdge = 8
bottleEdgeTop = 18
squareSize = 36
ScreenSizeX = gutter*(round(mode[chooseMode]/2-0.1)+2)+bottleEdge*2*(round(mode[chooseMode]/2-0.1)+1)+squareSize*(round(mode[chooseMode]/2-0.1)+1)-2
ScreenSizeY = gutter*3+bottleEdgeTop*2+bottleEdge*2+squareSize*8
halfScreenX = int(ScreenSizeX/2)
halfScreenY = int(ScreenSizeY/2)
offset = 15
startingX = -1*halfScreenX+gutter+bottleEdge+offset
startingY = halfScreenY-gutter-bottleEdgeTop+50
turtleSize = squareSize / 20
bottleLength = 170
bottleWidth = 52
buttonGutter = (ScreenSizeX-300)/4
ifRedo = True
ifEmpty = True
wait = False
IfWin = False
#----------WindowSetup-----------
turtle.setup(ScreenSizeX,ScreenSizeY+100)
myWin = turtle.Screen()
myWin.title('WaterColorSort')
myWin.tracer(0)
#----------ImageSetup----------
bottleImage = str(BASE_DIR / "bottle.gif")
glow = str(BASE_DIR / "glow.gif")
restart = str(BASE_DIR / "restart.gif")
redo = str(BASE_DIR / "redo.gif")
redoDark = str(BASE_DIR / "redoDark.gif")
empty = str(BASE_DIR / "empty.gif")
emptyDark = str(BASE_DIR / "emptyDark.gif")
nextLevel = str(BASE_DIR / "nextLevel.gif")
notuseBottle = str(BASE_DIR / "notuseBottle.gif")
congrats = str(BASE_DIR / "congrats.gif")
myWin.addshape(bottleImage)
myWin.addshape(glow)
myWin.addshape(restart)
myWin.addshape(redo)
myWin.addshape(redoDark)
myWin.addshape(empty)
myWin.addshape(emptyDark)
myWin.addshape(nextLevel)
myWin.addshape(notuseBottle)
myWin.addshape(congrats)
#----------ListSetup----------
color = ["#ff4747","#ff9418","#fff467","#a1ef5e","#56905d","#3ee3dd","#3fa2f7","#b365bb","#ffb1d9","#988907","#85b2c7","#874f40","#240f6e"]
bottleCoordinate = []
bottleState = []
tempBottle = []
tempRedo = []
tempLevel = []
#----------TurtleCreation----------
colorSquare = turtle.Turtle()
colorSquare.penup()
colorSquare.turtlesize(turtleSize)
colorSquare.speed(0)
colorSquare.shape("square")
colorSquare.hideturtle()
#----------
bottleSquare = turtle.Turtle()
bottleSquare.shape(bottleImage)
bottleSquare.penup()
bottleSquare.speed(0)
bottleSquare.hideturtle()
#----------
animationSquare = turtle.Turtle()
animationSquare.penup()
animationSquare.turtlesize(1/20,squareSize/20)
animationSquare.speed(0)
animationSquare.shape("square")
animationSquare.hideturtle()
#----------
glowSquare = turtle.Turtle()
glowSquare.shape(glow)
glowSquare.penup()
glowSquare.speed(0)
glowSquare.hideturtle()
#----------
restartSquare = turtle.Turtle()
restartSquare.shape(restart)
restartSquare.penup()
restartSquare.speed(0)
restartSquare.goto(-1*halfScreenX+buttonGutter+50,-1*halfScreenY+30)
#----------
redoSquare = turtle.Turtle()
redoSquare.shape(redo)
redoSquare.penup()
redoSquare.speed(0)
redoSquare.goto(-1*halfScreenX+buttonGutter*2+150,-1*halfScreenY+30)
#----------
emptySquare = turtle.Turtle()
emptySquare.shape(empty)
emptySquare.penup()
emptySquare.speed(0)
emptySquare.goto(-1*halfScreenX+buttonGutter*3+250,-1*halfScreenY+30)
#----------
whiteBackgroundSquare = turtle.Turtle()
whiteBackgroundSquare.shape("square")
whiteBackgroundSquare.color("white")
whiteBackgroundSquare.turtlesize(1000,1000)
whiteBackgroundSquare.hideturtle()
#----------
congratsSquare = turtle.Turtle()
congratsSquare.shape(congrats)
congratsSquare.penup()
congratsSquare.goto(0,50)
congratsSquare.speed(0)
congratsSquare.hideturtle()
#----------
levelSquare = turtle.Turtle()
levelSquare.shape(nextLevel)
levelSquare.penup()
levelSquare.speed(0)
levelSquare.goto(0,-20)
levelSquare.hideturtle()
#----------GameSetup----------
bottleSquare.goto(startingX,bottleEdgeTop+3*squareSize+2+50)
for i in range(round(mode[chooseMode]/2-0.1)+1):
    bottleSquare.stamp()
    bottleCoordinate.append(bottleSquare.pos())
    bottleState.append(0)
    bottleSquare.setx(bottleSquare.xcor()+gutter+squareSize+bottleEdge*2)
bottleSquare.goto(startingX,bottleEdgeTop+bottleEdge-2*squareSize-gutter+4+50)
for i in range(round(mode[chooseMode]/2-0.1)):
    bottleSquare.stamp()
    bottleCoordinate.append(bottleSquare.pos())
    bottleState.append(0)
    bottleSquare.setx(bottleSquare.xcor()+gutter+squareSize+bottleEdge*2)
bottleSquare.shape(notuseBottle)
bottleSquare.stamp()
myWin.update()
createCoordinates()
#----------EventHandlers----------
myWin.onclick(clickBottle)
restartSquare.onclick(Restart)
redoSquare.onclick(Redo)
emptySquare.onclick(Empty)
#----------TheLastLine----------
myWin.mainloop()