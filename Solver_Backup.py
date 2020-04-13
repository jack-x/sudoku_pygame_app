

matrixLimit = [
                    [0,0,2,2],[0,3,2,5],[0,6,2,8],
                    [3,0,5,2],[3,3,5,5],[3,6,5,8],
                    [6,0,8,2],[6,3,8,5],[6,6,8,8]
                  ]


recursionDepthCount = 0

def displayGridcmd(sudoku):
    
    for linenumber in range(0,11):

        if linenumber == 0:
            line = ['|||||||'] * 9
            print("|||{}|||".format(''.join(line)))
            print()

        elif linenumber == 10:
            print()
            line = ['|||||||'] * 9
            print("|||{}|||".format(''.join(line)))

            
        else:
            gridRow = linenumber - 1
            line = "|||"

            count =0
            for x in sudoku[gridRow]:
                count +=1 
                if count == 3:
                    line = line + "   " + str(x) +" *|"
                    count = 0
                elif count == 1:
                    line = line + "|* " + str(x) +"   "
                else:
                    line = line + "   " + str(x) +"   "
            
            line = line + "|||"
            print(line)
            
            if linenumber in [3,6,9]:
                line = ['-------'] * 9
                print("|||{}|||".format(''.join(line)))

            line = ['-------'] * 9
            print("|||{}|||".format(''.join(line)))



def inputSudoku():
    line = [0,0,0,0,0,0,0,0,0]

    sudokuGrid = [0]*9

    for position in range(0,9):
        sudokuGrid[position] = list(line)
    
    
    sudokuFile = open("sudokuInput.txt",'r')   
    for gridRow in range(0,9):
        fileLine = sudokuFile.readline()
        line = list(fileLine)
        for gridColumn in range(0,9):
            sudokuGrid[gridRow][gridColumn] = int(line[gridColumn])

    return sudokuGrid
    




def main():
    sudokuGrid = inputSudoku()
    displayGridcmd(sudokuGrid)

    for row in range(0,9):
        for column in range(0,9):

            if sudokuGrid[row][column] == 0:
                knockoutList = [1,2,3,4,5,6,7,8,9]

                #check row
                currentrow = list(sudokuGrid[row])
                for element in currentrow:
                    if element in knockoutList:
                        knockoutList.remove(element)
                
                #check column
                columnNumber = column

                for rowNumber in range(0,9):
                    number = sudokuGrid[rowNumber][columnNumber]
                    if number in knockoutList:
                        knockoutList.remove(number)

                #check 3*3 matrix
                currentMatrix = 0
                for matrix in matrixLimit:
                    
                    rowStart = matrix[0] 
                    colStart = matrix[1]

                    rowEnd = matrix[2]
                    colEnd = matrix[3]

                    if row >= rowStart and row<=rowEnd:
                        if column >= colStart and column <=colEnd:
                            currentMatrix = list(matrix)
                            break
                            #breaking out of matrix limit loop, as the matrix in which the element belongs has been found
                    
                
                for rowcheck in range(currentMatrix[0],currentMatrix[2]+1):
                    for colcheck in range(currentMatrix[1],currentMatrix[3]+1):
                        number = sudokuGrid[rowcheck][colcheck]
                        if number in knockoutList:
                            knockoutList.remove(number)
                
                if (len(knockoutList) == 1):
                    sudokuGrid[row][column] = knockoutList[0]
                else:
                    sudokuGrid[row][column] = knockoutList
            
        
    displayGridcmd(sudokuGrid)

    print(solveSudoku(sudokuGrid))

def solveSudoku(sudokuGridFunctionParam):

    print("Entered Main Function")
    # displayGridcmd(sudokuGridFunctionParam)

    for row in range(0,9):
        for col in range(0,9):
            
            print("Entering Master Loop for Recursion")
            print("row:{}".format(row))
            print("col:{}".format(col))
            input()
            if type(sudokuGridFunctionParam[row][col]) == int:
                continue
            if type(sudokuGridFunctionParam[row][col]) == list:
                elementList = list(sudokuGridFunctionParam[row][col])
                
                
                print("List has been Found: Iterating")
                print("List:{}".format(elementList))
                displayGridcmd(sudokuGridFunctionParam)    


                #All magic happens here in this loop

                
                for element in elementList:
                    elementAlreadyFixedFlag = False
                    #check if element is feasible
                    
                    #check row
                    currentrow = list(sudokuGridFunctionParam[row])
                    for rowelement in currentrow:

                        if element == rowelement:
                            #cannot use this element in this iteration
                            elementAlreadyFixedFlag = True
                            break
                    
                    if elementAlreadyFixedFlag == True:
                        continue
                    
                    #check column
                    columnNumber = col
                    for rowNumber in range(0,9):
                        number = sudokuGridFunctionParam[rowNumber][columnNumber]
                        if number == element:
                            #cannot use this element in this iteration
                            elementAlreadyFixedFlag = True
                            break
                    
                    if elementAlreadyFixedFlag == True:
                        continue

                    #check 3*3 matrix
                    currentMatrix = 0
                    for matrix in matrixLimit:
                        
                        rowStart = matrix[0] 
                        colStart = matrix[1]

                        rowEnd = matrix[2]
                        colEnd = matrix[3]

                        if row >= rowStart and row<=rowEnd:
                            if col >= colStart and col <=colEnd:
                                currentMatrix = list(matrix)
                                print("CHecking matrix Found logic")
                                print(currentMatrix)
                                print(row)
                                print(col)
                                # input()
                                break
                                #breaking out of matrix limit loop, as the matrix in which the element belongs has been found
                    print(elementList)
                    print("entering 3*3 check")
                    for rowcheck in range(currentMatrix[0],currentMatrix[2]+1):
                        for colcheck in range(currentMatrix[1],currentMatrix[3]+1):
                            number = sudokuGridFunctionParam[rowcheck][colcheck]
                            if number == element:
                                #cannot use this element in this iteration, breaking out of the loop
                                elementAlreadyFixedFlag = True
                                break
                        
                        #breaking out of the 'row' loop if element found
                        if elementAlreadyFixedFlag == True:
                            break
                    
                    if elementAlreadyFixedFlag == True:
                        continue
                        #moving on to the next element



                    print("Fixing Element Here")
                    print("Row + {}".format(row))
                    print("COLumn: {}".format(col))

                    backup = sudokuGridFunctionParam[row][col]
                    sudokuGridFunctionParam[row][col] = element
                    
                    
                    displayGridcmd(sudokuGridFunctionParam)

                    #recursion happens here
                    if(solveSudoku(sudokuGridFunctionParam) == True):
                        displayGridcmd(sudokuGridFunctionParam)
                        # input()
                        return True
                    else:
                        sudokuGridFunctionParam[row][col] = list(backup)
                        continue
                        #we move on to the next element in the list of the current block

                print("FALSE!! DENIED!! ROLLING BACK")
                # displayGridcmd(sudokuGridFunctionParam) 
                return False

        #The logic has gone through all the entries and found no list. Hence the sudoku is solved. Returning True  
        displayGridcmd(sudokuGridFunctionParam)
    displayGridcmd(sudokuGridFunctionParam)
    input()
    input()
    print('waaaaaaaaaaaiiiiiiiiiiiiiiiiiiiiiiitttttttttttttttttttttttttttttttttttttttttt')
    return True





if __name__ == '__main__':
    main()