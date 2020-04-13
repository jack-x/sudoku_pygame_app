import random
import Solver
from Solver import solveSudokuConcise,solveSudoku,positionalListGenerator, displayGridcmd

def main():
    line = [0,0,0,0,0,0,0,0,0]
    
    sudokuGrid = [0]*9
    for x in range(0,9):
        sudokuGrid[x] = list(line)    

    knockoutlist = [1,2,3,4,5,6,7,8,9]
    for row in range(0,3):
        for column in range(0,3):
            number = random.choice(knockoutlist)
            sudokuGrid[row][column] = number
            knockoutlist.remove(number)
    
    knockoutlist = [1,2,3,4,5,6,7,8,9]
    for row in range(3,6):
        for column in range(3,6):
            number = random.choice(knockoutlist)
            sudokuGrid[row][column] = number
            knockoutlist.remove(number)
    
    knockoutlist = [1,2,3,4,5,6,7,8,9]
    for row in range(6,9):
        for column in range(6,9):
            number = random.choice(knockoutlist)
            sudokuGrid[row][column] = number
            knockoutlist.remove(number)

    preppedSudokuGrid = positionalListGenerator(sudokuGrid)
    
    finalSudoku = solveSudokuConcise(preppedSudokuGrid)

    displayGridcmd(finalSudoku)

def buildSudoku():
    line = [0,0,0,0,0,0,0,0,0]
    
    sudokuGrid = [0]*9
    for x in range(0,9):
        sudokuGrid[x] = list(line)    

    knockoutlist = [1,2,3,4,5,6,7,8,9]
    for row in range(0,3):
        for column in range(0,3):
            number = random.choice(knockoutlist)
            sudokuGrid[row][column] = number
            knockoutlist.remove(number)
    
    knockoutlist = [1,2,3,4,5,6,7,8,9]
    for row in range(3,6):
        for column in range(3,6):
            number = random.choice(knockoutlist)
            sudokuGrid[row][column] = number
            knockoutlist.remove(number)
    
    knockoutlist = [1,2,3,4,5,6,7,8,9]
    for row in range(6,9):
        for column in range(6,9):
            number = random.choice(knockoutlist)
            sudokuGrid[row][column] = number
            knockoutlist.remove(number)

    preppedSudokuGrid = positionalListGenerator(sudokuGrid)
    
    finalSudoku = solveSudokuConcise(preppedSudokuGrid)

    return finalSudoku

    









if __name__=='__main__':
    main()