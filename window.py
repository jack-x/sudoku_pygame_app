import pygame

import time
import builder, puzzler

#initialize sudoku
pygame.init()


#colors defined here

black = (0,0,0)
green = (0,255,100)
grey = (174,174,163)
blue = (255, 102, 0)

gameDisplay = pygame.display.set_mode((1000,1000))

sud = puzzler.generatePuzzleSolution(45)
sudokuGrid = sud[0]
sudokuSolution = sud[1]
sudokuGridCorner = [55,50]

sudokuGridInterface = puzzler.createSudokuCopy(sudokuGrid)
#initial setup

text = ' 7 '
fontobject = pygame.font.SysFont('comicsansms', 50)
textSurface = fontobject.render(text,True,(0,0,0))
cellwidth = textSurface.get_width()
cellheight = textSurface.get_height()

simpleList = [0] *9
cellCoordinatesArray = [0] * 9
for x in range(0,9):
    cellCoordinatesArray[x] = list(simpleList)

#store in a dict, coordinates for all rectangle corners
cornerX = sudokuGridCorner[0]
cornerY = sudokuGridCorner[1]
for x in range(0,9):
    for y in range(0,9):
        cellCoordinatesArray[x][y] = (cornerX,cornerY)
        cornerX += cellwidth + 15
    cornerY += cellheight + 15
    cornerX = sudokuGridCorner[0]

####inital setup complete
setupList = [False]*9

cellHighlightFlagArray = [True]*9
cellClickFlagArray = [False] * 9
clickHighlightArray = [False] * 9
for x in range(0,9):
    cellHighlightFlagArray[x] = list(setupList)
    cellClickFlagArray[x] = list(setupList)
    clickHighlightArray[x] = list(setupList)



pygame.display.set_caption('Python Sudoku')
gameDisplay.fill(grey)

clock = pygame.time.Clock()


gridTopCorner = [55,50]


def showGridSurface():
        

    for x in range(0,9):
        for y in range(0,9):
            if sudokuGrid[x][y] != 0:
                text = ' ' + str(sudokuGrid[x][y]) + ' '
            else:
                text = ' '+ ' ' + ' '

            fontobject = pygame.font.SysFont('comicsansms', 50)
            textSurface = fontobject.render(text,True,(0,0,0))
            gameDisplay.blit(textSurface,cellCoordinatesArray[x][y])

    lineTop = (cellCoordinatesArray[0][2][0]+cellwidth + 7, cellCoordinatesArray[0][2][1] - 7)
    lineBottom = (cellCoordinatesArray[8][2][0]+cellwidth + 7, cellCoordinatesArray[8][2][1] + cellheight +7 )


    pygame.draw.line(gameDisplay,(224,224,224),lineTop, lineBottom, 3)

    lineTop = (cellCoordinatesArray[0][5][0]+cellwidth + 7, cellCoordinatesArray[0][5][1] - 7)
    lineBottom = (cellCoordinatesArray[8][5][0]+cellwidth + 7, cellCoordinatesArray[8][5][1] + cellheight +7 )


    pygame.draw.line(gameDisplay,(224,224,224),lineTop, lineBottom, 3)


    lineLeft = (cellCoordinatesArray[2][0][0] - 7, cellCoordinatesArray[2][0][1] + cellheight + 7)
    lineRight = (cellCoordinatesArray[2][8][0]+cellwidth + 7, cellCoordinatesArray[2][8][1] + cellheight +7 )


    pygame.draw.line(gameDisplay,(224,224,224),lineLeft, lineRight, 3)



    lineLeft = (cellCoordinatesArray[5][0][0] - 7, cellCoordinatesArray[5][0][1] + cellheight + 7)
    lineRight = (cellCoordinatesArray[5][8][0]+cellwidth + 7, cellCoordinatesArray[5][8][1] + cellheight +7 )


    pygame.draw.line(gameDisplay,(224,224,224),lineLeft, lineRight, 3)



    for x in range(0,9):
        for y in range(0,9):
            
            #draw the side vertical line
            if y in [2,5,8]:
                continue
            currentCoordinates = list(cellCoordinatesArray[x][y])
            currentCoordinates[0] += cellwidth
            lineTop = (currentCoordinates[0] + 7,currentCoordinates[1])
            lineBottom = (currentCoordinates[0] + 7,currentCoordinates[1]+cellheight)
            pygame.draw.line(gameDisplay,black,lineTop,lineBottom,1)


    for x in range(0,9):
        for y in range(0,9):
            #draw the bottom horizontal line
            if x in [2,5,8]:
                continue

            currentCoordinates = list(cellCoordinatesArray[x][y])
            currentCoordinates[1] += cellheight
            lineLeft = (currentCoordinates[0],currentCoordinates[1] + 7)
            lineRight = (currentCoordinates[0]+cellwidth,currentCoordinates[1] + 7)
            pygame.draw.line(gameDisplay,black,lineLeft,lineRight,1)


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse  = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if (x+w > mouse[0] and x < mouse[0] ) and (mouse[1] < (y + h) and mouse[1] > y):
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == 'solve':
                solveButtonClicked()
                time.sleep(3)
                pygame.quit()
                quit()
            # if action == 'Play':
            #   gameLoop()
            # if action == 'Quit':
            #     pygame.quit()
            #     quit()  
            # if action == 'Unpause':
            #     unpause()    
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
    
    fontobject = pygame.font.SysFont('comicsansms', 20)
    textSurface = fontobject.render(msg,True,blue)
    textRect = textSurface.get_rect()
    textRect.center = ( x +(w/2) , y + (h/2) )
    gameDisplay.blit(textSurface,textRect)

    # smallText = pygame.font.SysFont('comicsansms',20)
    # textSurf,textRect = text_objects(msg, smallText)
    
    # gameDisplay.blit(textSurf,textRect)




