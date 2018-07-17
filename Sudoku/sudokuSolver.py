# Basic Rules of Sudoku
# 1. No 2 identical numbers can be in the same column, row, or square
# 2. All columns, rows, and squares must have the unique numbers 1 through 9
# 3. The playing board is 9x9, with 9 3x3


# List of Squares
# square 1 = 0,0 2,2
# square 2 = 0,3 2,5
# square 3 = 0,6 2,8
# square 4 = 3,0 5,2
# square 5 = 3,3 5,5
# square 6 = 3,6 5,8
# square 7 = 6,0 8,2
# square 8 = 6,3 8,5
# square 9 = 6,6 8,8


sudoku = []


def readSudoku():
    #keywordInput = input('Please input sudoku file')
    #sudokuFile = open(keywordInput, 'r', encoding='utf8')
    sudokuFile = open('sudoku.txt', 'r', encoding='utf8')
    for line in sudokuFile:
        num = line.strip().strip("[").strip("]").split(',')
        num = [int(i) for i in num]
        sudoku.append(num)
    sudokuFile.close

def pencilNums(columns, rows):
    pencilList = [1,2,3,4,5,6,7,8,9]
    # rowCheck
    for num in sudoku[columns]:
        if num != 0:
            if num in pencilList:
                pencilList.remove(num)
    # columnCheck
    for num in range(0,8):
        if sudoku[num][rows] != 0:
            if num in pencilList:
                pencilList.remove(num)
    # squareCheck
    sqX, sqY = 3 * (columns // 3), 3 * (rows // 3)
    for x in range(sqX, sqX + 3):
        for y in range(sqY, sqY + 3):
            if sudoku[x][y] != 0:
                if num in pencilList:
                    pencilList.remove(num)
    return pencilList


def solver():
    flag = True
    while(flag):
        flag = False
        for cols in range(0, 9):
            for rows in range(0, 9):
                if isinstance(sudoku[cols][rows], list):
                    flag = True
                    pencilNums(cols, rows)
                    if len(sudoku[cols][rows]) == 1:
                        sudoku[cols][rows] == sudoku[cols][rows][0]


def main():
    readSudoku()
    for columnCounter in range(0,8):
            while (True):
                try:
                    spot = sudoku[columnCounter].index(0)
                except ValueError:
                    print('lol im gay')
                    break
                sudoku[columnCounter][spot] = pencilNums(columnCounter, spot)
    for i in sudoku:
        print(i)



    solver()


main()