puzzle = [[0,0,0,0,0,0,0,0,0],
          [0,3,0,0,0,0,1,6,0],
          [0,6,7,0,3,5,0,0,4],
          [6,0,8,1,2,0,9,0,0],
          [0,9,0,0,8,0,0,3,0],
          [0,0,2,0,7,9,8,0,6],
          [8,0,0,6,9,0,3,5,0],
          [0,2,6,0,0,0,0,9,0],
          [0,0,0,0,0,0,0,0,0]]

possible_nums = [1,2,3,4,5,6,7,8,9]

#function to draw formatted sudoku puzzle
def draw_puzzle(puzzle):
    for i in range(9):
        print(puzzle[i])


#function that returns list of numbers that are in a column
def get_column(index,puzzle):
    column_list = []
    for row in range(9):
        column_list.append(puzzle[row][index])
    return column_list


#function to check what numbers are availble horizontally for blank space
def available_nums_in_row(row_list):
    available_nums = [numbers for numbers in possible_nums if numbers not in row_list]
    return available_nums
    # print(available_nums_in_row(puzzle[1]))


#function to check what numbers are available vertically for blank space
def available_nums_in_column(column_list):
    available_nums = [numbers for numbers in possible_nums if numbers not in column_list]
    return available_nums


#function to check what square were currently checking in
def get_square(row, column):
    if 0 <= row <= 2:
        if 0 <= column <= 2:
            square = 'one'
        if 3 <= column <= 5:
            square = 'two'
        if 6 <= column <= 8:
            square = 'three'
    if 3 <= row <= 5:
        if 0 <= column <= 2:
            square = 'four'
        if 3 <= column <= 5:
            square = 'five'
        if 6 <= column <= 8:
            square = 'six'
    if 6 <= row <= 8:
        if 0 <= column <= 2:
            square = 'seven'
        if 3 <= column <= 5:
            square = 'eight'
        if 6 <= column <= 8:
            square = 'nine'
    return square


#function to check what numbers are in 3x3 square for blank space
def get_nums_in_square(square, puzzle):
    available_nums = []
    if square == 'one':
        for row in range(3):
            for col in range(3):
                available_nums.append(puzzle[row][col])
    elif square == 'two':
        for row in range(3):
            for col in range(3, 6):
                available_nums.append(puzzle[row][col])
    elif square == 'three':
        for row in range(3):
            for col in range(6,9):
                available_nums.append(puzzle[row][col])
    elif square == 'four':
        for row in range(3,6):
            for col in range(3):
                available_nums.append(puzzle[row][col])
    elif square == 'five':
        for row in range(3,6):
            for col in range(3,6):
                available_nums.append(puzzle[row][col])
    elif square == 'six':
        for row in range(3,6):
            for col in range(6,9):
                available_nums.append(puzzle[row][col])
    elif square == 'seven':
        for row in range(6,9):
            for col in range(3):
                available_nums.append(puzzle[row][col])
    elif square == 'eight':
        for row in range(6,9):
            for col in range(3,6):
                available_nums.append(puzzle[row][col])
    elif square == 'nine':
        for row in range(6,9):
            for col in range(6,9):
                available_nums.append(puzzle[row][col])
    return available_nums


#function to check what numbers are available in given square
def available_nums_in_square(square_list):
    available_nums = [numbers for numbers in possible_nums if numbers not in square_list]
    return available_nums


#Create list of available nums based on what numbers are in vertical, horizontal and square checks.
def combined_available_nums(row_list,column_list,square_list):
    available_nums = [numbers for numbers in row_list if numbers in column_list and numbers in square_list]
    return available_nums

# print(get_column(1, puzzle))
for row in range(9):
    column = 0
    for number in puzzle[row]:
        if number == 0:

            available_nums_horizontal = available_nums_in_row(puzzle[row])  # If a blank space is found check row for available numbers
            available_nums_vertical = available_nums_in_column(get_column(column, puzzle))  # then check column for available numbers
            available_nums_square = available_nums_in_square(get_nums_in_square(get_square(row, column),puzzle))    #then check square for available numbers

            available_nums_combined = combined_available_nums(available_nums_horizontal,available_nums_vertical, # then create a list of numbers that are available in row, column, and square
                                                              available_nums_square)

            if len(available_nums_combined) > 0:
                puzzle[row][column] = available_nums_combined[0] # if there are numbers available, insert the first into the blank spot
                column += 1


            # if there are no numbers available, this means there is a mistake somewhere in the puzzle --
            # step backward try next number in available numbers list and proceed.

            else:
                if column >= 1:
                    column -= 1
                else:
                    row -= 1
                    column = 8
        else:
            pass


        draw_puzzle(puzzle)
        print("")
        print(row)
        print(column)
        print("____________________")
        # print(available_nums_horizontal,available_nums_vertical, available_nums_combined)

