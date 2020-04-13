from builder import buildSudoku
from Solver import solveSudokuConcise,displayGridcmd, positionalListGenerator,displayGridcmdBlankSpace
import random

def createSudokuCopy(sudoku):

    copySudoku = [0]*9
    line = [0,0,0,0,0,0,0,0,0]
    for x in range(0,9):
        copySudoku[x] = list(line)

    for row in range(0,9):
        for column in range(0,9):
            copySudoku[row][column] = sudoku[row][column]
    
    return copySudoku

def createSudokuPuzzle(blanks=10):
    '''
    Creates a sudoku puzzle with specified number of empty fields
    '''
    sudoku = buildSudoku()
    print("NEW SUDOKU")
    displayGridcmd(sudoku)


    comparisonSudoku = createSudokuCopy(sudoku)
    # line = [0,0,0,0,0,0,0,0,0]
    # for x in range(0,9):
    #     comparisonSudoku[x] = list(line)

    # for row in range(0,9):
    #     for column in range(0,9):
    #         comparisonSudoku[row][column] = sudoku[row][column]

    removedList = []
    numberList = [0,1,2,3,4,5,6,7,8]
    x = 0
    while x < blanks:
        randomRow = random.choice(numberList)
        randomColumn = random.choice(numberList)

        pair = (randomRow,randomColumn)

        if pair in removedList:
            continue
        removedList.append(pair)
        
        temp = sudoku[randomRow][randomColumn]
        sudoku[randomRow][randomColumn] = 0
    
    
        calculationSudoku = createSudokuCopy(sudoku)
        generatePositionList = positionalListGenerator(calculationSudoku)
        solvedSudoku = solveSudokuConcise(generatePositionList)
        
        # print("See if returned sudoku is solved")
        # displayGridcmd(solvedSudoku)
        # print()
        # print()
        # input()

        # print("See the final comparison value")
        # print(solvedSudoku == comparisonSudoku)
        # input()

        if solvedSudoku == comparisonSudoku:
            # sudoku[randomRow][randomColumn] = 0
            #success
            x+=1
            continue
        else:
            #failure
            #rollback
            print("rollback")
            # input()
            removedList.remove(pair)
            sudoku[randomRow][randomColumn] = temp
            continue
        
    return sudoku


def generatePuzzleSolution(blanks=10):
    '''
    Takes in number of blanks as input.
    Returns a tuple of length 2. Tuple includes sudoku puzzle with specified blanks, along with the completely solved sudoku.
    '''
    sudoku = buildSudoku()
    # print("NEW SUDOKU")
    # displayGridcmd(sudoku)


    comparisonSudoku = createSudokuCopy(sudoku)

    removedList = []
    numberList = [0,1,2,3,4,5,6,7,8]
    x = 0
    while x < blanks:
        randomRow = random.choice(numberList)
        randomColumn = random.choice(numberList)

        pair = (randomRow,randomColumn)

        if pair in removedList:
            continue
        removedList.append(pair)

        temp = sudoku[randomRow][randomColumn]
        sudoku[randomRow][randomColumn] = 0


        calculationSudoku = createSudokuCopy(sudoku)
        generatePositionList = positionalListGenerator(calculationSudoku)
        solvedSudoku = solveSudokuConcise(generatePositionList)

        if solvedSudoku == comparisonSudoku:
            # sudoku[randomRow][randomColumn] = 0
            #success
            x+=1
            continue
        else:
            #failure
            #rollback
            print("rollback")
            # input()
            removedList.remove(pair)
            sudoku[randomRow][randomColumn] = temp
            continue

    return (sudoku,solvedSudoku)






def main():
    newPuzzle =  generatePuzzleSolution(30)

    print("NEW PUZZLE")
    displayGridcmdBlankSpace(newPuzzle[0])

    # displayGridcmd(createSudokuPuzzle(10))

    print("SOLVING THE SUDOKU")
    solution = solveSudokuConcise(positionalListGenerator(newPuzzle[0]))
    displayGridcmd(solution)


if __name__ == "__main__":
    main()