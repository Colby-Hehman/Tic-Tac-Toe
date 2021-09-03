# Letters are eight spaces wide and seven rows tall. Board is 38 spaces wide and 23 rows tall
x = ''' \\     /
  \\   / 
   \\ /  
    X   
   / \\  
  /   \\ 
 /     \\'''
o = ''' ______ 
|      |
|      |
|      |
|      |
|      |
 ------ '''
board = '''            |            |            
            |            |            
            |            |            
    1       |      2     |       3    
            |            |            
            |            |            
            |            |            
------------|------------|------------
            |            |            
            |            |            
            |            |            
    4       |      5     |       6    
            |            |            
            |            |            
            |            |            
------------|------------|------------
            |            |            
            |            |            
            |            |            
    7       |      8     |       9    
            |            |            
            |            |            
            |            |            '''
x_split = x.split('\n')
o_split = o.split('\n')


# Translates the board into rows, then replaces the numbered area selected with the user's letter
def move(player, zone):
    global board
    board_split = board.split('\n')
    new_board_split = []
    if player == 'x':
        player = x_split
    else:
        player = o_split
    row = ''
    if zone in range(1, 4):
        row = board_split[0:7]
    elif zone in range(4, 7):
        row = board_split[8:15]
    else:
        row = board_split[16:23]
    column = zone
    while column > 3:
        column -= 3
    line_counter = 0
    new_row = []
    for line in row:
        index = 0
        newline = ''
        if column == 1:
            newline = line[0:2] + player[line_counter] + line[10:38]
        elif column == 2:
            newline = line[0:15] + player[line_counter] + line[23:38]
        else:
            newline = line[0:28] + player[line_counter] + line[35:37]
        line_counter += 1
        new_row.append(newline)
    if row == board_split[0:7]:
        new_board_split.append(new_row + board_split[7:23])
    elif row == board_split[8:15]:
        new_board_split.append(board_split[0:8] + new_row + board_split[15:23])
    else:
        new_board_split.append(board_split[0:16] + new_row)
    board = '\n'.join(new_board_split[0])


# Below is where the game is played
moves = 0
available_spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player1_moves = []
player2_moves = []
number_to_mark = ''
player1_letter = None
player2_letter = None
while player1_letter == None:
    acceptable_inputs = ['x', 'X', 'o', 'O']
    letter = input('player1, would you like to use an X or an O?')
    if letter.strip() in acceptable_inputs:
        player1_letter = letter.strip()
    else:
        print('\nNot a valid letter. Please try again!')
if player1_letter == 'x':
    player2_letter = 'o'
else:
    player2_letter = 'x'
while moves < 9:
    print(board + '\n')
    if moves % 2 == 0:
        player_turn = 'player1'
    else:
        player_turn = 'player2'
    try:
        number_to_mark = int(input(f'{player_turn}, what number would you like to mark?'))
    except ValueError:
        print('Invalid input')
        print('-' * 38)
        continue
    if len(str(number_to_mark)) == 1:
        if number_to_mark in available_spaces:
            if player_turn == 'player1':
                move(player1_letter, number_to_mark)
                available_spaces.remove(number_to_mark)
                player1_moves.append(number_to_mark)
                moves += 1
            else:
                move(player2_letter, number_to_mark)
                available_spaces.remove(number_to_mark)
                player2_moves.append(number_to_mark)
                moves += 1
        else:
            print("This area is already marked!")
    else:
        print("Invalid input")
    print('-' * 38)
    if moves > 4:
        correct = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        list_to_check = []
        game_won = False
        if player_turn == 'player1':
            list_to_check = player1_moves
        else:
            list_to_check = player2_moves
        for group in correct:
            correct_lttrs = []
            for letter in list_to_check:
                if letter in group:
                    correct_lttrs.append(letter)
            if len(correct_lttrs) == 3:
                game_won = True
                break
        if game_won is True:
            moves = 10
            print(board + '\n')
            print(f'{player_turn} has won the game!')


if moves == 9:
    print(board + '\n')
    print("\nIt's a tie!")

