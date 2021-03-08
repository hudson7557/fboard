# Author: Scott Hudson
# Date: 12/02/2019
# Description: FBoard class which contains an __init__ method allowing players
# to create a new 8x8 board, with o's at the bottom and an x at the top.
# Players can then use methods to move the x and o's, o's can only move
# diagonally up the board while x can move diagonally in any direction. Each
# time a player moves a win condition check is performed and the board is
# printed along with the current state of the game. Once the game is won it
# can no longer be changed.


class FBoard:
    """
    A class which is used to play the FBoard game.
    """

    def __init__(self):
        """
        A class __init__ which creates a game board made out of 8 lists of 8
        empty spaces. Each instance contains the board as ._board, the games
        current state as ._game_state, and keeps x's coordinates as
        ._location_x.
        """
        self._board = [[" ", " ", " ", "X", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " ", " "],
                       ["O", " ", "O", " ", "O", " ", "O", " "]]
        self._game_state = "UNFINISHED"
        self._location_x = [0, 3]

    def print_board(self):
        """
        Method that prints the board line by line and returns the board itself.
        """
        for num in range(8):
            print(self._board[num])

        return self._board

    def get_game_state(self):
        """
        Method which prints and returns the current state of the game.
        """
        print(self._game_state)
        return self._game_state

    def move_x(self, row_number, col_number):
        """
        A method which takes a row number and column number as arguments, if
        the move is allowed it moves X, changes ._location_x to it's new
        coordinates then runs win_conditions(), print_board(), and
        get_game_state().
        """

        # check that the move is inbounds.
        if 0 <= row_number <= 7 and 0 <= col_number <= 7:

            # check if the move makes x go left or right one position.
            if row_number - 1 == self._location_x[0] or\
                    row_number + 1 == self._location_x[0]:

                # check if the move makes x go up or down one position.
                if col_number - 1 == self._location_x[1] or\
                        col_number + 1 == self._location_x[1]:

                    # check if the game is unfinished and the space is open.
                    if self._game_state == "UNFINISHED" and\
                            self._board[row_number][col_number] == " ":

                        self._board[row_number][col_number] = "X"
                        self._board[self._location_x[0]][self._location_x[1]]\
                            = " "
                        self._location_x = [row_number, col_number]
                        self.win_conditions()
                        self.print_board()
                        self.get_game_state()
                        return True

                    else:

                        return False
                else:

                    return False

            else:

                return False

        else:

            return False

    def move_o(self, old_row, old_col, new_row, new_col):
        """
        A method which takes a row number and column number and uses them to
        target an O, it then uses the next two numbers to move o. If the move
        is allowed it moves that O to it's new coordinates, then runs
        win_conditions(), print_board(), and get_game_state().
        """

        # check that the move is inbounds.
        if 0 <= new_row <= 7 and 0 <= new_col <= 7:

            # check to make sure the user has targeted an O.
            if self._board[old_row][old_col] == "O":

                # check to make sure that the user isn't moving 0 backwards.
                if old_row - 1 == new_row:

                    # check if the game is unfinished and the space is open.
                    if self._game_state == "UNFINISHED" and\
                            self._board[new_row][new_col] == " ":

                        self._board[old_row][old_col] = " "
                        self._board[new_row][new_col] = "O"
                        self.win_conditions()
                        self.print_board()
                        self.get_game_state()
                        return True

                    else:
                        return False

                else:
                    return False

            else:
                return False

        else:

            return False

    def win_conditions(self):
        """
        Method checking to see if X or O have won the game. If one character
        has won the game_state is changed to reflect their victory.
        """

        # checks for x's win condition, they have reached row 7.
        if self._location_x[0] == 7:
            self._game_state = "X_WON"

        elif self._location_x[0] == 0 and self._location_x[1] == 7:
            if self._board[self._location_x[0] + 1][self._location_x[1] - 1]\
             != " ":
                self._game_state = "O_WON"
                return True

        elif self._location_x[0] == 0:
            # make sure x has a valid move when it is at the top of the board.
            if self._board[self._location_x[0] + 1][self._location_x[1] - 1]\
                 != " ":

                if self._board[self._location_x[0] + 1][self._location_x[1] + 1]\
                     != " ":
                    self._game_state = "O_WON"
                    return True

        elif self._location_x[1] == 0:
            # make sure x has a valid move when it is on the left side.
            if self._board[self._location_x[0] - 1][self._location_x[1] + 1]\
                 != " ":
                if self._board[self._location_x[0] + 1][self._location_x[1] + 1] != " ":
                    self._game_state = "O_WON"
                    return True

        elif self._location_x[1] == 7:
            # make sure x has a valid move when it is on the right side.
            if self._board[self._location_x[0] + 1][self._location_x[1] - 1]\
                != " ":
                if self._board[self._location_x[0] - 1][self._location_x[1] - 1] != " ":
                    self._game_state = "O_WON"
                    return True

        elif self._board[self._location_x[0] - 1][self._location_x[1] - 1]\
            != " ":
            # if X hasn't won then we check O by looking at all the surrounding
            # diagonal moves X could make. If there are none then O has won.

            if self._board[self._location_x[0] - 1][self._location_x[1] + 1]\
                 != " ":

                if self._board[self._location_x[0] + 1][self._location_x[1] - 1] != " ":

                    if self._board[self._location_x[0] + 1][self._location_x[1] + 1] != " ":

                        self._game_state = "O_WON"
                        return True

                    else:
                        
                        return False

                else:

                    return False

            else:

                return False

        else:

            return False

        return self._board


# test case 3 x is trapped by ob and o's
board_1 = FBoard()
board_1.print_board()
board_1.get_game_state()
board_1.move_o(7, 0, 6, 1)  # moving o's in general
board_1.move_o(7, 2, 6, 3)
board_1.move_o(7, 4, 6, 5)
board_1.move_o(7, 6, 6, 7)
board_1.move_x(1, 2)  # x finally busts a move
board_1.move_x(0, 3)  # x can move backwards
board_1.move_x(1, 4)  # x cannot move out of bounds
board_1.move_x(0, 5)
board_1.move_x(1, 6)
board_1.move_x(0, 7)
board_1.move_o(6, 3, 5, 4)
board_1.move_o(5, 4, 4, 5)
board_1.move_o(4, 5, 3, 6)
board_1.move_o(3, 6, 2, 7)
board_1.move_o(2, 7, 1, 6)
