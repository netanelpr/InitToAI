

def minimax(current_game):
    """
    :param current_game: Game Class Object
    :return: v - value , best_prev_move - list of previous game class objects that leads to v
    """
    if current_game.game_over():
        return current_game.get_score(), []
    if current_game.get_cur_player() == 1:  # -- MIN player --
        v = current_game.max_steps() + 1
        moves = current_game.get_moves()
        for move in moves:
            mx, prev_moves = minimax(move)
            if v > mx:
                v = mx
                best_move = move
                best_prev_move = prev_moves
    if current_game.get_cur_player() == 2:  ## -- MAX player --
        v = 0
        moves = current_game.get_moves()
        for move in moves:
            mx, prev_moves = minimax(move)
            if v < mx:
                v = mx
                best_move = move
                best_prev_move = prev_moves
    best_prev_move.append(best_move)
    return v, best_prev_move