def setAllOtherClicksFalse(x,y):
    for X in range(0,9):
        for Y in range(0,9):
            if X is x and Y is y:
                continue

            cellClickFlagArray[X][Y] = False

def setClickHighlightTrue(x,y):
    for X in range(0,9):
        for Y in range(0,9):
            if Y is y:
                clickHighlightArray[X][Y] = True
                continue
            if X is x:
                clickHighlightArray[X][Y] = True
                continue
            clickHighlightArray[X][Y] = False
            

def solveButtonClicked():
    print("entered function")

    cellTraversalList = [(0,0)] * 9
    for x in range(0,9):
        cellTraversalList[x] = (x,x)
    print(cellTraversalList)
    for corner in cellTraversalList:
        print(corner)
        cornerx = corner[0]
        cornery = corner[1]
       
        # highligt row
        for Y in range(cornery,9):
            x = cellCoordinatesArray[cornerx][Y][0]
            y = cellCoordinatesArray[cornerx][Y][1]
            print(x)
            print(y)
            newSurface = pygame.Surface((cellwidth,cellheight))
            newSurface.fill(grey)
            gameDisplay.blit(newSurface,(x,y))
            text = ' '+ str(sudokuSolution[cornerx][Y]) + ' '
            fontobject = pygame.font.SysFont('comicsansms', 50)
            textSurface = fontobject.render(text,True,black)
            gameDisplay.blit(textSurface,(x,y))

            newSurface = pygame.Surface((cellwidth,cellheight))
            newSurface.set_alpha(70)
            newSurface.fill((102, 255, 102))
            gameDisplay.blit(newSurface,(x,y))
        

        #highlight column
        for X in range(cornerx,9):
            x = cellCoordinatesArray[X][cornery][0]
            y = cellCoordinatesArray[X][cornery][1]
            print(x)
            print(y)
            newSurface = pygame.Surface((cellwidth,cellheight))
            newSurface.fill(grey)
            gameDisplay.blit(newSurface,(x,y))

            text = ' '+ str(sudokuSolution[X][cornery]) + ' '
            fontobject = pygame.font.SysFont('comicsansms', 50)
            textSurface = fontobject.render(text,True,black)
            gameDisplay.blit(textSurface,(x,y))

            newSurface = pygame.Surface((cellwidth,cellheight))
            newSurface.set_alpha(70)
            newSurface.fill((102, 255, 102))
            gameDisplay.blit(newSurface,(x,y))
        
        pygame.display.update()
        time.sleep(0.5)
        clock.tick(120)







