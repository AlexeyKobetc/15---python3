import random
import sys
import colorama
from colorama import Fore, Back, Style

POLE_WIDTH = 4
POLE_HEIGHT = 4

pole = []

def initArray(poleArray):

    for n in range(0, 16):

        number = random.randint (0, 15)

        while number in poleArray:

            number = random.randint (0, 15)
            

        poleArray.insert(n, number)

def drawPole (poleArray):

    for row in range(POLE_HEIGHT):
        for col in range(POLE_WIDTH):

            if poleArray[row * POLE_WIDTH + col] == 0:
                #print (Fore.RED, end = '')
                print ('XX', end = ' ')
                #print (Style.RESET_ALL, end = '')
            else:
                #print (Fore.GREEN, end = '')
                print ('%02d' % poleArray[row * POLE_WIDTH + col], end = ' ')
                #print (Style.RESET_ALL, end = '')
                
        print('')

def figureMove(dirMove, poleArray):

    for n in range(len(poleArray)):
        if poleArray[n] == 0:
            nZero = n

    col = nZero%POLE_WIDTH
    row = nZero//POLE_WIDTH

    if dirMove == 'UP':

        if row > 0:

            temp = poleArray[nZero -  POLE_WIDTH]
            poleArray[nZero -  POLE_WIDTH] = poleArray[nZero]
            poleArray[nZero] = temp

    if dirMove == 'DOWN':

        if row < POLE_HEIGHT - 1:

            temp = poleArray[nZero +  POLE_WIDTH]
            poleArray[nZero +  POLE_WIDTH] = poleArray[nZero]
            poleArray[nZero] = temp
    
    if dirMove == 'RIGHT':

        if col < POLE_WIDTH - 1:

            temp = poleArray[nZero + 1]
            poleArray[nZero + 1] = poleArray[nZero]
            poleArray[nZero] = temp

    if dirMove == 'LEFT':

        if col > 0:

            temp = poleArray[nZero - 1]
            poleArray[nZero - 1] = poleArray[nZero]
            poleArray[nZero] = temp


    drawPole (pole)
    check = checkArray(pole)

    print (check)
    

def checkArray(poleArray):

    start = 0

    for n in poleArray:

        if start == n:
            
            start += 1
            
        else:

            return 0
        
    return 1

def main():

    colorama.init()

    initArray (pole)
    drawPole (pole)

    error = ''

    while (1):

        userMove = input('{}Input dir by WASD: '.format (error))
        error = ''

        if userMove.upper() == 'W':

            figureMove('UP', pole)

        elif userMove.upper() == 'S':

            figureMove('DOWN', pole)

        elif userMove.upper() == 'A':

            figureMove('LEFT', pole)

        elif userMove.upper() == 'D':

            figureMove('RIGHT', pole)

        else:
        
            error = 'Error enter ! '

if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)

