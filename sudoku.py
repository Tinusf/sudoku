boardInfo =""
size = 0
def readFromFile(filename):
    f = open(filename, "r")
    global size
    size = f.readline()
    matrix = [None] * int(size)
    for x in range(9):
        listInMatrix = []
        current = f.readline().strip()
        for cur in current:
            listInMatrix.append(int(cur))
        matrix[x] = listInMatrix
    f.close()
    return matrix

def boardPritner():
    print("    0 1 2   3 4 5   6 7 8")
    print("-" * 25)
    for y in range(9):
        currentLine = ""
        for x in range(9):
            currentLine += str(boardInfo[y][x]) + " "
            if x == 2 or x == 5:
                currentLine += ("| ")
        print(y, "|", currentLine)
        if y == 2 or y == 5:
            print("-"* 25)

def getHorizonalList(x, y):
    return boardInfo[y]

def getVerticalList(x, y):
    outputList = []
    for i in range(len(boardInfo[0])):
        outputList.append(boardInfo[i][x])
    return outputList

def getSquareList(x, y):
    outList = []
    xSquare = x // 3
    ySquare = y // 3
    for i in range(3):
        for j in range(3):
            outList.append(boardInfo[3*ySquare+i][3*xSquare+j])
    return outList

def getConflictNumber(x,y):
    conflictNr = set()
    hor = getHorizonalList(x,y)
    ver = getVerticalList(x,y)
    square = getSquareList(x,y)
    for x in hor:
        conflictNr.add(x)
    for x in ver:
        conflictNr.add(x)
    for x in square:
        conflictNr.add(x)
    conflictNr.remove(0)
    return conflictNr

def checkMove(number, x, y):
    if -1 < x < 9 and -1 < y < 9:
        return not number in getConflictNumber(x,y) and boardInfo[y][x] == 0
    return False
def saveBoard(filename):
    f = open(filename, "w")
    f.write(str(size))
    for item in boardInfo:
        lineToWrite = ""
        for number in item:
            lineToWrite+= str(number)
        f.writelines(str(lineToWrite) + "\n")
    f.close()

def checkWin():
    for rows in boardInfo:
        if 0 in rows:
            return False
    return True

def main():
    global boardInfo
    print("Welcome to sudoku.")
    boardInfo = readFromFile("sudoku.txt")
    boardPritner()
    while True:
        answer = input('write "number x y" or "remove x y", or "save", or "quit"')
        if answer == "save":
            saveBoard("sudoku.txt")
        elif answer[0:6] == "remove":
            cords = answer.split(" ")
            x = int(cords[1])
            y = int(cords[2])
            boardInfo[y][x] = 0
        elif answer == "quit":
            break
        else: #number x y
            cords = answer.split(" ")
            number = int(cords[0])
            x = int(cords[1])
            y = int(cords[2])
            if 0 < number < 10:
                if checkMove(number,x,y):
                    boardInfo[y][x] = number
                    if checkWin():
                        print("Congratulations!")
                        break
                else:
                    print("That's not quite right!")
            else:
                print("That's not quite right!")
        boardPritner()
main()