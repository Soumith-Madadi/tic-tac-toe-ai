import time
import math
import os
import random
board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
user = 'O'
computer = 'X'
turns = 1

def display_board(board):

    return print('+-------+-------+-------+\n|       |       |       |\n|   '+board[0]+'   |   '+board[1]+'   |   '+board[2]+'   |\n|       |       |       |\n''+-------+-------+-------+\n''|       |       |       |\n|   '+board[3]+'   |   '+board[4]+'   |   '+board[5]+'   |\n|       |       |       |\n''+-------+-------+-------+\n|       |       |       |\n|   '+board[6]+'   |   '+board[7]+'   |   '+board[8]+'   |\n|       |       |       |\n''+-------+-------+-------+\n')


def reset_board():
    global board
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return board

def evaluate(board):
    if victory_for(board, 'O'):
        score = -1
    elif victory_for(board, 'X'):
        score = +1
    else:
        score = 0
    return score
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

def available_spots(board):
    result = []
    for i, j in enumerate(board):
        hi = i + 1
        if j == '1' or j == '2' or j == '3'or j == '4' or j == '5' or j == '6' or j == '7' or j == '8' or j == '9':
            result.append(i)
    return result


def minimax(board, depth, player):
    #make_list_of_free_fields(board)
    max_player = 'X'
    other_player = 'O' if player == "X" else 'X'
    if depth == 0 or victory_for(board, player) == True or victory_for(board, other_player) == True:
        score = evaluate(board)
        return {'position': -1, 'score': score}
    #elif len(free_squares) == 0:
    #    return {'position': None, 'score': 0}
    if max_player == player:
        best = {'position': -1, 'score': -math.inf}
    else:
        best = {'position': -1, 'score': math.inf}
    #make_list_of_free_fields(board)
    for all in available_spots(board):
            #if all in free_squares:
                #make_list_of_free_fields(board)
            save = board[all]
            board[all] = player
            score = minimax(board, depth-1, other_player)
                #make_list_of_free_fields(board)
            board[all] = save
            #print('here', all)
            score['position'] = all
            if player == max_player:
                if score['score'] > best['score']:
                    best = score
                    print(best)
            else:
                if score['score'] < best['score']:
                    best = score
                    print(best)

    print(best)
    return best


def ai(board):
    make_list_of_free_fields(board)
    depth = len(free_squares)
    if depth == 0 or victory_for(board, 'O') or victory_for(board, 'X'):
        return
    print('AI move: ')
    square = minimax(board,depth, 'X')['position']
    #print(square)

    #choice = board.index(free_squares[square])
    board[square] = 'X'

    return


def enter_move(board):
    try:
        user_move = int(input("Enter your move: "))
        if 0 < user_move < 10:
            if user_move == 1 and not board[0] == 'X' and not board[0] == 'O':
                board[0] = 'O'
                return
            elif user_move == 2 and board[1] != 'X' and board[1] != 'O':
                board[1] = 'O'
                return
            elif user_move == 3 and board[2] != 'X' and board[2] != 'O':
                board[2] = 'O'
                return
            elif user_move == 4 and not board[3] == 'X' and not board[3] == 'O':
                board[3] = 'O'
                return
            elif user_move == 5 and not board[4] == 'X' and not board[4] == 'O':
                board[4] = 'O'
                return
            elif user_move == 6 and not board[5] == 'X' and not board[5] == 'O':
                board[5] = 'O'
                return
            elif user_move == 7 and not board[6] == 'X' and not board[6] == 'O':
                board[6] = 'O'
                return
            elif user_move == 8 and not board[7] == 'X' and not board[7] == 'O':
                board[7] = 'O'
                return
            elif user_move == 9 and not board[8] == 'X' and not board[8] == 'O':
                board[8] = 'O'
                return

            else:
                print("That number is taken!")
                return enter_move(board)
        else:
            print("That number is out of the range!")
            return enter_move(board)
    except ValueError:
        print('Wrong Value')
        return enter_move(board)
    except:
        print('I don\'t know what happened')
        return enter_move(board)

def two_player_enter_move(board, user):
    player = 'Player 1' if user == "O" else 'Player 2'
    try:
        user_move = int(input(player + " enter your move: "))
        if 0 < user_move < 10:
            if user_move == 1 and not board[0] == 'X' and not board[0] == 'O':
                board[0] = user
                return
            elif user_move == 2 and board[1] != 'X' and board[1] != 'O':
                board[1] = user
                return
            elif user_move == 3 and board[2] != 'X' and board[2] != 'O':
                board[2] = user
                return
            elif user_move == 4 and not board[3] == 'X' and not board[3] == 'O':
                board[3] = user
                return
            elif user_move == 5 and not board[4] == 'X' and not board[4] == 'O':
                board[4] = user
                return
            elif user_move == 6 and not board[5] == 'X' and not board[5] == 'O':
                board[5] = user
                return
            elif user_move == 7 and not board[6] == 'X' and not board[6] == 'O':
                board[6] = user
                return
            elif user_move == 8 and not board[7] == 'X' and not board[7] == 'O':
                board[7] = user
                return
            elif user_move == 9 and not board[8] == 'X' and not board[8] == 'O':
                board[8] = user
                return

            else:
                print("That number is taken!")
                return two_player_enter_move(board, user)
        else:
            print("That number is out of the range!")
            return two_player_enter_move(board, user)
    except ValueError:
        print('Wrong Value')
        return two_player_enter_move(board, user)
    except:
        print('I don\'t know what happened')
        return two_player_enter_move(board, user)
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.

#free_squares = []
def make_list_of_free_fields(board):
    global free_squares
    free_squares = []
    for b in range(9):
        if board[b] == 'X' or board[b] == 'O':
            continue
        else:
            free_squares.append(b)



    return free_squares
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):

    if board[0] == sign and board[1] == sign and board[2] == sign:
            return True
    elif board[3] == sign and board[4] == sign and board[5] == sign:
            return True
    elif board[6] == sign and board[7] == sign and board[8] == sign:
            return True
    elif board[0] == sign and board[3] == sign and board[6] == sign:
            return True
    elif board[1] == sign and board[4] == sign and board[7] == sign:
            return True
    elif board[2] == sign and board[5] == sign and board[8] == sign:
            return True
    elif board[0] == sign and board[4] == sign and board[8] == sign:
            return True
    elif board[2] == sign and board[4] == sign and board[6] == sign:
            return True
    else:
        return False



    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    make_list_of_free_fields(board)
    while True:
        rando = random.randrange(9)
        if rando not in free_squares:
            continue
        else:
            print('Computer Move: ')
            board[rando] = 'X'
            return



    # The function draws the computer's move and updates the board.



def play():
    print("Welcome to Tic Tac Toe! \n")
    make_list_of_free_fields(board)
    opponent = input("Do you want to play a two player game (two) or against a bot or an ai: ")
    opponent = opponent.lower()
    display_board(board)
    if opponent == 'bot':
        while free_squares != []:
            enter_move(board)
            display_board(board)
            make_list_of_free_fields(board)
            if victory_for(board, user) == True:
                print("You Won!")
                again = str(input('Do you want to play again (y/n)'))
                if again == 'y':
                    os.system('cls')
                    reset_board()
                    play()
                elif again == 'Y':
                    os.system('cls')
                    reset_board()
                    play()
                else:
                    quit()
            else:
                make_list_of_free_fields(board)
                time.sleep(1)
            make_list_of_free_fields(board)
            if free_squares == []:
                continue
            draw_move(board)
            display_board(board)
            make_list_of_free_fields(board)
            if free_squares == []:
                continue
            if victory_for(board, computer) == True:
                print("Computer Won!")
                again1 = str(input('Do you want to play again (y/n)'))
                if again1 == 'y':
                    os.system('cls')
                    reset_board()
                    play()
                elif again1 == 'Y':
                    os.system('cls')
                    reset_board()
                    play()
                else:
                    quit()
            else:
                make_list_of_free_fields(board)



        else:
            print("It's a tie")
            again2 = str(input('Do you want to play again (y/n)'))
            if again2 == 'y':
                os.system('cls')
                reset_board()
                play()
            elif again2 == 'Y':
                os.system('cls')
                reset_board()
                play()
            else:
                quit()
    elif opponent == 'ai':
        while free_squares != []:
            enter_move(board)
            display_board(board)
            if victory_for(board, user) == True:
                display_board(board)
                print("You Won!")
                again3 = str(input('Do you want to play again (y/n)'))
                if again3 == 'y':
                    os.system('cls')
                    reset_board()
                    play()
                elif again3 == 'Y':
                    os.system('cls')
                    reset_board()
                    play()
                else:
                    quit()
            else:
                make_list_of_free_fields(board)
                time.sleep(1)
            make_list_of_free_fields(board)
            if free_squares == []:
                continue


            ai(board)
            display_board(board)

            if victory_for(board, computer) == True:
                print("AI won!")
                again4 = str(input('Do you want to play again (y/n)'))
                if again4 == 'y':
                    os.system('cls')
                    reset_board()
                    play()
                elif again4 == 'Y':
                    os.system('cls')
                    reset_board()
                    play()
                else:
                    quit()
            else:
                make_list_of_free_fields(board)



        else:
            print("It's a tie")
            again5 = str(input('Do you want to play again (y/n)'))
            if again5 == 'y':
                os.system('cls')
                reset_board()
                play()
            elif again5 == 'Y':
                os.system('cls')
                reset_board()
                play()
            else:
                quit()
    elif opponent == 'two':
        player1 = 'O'
        player2 = 'X'
        print('Player 1 is O\'s and Player 2 is X\'s\n')
        while free_squares != []:
            two_player_enter_move(board, player1)
            display_board(board)
            if victory_for(board, player1) == True:
                display_board(board)
                print("Player 1 Won!")
                again5 = str(input('Do you want to play again (y/n)'))
                if again5 == 'y':
                    os.system('cls')
                    reset_board()
                    play()
                elif again5 == 'Y':
                    os.system('cls')
                    reset_board()
                    play()
                else:
                    quit()
            else:
                make_list_of_free_fields(board)
            make_list_of_free_fields(board)
            if free_squares == []:
                continue


            two_player_enter_move(board, player2)
            display_board(board)

            if victory_for(board, player2) == True:
                print("Player 2 Won!")
                again6 = str(input('Do you want to play again (y/n)'))
                if again6 == 'y':
                    os.system('cls')
                    reset_board()
                    play()
                elif again6 == 'Y':
                    os.system('cls')
                    reset_board()
                    play()
                else:
                    quit()
            else:
                make_list_of_free_fields(board)



        else:
            print("It's a tie")
            again5 = str(input('Do you want to play again (y/n)'))
            if again5 == 'y':
                os.system('cls')
                reset_board()
                play()
            elif again5 == 'Y':
                os.system('cls')
                reset_board()
                play()
            else:
                quit()
    else:
        os.system('cls')
        play()

play()
