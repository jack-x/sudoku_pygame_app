import builder
import random
import os
import datetime

def generateExtension():
    alphabets = list('abcdefghijklmnopqrstuvwxyz')
    name =['x'] * 10

    for x in range(0,10):
        name[x] = random.choice(alphabets)
    return ''.join(name)

def main():
    a= datetime.datetime.now()

    filename = 'ThousandSudokus-' + generateExtension() +'.txt'
    if os.path.exists(filename) == True:
        filename = 'ThousandSudokus-' + generateExtension() +'.txt'
    File = open(filename,'w')
    
    x = 0
    while x<1000:
        x+=1
        sudoku = builder.buildSudoku()
        for row in sudoku:
            line = ''
            for num in row:
                line = line+str(num)
            File.write(line+"\n")
        File.write('\n\n')
    File.close()  
        

    b = datetime.datetime.now()

    print("Time Taken for this process: ")
    print(b-a)

if __name__ == "__main__":
    main()