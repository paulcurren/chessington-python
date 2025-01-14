"""
Definitions of each of the different chess pieces.
"""
from __future__ import annotations
from typing import Set, List, TYPE_CHECKING

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square

if TYPE_CHECKING:
    from chessington.engine.board import Board


class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """
    def get_available_moves(self, board : Board) -> List[Square]:

        square = board.find_piece(self)

        if self.player == Player.WHITE:
            increment = 1
            first_row = 1
            last_row = board.get_size() - 1
            enemy = Player.BLACK
        else:
            increment = -1
            first_row = board.get_size() - 2
            last_row = 0
            enemy = Player.WHITE

        # on the edge? No more moves
        if square.row == last_row:
            return []

        # is pawn at starting position?
        if square.row == first_row:
            is_first_move = True
        else:
            is_first_move = False


        squares = []
        if is_first_move:
            new_square1 = Square.at(square.row + increment, square.col)
            new_square2 = Square.at(square.row + increment + increment, square.col)

            if board.get_piece(new_square1) == None:
                squares.append(new_square1)
                if board.get_piece(new_square2) == None:
                    squares.append(new_square2)

        else:
            new_square = Square.at(square.row + increment, square.col)
            if board.get_piece(new_square) == None:
                squares.append(new_square)

        # look for the enemy to capture
        enemy1_square = Square.at(square.row + increment, square.col - increment)
        enemy2_square = Square.at(square.row + increment, square.col + increment)

        piece1 = board.get_piece(enemy1_square)
        piece2 = board.get_piece(enemy2_square)

        if piece1 != None and piece1.player == enemy:
            squares.append(enemy1_square)

        if piece2 != None and piece2.player == enemy:
            squares.append(enemy2_square)


        return squares


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []