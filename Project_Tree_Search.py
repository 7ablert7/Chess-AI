import chess

board = chess.Board()


piece_values = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 0,
}

def evaluate(board):
    score = 0

    for square, piece in board.piece_map().items():
        value = piece_values[piece.piece_type]

        if piece.color == chess.WHITE:
            score += value
        else:
            score -= value

    return score

def minimax (board, depth, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate(board)

    if maximizing_player:
        best_score = -999999
        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, depth - 1, False)
            board.pop()

            if score > best_score:
                best_score = score


        return best_score
    else:
        best_score = 999999
        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, depth - 1, True)
            board.pop()

            if score < best_score:
                best_score = score


        return best_score

def choose_best_move(board, depth):
    best_move = None
    best_score = -999999

    for move in board.legal_moves:
        board.push(move)
        score = minimax(board, depth-1, False)
        board.pop()

        if score > best_score:
            best_score = score
            best_move = move

    return best_move

while board.is_game_over() == False:
    print(board)
    board.push_uci(input("Enter your move in UCI notation"))
    print("")
    print(board)
    print("")
    board.push(choose_best_move(board, 3))