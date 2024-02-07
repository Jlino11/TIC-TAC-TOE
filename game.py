#import numpy as np
borad = [
    [
        '1','2','3'
    ],
    [
        '4','5','6'
    ],
    [
        '7','8','9'
    ]
]
currentPlayer = "X"
winner = None
gameRunning = True
numbers_already_taken = []

#Printing the game borad
def printBorad(borad):
    for raw in borad:
        print("\n")
        for item in raw:
            print(item, end=" ")
    print("\n")

#take player input
def playerInput(borad):
    global numbers_already_taken, gameRunning
    number = input("Number of position to take: ")
    if int(number) >= 1 and int(number) <=9 and number :
        if number not in numbers_already_taken:
            #print(borad)
            for position in range(0,3):
                for subposition in range(0,3):
                    if borad[position][subposition] == number :
                        numbers_already_taken.append(number)
                        borad[position][subposition] = currentPlayer
        else:
            print("\nPosition already taken!\n")
            printBorad(borad)
            playerInput(borad)
    else:
        print("Ooops thats number is not in range!")

#check for win or tie
def chechHorizontle(borad):
    global winner
    if borad[0][0] == 'X' and borad[0][1] == 'X' and borad[0][2] == 'X':
        winner = borad[0][0]
        return True
    elif borad[1][0] == 'X' and borad[1][1] == 'X' and borad[1][2] == 'X':
        winner = borad[1][0]
        return True
    elif borad[2][0] == 'X' and borad[2][1] == 'X' and borad[2][2] == 'X':
        winner = borad[2][0]
        return True
    elif borad[1][0] == 'O' and borad[1][1] == 'O' and borad[1][2] == 'O':
        winner = borad[1][0]
        return True
    elif borad[2][0] == 'O' and borad[2][1] == 'O' and borad[2][2] == 'O':
        winner = borad[2][0]
        return True
    elif borad[2][0] == 'O' and borad[2][1] == 'O' and borad[2][2] == 'O':
        winner = borad[2][0]
        return True

#Check for row
def checkRow(borad):
    global winner
    if borad[0][0] == 'X' and borad[1][0] == 'X' and borad[2][0] == 'X':
        winner = borad[0][0]
        return True
    elif borad[0][1] == 'X' and borad[1][1] == 'X' and borad[2][1] == 'X':
        winner = borad[0][1]
        return True
    elif borad[0][0] == 'X' and borad[1][0] == 'X' and borad[2][0] == 'X':
        winner = borad[0][0]
        return True
    elif borad[0][1] == 'O' and borad[1][1] == 'O' and borad[2][1] == 'O':
        winner = borad[0][1]
        return True
    elif borad[0][2] == 'O' and borad[1][2] == 'O' and borad[2][2] == 'O':
        winner = borad[0][2]
        return True
    elif borad[2][0] == 'O' and borad[2][1] == 'O' and borad[2][2] == 'O':
        winner = borad[2][0]
        return True 

#Check for diag
def checkDiag(borad):
    global winner
    if borad[0][0] == 'X' and borad[1][1] == 'X' and borad[2][2] == 'X':
        winner = borad[0][0]
        return True
    elif borad[0][2] == 'X' and borad[1][1] == 'X' and borad[2][0] == 'X':
        winner = borad[0][2]
        return True
    elif borad[0][0] == 'O' and borad[1][1] == 'O' and borad[2][2] == 'O':
        winner = borad[0][0]
        return True
    elif borad[0][2] == 'O' and borad[1][1] == 'O' and borad[2][0] == 'O':
        winner = borad[0][2]
        return True

#Check winner
def checkTie(borad):
    global gameRunning
    if chechHorizontle(borad) or checkRow(borad) or checkDiag(borad):
        print(f"The winner is {winner}!")
        printBorad(borad)
        gameRunning = False
    elif len(numbers_already_taken) == 9:          
        print("\nGame over toe!\n")
        gameRunning = False



#switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'
#check for win or tie again

while gameRunning:
    
    printBorad(borad)
    switchPlayer()
    playerInput(borad)
    checkTie(borad)
    