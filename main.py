class Player:
    def __init__(self):
        self.player_status = None
        self.player_moves = []


p1 = Player()
p2 = Player()
game_turns = 0
game_board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
game_status = None
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


def check_game_status(player_symbol):
    global game_board
    if game_board.count(player_symbol) < 3:
        return None
    else:
        if not any(i != player_symbol for i in game_board[:3]):
            return True
        elif not any(i != player_symbol for i in game_board[0:9:4]):
            return True
        elif not any(i != player_symbol for i in game_board[0:7:3]):
            return True
        elif not any(i != player_symbol for i in game_board[1:8:3]):
            return True
        elif not any(i != player_symbol for i in game_board[2:7:2]):
            return True
        elif not any(i != player_symbol for i in game_board[2:9:3]):
            return True
        elif not any(i != player_symbol for i in game_board[3:6]):
            return True
        elif not any(i != player_symbol for i in game_board[6:9]):
            return True
        else:
            return None


def game_outcome_check():
    global game_status, game_turns
    if game_turns == 9:
        game_status = "Draw"
    elif game_status is not None:
        return "Game finished"



game_is_on = input("Do you want to start the game? (yes or no) ").lower()

while game_is_on == "yes":

    while game_turns < 9:
        wait_player1_move = True
        while wait_player1_move:
            game_board_printing(game_board)
            player1_move = int(input("player 1 move, choose the number between 1,9? ")) - 1
            if player1_move > 9 or player1_move < 0:
                print("Please choose a number between 1 and 9 ")
            elif player1_move in places_taken:
                print("Place already chosen, choose another number ")
            else:
                p1.player_moves.append(player1_move)
                places_taken.append(player1_move)
                update_game_board(p1.player_moves, p2.player_moves)
                game_turns += 1
                p1.player_status = check_game_status("X")
                if p1.player_status:
                    game_status = "Player 1 win"
                wait_player1_move = False

        end = game_outcome_check()
        if end == "Game finished":
            break


        wait_player2_move = True
        while wait_player2_move:
            game_board_printing(game_board)
            player2_move = int(input("player 2 move, choose the number between 1,9? ")) - 1
            if player2_move > 9 or player2_move < 0:
                print("Please choose a number between 1 and 9 ")
            elif player2_move in places_taken:
                print("Place already chosen, choose another number ")
            else:
                p2.player_moves.append(player2_move)
                places_taken.append(player2_move)
                update_game_board(p1.player_moves, p2.player_moves)
                game_turns += 1
                p2.player_status = check_game_status("O")
                if p2.player_status:
                    game_status = "Player 2 win"
                wait_player2_move = False

        end = game_outcome_check()
        if end == "Game finished":
            break

    game_board_printing(game_board)
    print(f"The game ended up with: {game_status}")
    game_is_on = "off"
