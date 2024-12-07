grid = [[0 for j in range(9)] for i in range(9)]

def main():
    try:
        while True:
            R,C,N = input("Enter Row/Column/Number: ").split("/")
            grid[int(R)][int(C)] = int(N)
    except EOFError as e:
        returnSolved()
def insertValidCheck(row, column, number, grid):
    if number in grid[row]:
        return False
    for m in range(9):
        if grid[m][column] == number:
            return False
    topLeftRow = row - (row % 3)
    topLeftColumn = column - (column % 3)

    for r in range(3):
        for c in range(3):
            if grid[topLeftRow + r][topLeftColumn + c] == number:
                return False
    return True

def inserter(grid, row, column):
    if column == 9:
        if row == 8:
            return True
        else:
            row += 1
            column = 0
    if grid[row][column] > 0:
        return inserter(grid, row, column + 1)

    for number in range(1, 10):
        if insertValidCheck(row, column, number, grid):
            grid[row][column] = number

            if inserter(grid, row, column + 1):
                return True

        grid[row][column] = 0

def returnSolved():
    if inserter(grid, 0, 0):
        for i in range(9):
            for j in range(9):
                print(grid[i][j], end=" ")
            print()
        return True
    else:
        print("We can't solve this SUDOKU!")

if __name__ == '__main__':
    main()




