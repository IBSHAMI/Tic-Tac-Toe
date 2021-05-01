from player1 import Player1
from player2 import Player2

p1 = Player1()
p2 = Player2()
game_turns = 0
game_board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
places_taken = []


def game_board_printing(game_board):
    line = ""
    for i in range(len(game_board)):
        if i in [2, 5, 8]:
            line += game_board[i]
            print(line)
            line = ""
        else:
            line += f"{game_board[i]} , "


def update_game_board(player1_moves, player2_moves):
    global game_board
    game_board = []
    for i in range(9):
        if i in player2_moves:
            game_board.append("O")
        elif i in player1_moves:
            game_board.append("X")
        else:
            game_board.append("-")


game_is_on = input("Do you want to start the game? (yes or no) ").lower()

while game_is_on == "yes":

    while game_turns < 9:
        wait_player1_move = True
        while wait_player1_move:
            game_board_printing(game_board)
            player1_move = int(input("player 1 move, choose the number between 1,9? "))
            if player1_move > 9 or player1_move <= 0:
                print("Please choose a number between 1 and 9 ")
            elif player1_move in places_taken:
                print("Place already chosen, choose another number ")
            else:
                p1.player_moves.append(player1_move - 1)
                places_taken.append(player1_move - 1)
                print(places_taken)
                game_turns += 1
                wait_player1_move = False

        update_game_board(p1.player_moves, p2.player_moves)

        if game_turns == 9:
            game_board_printing(game_board)
            break

        wait_player2_move = True
        while wait_player2_move:
            game_board_printing(game_board)
            player2_move = int(input("player 2 move, choose the number between 1,9? "))
            if player2_move > 9 or player2_move <= 0:
                print("Please choose a number between 1 and 9 ")
            elif player2_move in places_taken:
                print("Place already chosen, choose another number ")
            else:
                p2.player_moves.append(player2_move - 1)
                places_taken.append(player2_move - 1)
                game_turns += 1
                print(places_taken)
                wait_player2_move = False
        update_game_board(p1.player_moves, p2.player_moves)


    game_is_on = "off"
