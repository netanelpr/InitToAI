import numpy as np
import math


class Game:
    def __init__(self, grid, start_location, score=0):
        """
        :param grid: matrix that represents the grid during this turn
        :param start_location: player 1 location in this turn
        :param score: the number of moves up to this turn
        """
        self.__grid = grid
        self.__p1_location = start_location
        if self.__grid[start_location[0]][start_location[1]] != 'W':
            self.__grid[start_location[0]][start_location[1]] = 'X'
        self.__score = score
        if score%3 > 1:
            self.__cur_player = 2
        else:
            self.__cur_player = 1

    def potential_moves(self):
        """
        :param grid: NxN two-dimensions numpy array
        :param location: (x,y) location of player, tuple
        :param player: int, 1 or 2
        :param goals: list of all locations of goals
        :return: list of all the moves
        """
        x, y = self.__p1_location
        grid = self.__grid
        moves = []
        # Check right
        if x + 1 < len(grid):
            if grid[x + 1][y] != '@' and grid[x+1][y] != 'X':
                moves.append((x + 1, y))
        # Check left
        if x - 1 > 0:
            if grid[x - 1][y] != '@' and grid[x-1][y] != 'X':
                moves.append((x - 1, y))
        # Check up
        if y - 1 > 0:
            if grid[x][y - 1] != '@' and grid[x][y - 1] != 'X':
                moves.append((x, y - 1))
        # Check down
        if y + 1 < len(grid):
            if grid[x][y + 1] != '@' and grid[x][y + 1] != 'X':
                moves.append((x, y + 1))
        # If the current player is the ooc-car
        if self.__cur_player == 1:
            return moves
        # If the current player is the police
        p2_moves = []
        for move in moves:
            if grid[move[0]][move[1]] != 'W':
                p2_moves.append(move)
        return p2_moves

    def get_moves(self):
        """
        :return: All possible GameClass objects after performing a valid move during this turn
        """
        moves = self.potential_moves()
        new_games = []
        for move in moves:
            if self.__cur_player == 2:
                new_grid = list(map(list, self.__grid))
                new_grid[move[0]][move[1]] = '@'
                new_games.append(Game(new_grid, self.__p1_location, self.__score+1))
            else:
                new_grid = list(map(list, self.__grid))
                new_games.append(Game(new_grid, move, self.__score+1))
        return new_games

    def game_over(self):
        """
        :return: whether the game is over or not
        """
        if len(self.potential_moves()) == 0:
            return True
        x, y = self.__p1_location
        if self.__grid[x][y] == 'W':
            return True
        else:
            return False

    def get_score(self):
        """
        :return: the current score of the game
        """
        x, y = self.__p1_location
        if self.__grid[x][y] == 'W':
            return self.__score
        if len(self.potential_moves()) == 0:
            return self.max_steps()
        return self.__score

    def get_cur_player(self):
        """
        :return: the current player number - 1 = ooc car , 2 = police
        """
        return self.__cur_player

    def __str__(self):
        return str(self.__grid)

    def __repr__(self):
        return self.__grid

    def get_grid(self):
        """
        :return: current game grid matrix
        """
        return self.__grid

    def max_steps(self):
        """
        :return: value of max possible steps
        """
        return len(self.__grid)*len(self.__grid)*3

