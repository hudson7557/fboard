# Test case 1, O wins

board_1 = FBoard()
board_1.print_board()
board_1.get_game_state()
board_1.move_o(7, 0, 6, 1)  # moving o's in general
board_1.move_o(7, 2, 6, 3)
board_1.move_o(7, 4, 6, 5)
board_1.move_o(7, 6, 6, 7)
board_1.move_o(6, 7, 7, 6)  # attempting an illegal move of going backwards
board_1.move_o(6, 7, 5, 8)  # attempting an out of bounds move
board_1.move_o(6, 7, 5, 6)
board_1.move_o(5, 6, 4, 7)
board_1.move_o(4, 7, 3, 6)
board_1.move_o(3, 6, 2, 5)
board_1.move_x(1, 2)  # x finally busts a move
board_1.move_x(0, 1)  # x can move backwards
board_1.move_x(1, -1)  # x cannot move out of bounds
board_1.move_x(1, 2)
board_1.move_x(2, 3)
board_1.move_x(3, 4)
board_1.move_o(6, 5, 5, 6)
board_1.move_o(5, 6, 4, 5)
board_1.move_o(6, 1, 5, 0)
board_1.move_o(5, 0, 4, 1)
board_1.move_o(4, 1, 3, 2)
board_1.move_o(3, 2, 2, 3)
board_1.move_o(6, 3, 5, 4)
board_1.move_o(5, 4, 4, 3)  # should trap X and set game_state to "O_WON"
board_1.move_o(5, 4, 4, 3)
board_1.move_x(3, 4)  # no one can move now that someone has won


# Test case 2, x wins
board_1 = FBoard()
board_1.print_board()
board_1.get_game_state()
board_1.move_o(7, 0, 6, 1)  # moving o's in general
board_1.move_o(7, 2, 6, 3)
board_1.move_o(7, 4, 6, 5)
board_1.move_o(7, 6, 6, 7)
board_1.move_o(6, 7, 7, 6)  # attempting an illegal move of going backwards
board_1.move_o(6, 7, 5, 8)  # attempting an out of bounds move
board_1.move_o(6, 7, 5, 6)
board_1.move_o(5, 6, 4, 7)
board_1.move_o(4, 7, 3, 6)
board_1.move_o(3, 6, 2, 5)
board_1.move_x(1, 2)  # x finally busts a move
board_1.move_x(0, 1)  # x can move backwards
board_1.move_x(1, -1)  # x cannot move out of bounds
board_1.move_x(1, 2)
board_1.move_x(2, 3)
board_1.move_x(3, 4)
board_1.move_x(4, 3)
board_1.move_x(3, 2)  # x feels scared and backs up
board_1.move_x(4, 1)
board_1.move_x(5, 0)
board_1.move_x(6, 1)  # x tries to jump on O but this aint checkers son!
board_1.move_o(6, 1, 5, 2)  # O politely moves out of the way.
board_1.move_x(7, 2)  # x gets excited and tries to jump two spaces, doesn't work.
board_1.move_x(6, 1)
board_1.move_x(7, 0)
board_1.move_x(6, 1)  # checking to make sure the game ends when someone has won.

# test case 3 x is trapped by ob and o's
board_1 = FBoard()
board_1.print_board()
board_1.get_game_state()
board_1.move_o(7, 0, 6, 1)  # moving o's in general
board_1.move_o(7, 2, 6, 3)
board_1.move_o(7, 4, 6, 5)
board_1.move_o(7, 6, 6, 7)
board_1.move_x(1, 2)  # x finally busts a move
board_1.move_x(0, 1)  # x can move backwards
board_1.move_x(1, -1)  # x cannot move out of bounds
board_1.move_x(1, 2)
board_1.move_x(2, 1)
board_1.move_x(3, 0)
board_1.move_o(6, 1, 5, 0)
board_1.move_o(5, 0, 4, 1)
board_1.move_o(6, 3, 5, 2)
board_1.move_o(5, 2, 4, 3)
board_1.move_o(4, 3, 3, 2)
board_1.move_o(3, 2, 2, 1)
