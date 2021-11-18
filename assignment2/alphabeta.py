

def alphabeta(current_game):
    """
    :param current_game: the first GameClass object of the game
    :return: result of recursive alphabeta
    """
    return recursive_alphabeta(current_game, -1, current_game.max_steps()+2)


def recursive_alphabeta(current_game, alpha, beta):
    """
    The algorithm currently implemented here is minimax and not alphabeta, you need to change it
    :param current_game: Game Class Object
    :param alpha: alpha value
    :param beta: beta value
    :return: v - value , best_prev_move - list of previous game class objects that leads to v
    """
    if current_game.game_over():
        return current_game.get_score(), []
    if current_game.get_cur_player() == 1:  # -- MIN player --
        v = current_game.max_steps() + 1
        moves = current_game.get_moves()
        for move in moves:
            mx, prev_moves = recursive_alphabeta(move, alpha, beta)
            if v > mx:
                v = mx
                best_move = move
                best_prev_move = prev_moves
            if v < beta:
                beta = v
            if beta <= alpha:
                break
    if current_game.get_cur_player() == 2:  ## -- MAX player --
        v = 0
        moves = current_game.get_moves()
        for move in moves:
            mx, prev_moves = recursive_alphabeta(move, alpha, beta)
            if v < mx:
                v = mx
                best_move = move
                best_prev_move = prev_moves
            if v > alpha:
                alpha = v
            if beta <= alpha:
                break
    best_prev_move.append(best_move)
    return v, best_prev_move