def main_game_loop():
    gameExit = False
    showGridSurface()

    while gameExit is False:
        GameEvents = pygame.event.get()
        
        button('Submit',800, 100, 100,60,green,blue)

        button('Solve',800, 300, 100,60,green,blue,"solve")
        

        for event in GameEvents:

            # print(event)
            if event.type == pygame.QUIT:
                gameExit = True

            mouse  = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            
            if event.type == pygame.KEYDOWN:
                print(event.key)
                if (event.key >=49 and event.key <= 57) or (event.key >= 257 and event.key <= 265):
                    #First find the clicked / Active cell
                    variable = event.key
                    found = False
                    activeX = -1
                    activeY = -1
                    if event.key >= 257:
                        variable = (event.key - 257) + 49


                    for x in range(0,9):
                        for y in range(0,9):
                            if cellClickFlagArray[x][y] == True:
                                found = True
                                activeX = x
                                activeY = y
                                break
                        if found == True:
                            break
                    
                    if sudokuGrid[activeX][activeY] == 0:
                        sudokuGridInterface[activeX][activeY] = variable - pygame.K_0
                        
                        newSurface = pygame.Surface((cellwidth,cellheight))
                        newSurface.fill(grey)
                        gameDisplay.blit(newSurface,cellCoordinatesArray[activeX][activeY])
                        text = ' '+ str(sudokuGridInterface[activeX][activeY]) + ' '
                        fontobject = pygame.font.SysFont('comicsansms', 50)
                        textSurface = fontobject.render(text,True,blue)
                        gameDisplay.blit(textSurface,cellCoordinatesArray[activeX][activeY])
                        newSurface = pygame.Surface((cellwidth,cellheight))
                        newSurface.set_alpha(50)
                        newSurface.fill((0, 153, 0))
                        gameDisplay.blit(newSurface,cellCoordinatesArray[activeX][activeY])

                break #break out of event loop

            
            for x in range(0,9):
                for y in range(0,9):
                    currentCoordinates = cellCoordinatesArray[x][y]

                    if cellClickFlagArray[x][y] == True:
                        continue #skip everything
                    if clickHighlightArray[x][y] == True:
                        if ( mouse[0] >= currentCoordinates[0] ) and ( mouse[0] < currentCoordinates[0] + cellwidth ) and (mouse[1] >= currentCoordinates[1]) and ( mouse[1] <= currentCoordinates[1] + cellheight ):
                            if click[0] == 1:
                            

                                for xx in range(0,9):
                                    #highlighting row
                                    newSurface = pygame.Surface((cellwidth,cellheight))
                                    newSurface.fill(grey)
                                    gameDisplay.blit(newSurface,cellCoordinatesArray[xx][y])

                                    if sudokuGrid[xx][y] != 0:
                                        text = ' ' + str(sudokuGrid[xx][y]) + ' '
                                        color = black
                                    else:
                                        if sudokuGridInterface[xx][y] == 0:
                                            text = ' '+ ' ' + ' '
                                            color = black
                                        else:
                                            text = ' ' + str(sudokuGridInterface[xx][y]) + ' '
                                            color = blue
                                    fontobject = pygame.font.SysFont('comicsansms', 50)
                                    textSurface = fontobject.render(text,True,color)
                                    gameDisplay.blit(textSurface,cellCoordinatesArray[xx][y])

                                    newSurface = pygame.Surface((cellwidth,cellheight))
                                    newSurface.set_alpha(50)
                                    newSurface.fill((204, 255, 204))
                                    gameDisplay.blit(newSurface,cellCoordinatesArray[xx][y])
                                    cellHighlightFlagArray[xx][y] = True
                                
                                for yy in range(0,9):
                                    #highlighting column
                                    newSurface = pygame.Surface((cellwidth,cellheight))
                                    newSurface.fill(grey)
                                    gameDisplay.blit(newSurface,cellCoordinatesArray[x][yy])

                                    if sudokuGrid[x][yy] != 0:
                                        text = ' ' + str(sudokuGridInterface[x][yy]) + ' '
                                        color = black
                                    else:
                                        if sudokuGridInterface[x][yy] == 0:
                                            text = ' '+ ' ' + ' '
                                            color = black
                                        else:
                                            text = ' ' + str(sudokuGridInterface[x][yy]) + ' '
                                            color = blue
                                    fontobject = pygame.font.SysFont('comicsansms', 50)
                                    textSurface = fontobject.render(text,True,color)
                                    gameDisplay.blit(textSurface,cellCoordinatesArray[x][yy])

                                    newSurface = pygame.Surface((cellwidth,cellheight))
                                    newSurface.set_alpha(50)
                                    newSurface.fill((204, 255, 204))
                                    gameDisplay.blit(newSurface,cellCoordinatesArray[x][yy])
                                    cellHighlightFlagArray[x][yy] = True
                                
                                newSurface = pygame.Surface((cellwidth,cellheight))
                                newSurface.set_alpha(50)
                                newSurface.fill((0, 153, 0))
                                gameDisplay.blit(newSurface,currentCoordinates)
                                cellClickFlagArray[x][y] = True
                            
                                setClickHighlightTrue(x,y)
                                setAllOtherClicksFalse(x,y)

                        continue
                    newSurface = pygame.Surface((cellwidth,cellheight))
                    newSurface.fill(grey)
                    gameDisplay.blit(newSurface,currentCoordinates)
                    if sudokuGrid[x][y] != 0:
                        text = ' ' + str(sudokuGridInterface[x][y]) + ' '
                        color = black
                    else:
                        if sudokuGridInterface[x][y] == 0:
                            text = ' '+ ' ' + ' '
                            color = black
                        else:
                            text = ' ' + str(sudokuGridInterface[x][y]) + ' '
                            color = blue
                    fontobject = pygame.font.SysFont('comicsansms', 50)
                    textSurface = fontobject.render(text,True,color)
                    gameDisplay.blit(textSurface,cellCoordinatesArray[x][y])
                    cellHighlightFlagArray[x][y] = False



                    if ( mouse[0] >= currentCoordinates[0] ) and ( mouse[0] < currentCoordinates[0] + cellwidth ) and (mouse[1] >= currentCoordinates[1]) and ( mouse[1] <= currentCoordinates[1] + cellheight ):
                        if cellHighlightFlagArray[x][y] == True:
                            continue
                        else:
                            newSurface = pygame.Surface((cellwidth,cellheight))
                            newSurface.set_alpha(50)
                            newSurface.fill((204, 255, 204))
                            gameDisplay.blit(newSurface,currentCoordinates)
                            cellHighlightFlagArray[x][y] = True
                    
                        if click[0] == 1:
                        
                            for xx in range(0,9):
                                #highlighting row
                                newSurface = pygame.Surface((cellwidth,cellheight))
                                newSurface.fill(grey)
                                gameDisplay.blit(newSurface,cellCoordinatesArray[xx][y])

                                if sudokuGrid[xx][y] != 0:
                                    text = ' ' + str(sudokuGridInterface[xx][y]) + ' '
                                    color = black
                                else:
                                    if sudokuGridInterface[xx][y] == 0:
                                        text = ' '+ ' ' + ' '
                                        color = black
                                    else:
                                        text = ' ' + str(sudokuGridInterface[xx][y]) + ' '
                                        color = blue
                                fontobject = pygame.font.SysFont('comicsansms', 50)
                                textSurface = fontobject.render(text,True,color)
                                gameDisplay.blit(textSurface,cellCoordinatesArray[xx][y])

                                newSurface = pygame.Surface((cellwidth,cellheight))
                                newSurface.set_alpha(50)
                                newSurface.fill((204, 255, 204))
                                gameDisplay.blit(newSurface,cellCoordinatesArray[xx][y])
                                cellHighlightFlagArray[xx][y] = True
                            
                            for yy in range(0,9):
                                #highlighting column
                                newSurface = pygame.Surface((cellwidth,cellheight))
                                newSurface.fill(grey)
                                gameDisplay.blit(newSurface,cellCoordinatesArray[x][yy])

                                if sudokuGrid[x][yy] != 0:
                                    text = ' ' + str(sudokuGridInterface[x][yy]) + ' '
                                    color = black
                                else:
                                    if sudokuGridInterface[x][yy] == 0:
                                        text = ' '+ ' ' + ' '
                                        color = black
                                    else:
                                        text = ' ' + str(sudokuGridInterface[x][yy]) + ' '
                                        color = blue
                                fontobject = pygame.font.SysFont('comicsansms', 50)
                                textSurface = fontobject.render(text,True,color)
                                gameDisplay.blit(textSurface,cellCoordinatesArray[x][yy])

                                newSurface = pygame.Surface((cellwidth,cellheight))
                                newSurface.set_alpha(50)
                                newSurface.fill((204, 255, 204))
                                gameDisplay.blit(newSurface,cellCoordinatesArray[x][yy])
                                cellHighlightFlagArray[x][yy] = True
                        
                            newSurface = pygame.Surface((cellwidth,cellheight))
                            newSurface.set_alpha(50)
                            newSurface.fill((0, 153, 0))
                            gameDisplay.blit(newSurface,currentCoordinates)
                            cellClickFlagArray[x][y] = True
                           
                            setClickHighlightTrue(x,y)
                            setAllOtherClicksFalse(x,y)




            
            

        pygame.display.update()
        clock.tick(120)



main_game_loop()
pygame.quit()
quit()