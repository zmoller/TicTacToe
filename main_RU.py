def init():
    board_array = []
    for _ in range(9):
        board_array.append(' ')
    return board_array


def draw(board_array):
    i = 0
    for row in range(9):
        for col in range(17):
            if col == 5 or col == 11:
                print('|', end='')
            elif row == 2 or row == 5:
                print('_', end='')
            elif (row == 1 or row == 4 or row == 7) and (col == 2 or col == 8 or col == 14):
                print(board_array[i], end='')
                i += 1
            else:
                print(' ', end='')
        print()


def player_choice(board_array, player):
    if player:
        call_to_action = 'Игрок X:'
    else:
        call_to_action = 'Игрок O:'
    print('\n', call_to_action, '\nсделай ход, введя число 1-9 (0 - перерисовать поле): ', sep='', end='')
    while True:
        choice = int(input())
        if 0 < choice <= 9:
            if board_array[choice - 1] == ' ':
                return choice
            else:
                print('Другой игрок это поле уже занял! Выбери другой ход.')
                print('\n', call_to_action, '\nсделай ход, введя число 1-9 (0 - перерисовать поле): ', sep='', end='')
        elif choice == 0:
            draw(board_array)
            print('\n', call_to_action, '\nсделай ход, введя число 1-9 (0 - перерисовать поле)', sep='', end='')
        else:
            print('Неверный ход!')
            print('\n', call_to_action, '\nсделай ход, введя число 1-9 (0 - перерисовать поле): ', sep='', end='')


def update_board(board_array, move, player):
    if board_array[move - 1] == ' ':
        if player:
            board_array[move - 1] = 'X'
        else:
            board_array[move - 1] = 'O'
    return board_array


def check_win(board_array):
    win_states = [123, 456, 789, 147, 258, 369, 159, 357]
    win_state_check = ''
    win = False
    for win_state in win_states:
        for _ in (str(win_state)):
            win_state_check += board_array[int(_) - 1]
        if win_state_check == 'XXX' or win_state_check == 'OOO':
            win = True
            break
        win_state_check = ''
    return win


def game(board_array):
    board = board_array
    current_move = 1
    player_x = True

    draw(board)
    while current_move <= 9:
        current_player_move = player_choice(board, player_x)
        board = update_board(board, current_player_move, player_x)
        draw(board)

        if current_move >= 5:
            win = check_win(board)
            if win:
                if player_x:
                    print('Игрок X выиграл!')
                    return 1
                else:
                    print('Игрок O выиграл!')
                    return 2

        player_x = not player_x
        current_move += 1
        if current_move == 10:
            print('Ничья!')
            return 0


def main():
    games = int(input('Сколько партий желаете сыграть? '))
    player_x_score = 0
    player_o_score = 0

    for match in range(games):
        print('Игра', (match + 1), 'начинается')
        state = game(init())
        if state == 1:
            player_x_score += 1
        elif state == 2:
            player_o_score += 1
        print('\nОчки игрока X:', player_x_score)
        print('Очки игрока O:', player_o_score)


main()
close = input('\nНажми любую клавишу -> ENTER для выхода: ')