puzzle = [
    [0, 0, 7, 5, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 7, 4, 0],
    [3, 8, 0, 0, 0, 7, 0, 0, 6],
    [0, 0, 4, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 4, 5, 8, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 1, 0, 0],
    [2, 0, 0, 6, 0, 0, 0, 9, 7],
    [0, 9, 5, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 1, 2, 0, 0]
]

#  function to draw formatted sudoku puzzle
def draw_puzzle(puzzle):
    for i in range(9):
        print(puzzle[i])
    print("")
    print("")


# Find next empty cell in puzzle --> return row, and column for use in other functions
def find_empty_cell(puzzle):
    for row in range(len(puzzle)):
        for col in range(len(puzzle[0])):
            if puzzle[row][col] == 0:
                return (row, col)
    return None


# start inserting numbers into empty cell to check if they're valid
# if valid, break loop and move on to next cell, else continue loop
# if loop is completed and no valid numbers are found --> Backtrack
def fill_cell(index):
    for number in range(1, 10):
        # If number is valid, insert number and break loop
        if number_is_valid(number, index):
            puzzle[index[0]][index[1]] = number
            break
        # if number is not valid, keep going through loop
        else:
            pass

# If number is not in row, column or square, return True -- else return False
def number_is_valid(number,index):
    vertical_list = []
    if horizontal_check(number, index[0]) and vertical_check(number, index[1]) and square_check(number, index[0], index[1]):
        return True
    else:
        return False


# If number is not already in row, return True, else False
def horizontal_check(number, row):
    if number not in puzzle[row]:
        return True
    else:
        return False


# If number is not already in column, return True, else False
def vertical_check(number, col):
    vertical_list = []
    for row in range(0, 9):
        vertical_list.append(puzzle[row][col])
    if number not in vertical_list:
        return True
    else:
        return False


#  Discern what square the cell belongs to --> if number not in square, return True, else False
def square_check(number, row, col):
    square_list = []
    if 0 <= row <= 2:
        if 0 <= col <= 2:
            for row in range(3):
                for col in range(3):
                    square_list.append(puzzle[row][col])
                    if number not in square_list:
                        return True
                    else:
                        return False
        if 3 <= col <= 5:
            for row in range(3):
                for col in range(3, 6):
                    square_list.append(puzzle[row][col])
                    if number not in square_list:
                        return True
                    else:
                        return False
        if 6 <= col <= 8:
            for row in range(3):
                for col in range(6, 9):
                    square_list.append(puzzle[row][col])
                    if number not in square_list:
                        return True
                    else:
                        return False
    elif 3 <= row <= 5:
        if 0 <= col <= 2:
            for row in range(3, 6):
                for col in range(3):
                    square_list.append(puzzle[row][col])
                    if number not in square_list:
                        return True
                    else:
                        return False
        if 3 <= col <= 5:
            for row in range(3, 6):
                for col in range(3, 6):
                    square_list.append(puzzle[row][col])
                    if number not in square_list:
                        return True
                    else:
                        return False
        if 6 <= col <= 8:
            for row in range(3, 6):
                for col in range(6, 9):
                    square_list.append(puzzle[row][col])
                    if number not in square_list:
                        return True
                    else:
                        return False
    elif 6 <= row <= 8:
        if 0 <= col <= 2:
            for row in range(6, 9):
                for col in range(3):
                    square_list.append(puzzle[row][col])
                    if number not in square_list:
                        return True
                    else:
                        return False
        if 3 <= col <= 5:
            for row in range(6, 9):
                for col in range(3, 6):
                    square_list.append(puzzle[row][col])
                    if number not in square_list:
                        return True
                    else:
                        return False
        if 6 <= col <= 8:
            for row in range(6, 9):
                for col in range(6, 9):
                    square_list.append(puzzle[row][col])
                    if number not in square_list:
                        return True
                    else:
                        return False

#Loop to solve puzzle
def solve_puzzle(puzzle):
    more_cells = find_empty_cell(puzzle)
    if not more_cells:
        return True
    else:
        row, col = more_cells

    #  Loop through values 1-9 to check is the value already exists in row, column, or square
    #  If value is valid, column or square, fill cell with value

    for number in range(1, 10):
        if number_is_valid(number, (row, col)):
            puzzle[row][col] = number

            # Run over solve loop using new board with added value
            if solve_puzzle(puzzle):
                return True

            # If there are no valid numbers --> solve_puzzle returns false and the last changed element is changed to 0
            # Then a new value is put in until we get to the end of the board.

            puzzle[row][col] = 0

    return False

solve_puzzle(puzzle)
draw_puzzle(puzzle)
