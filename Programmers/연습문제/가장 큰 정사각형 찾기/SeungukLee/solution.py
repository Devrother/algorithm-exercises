def solution(board):
    row_len, col_len = len(board), len(board[0])
    
    if is_all_zero_in_board(board):
        return 0
    
    max_v = 1
    for i in range(1, row_len):
        for j in range(1, col_len):
            if board[i][j] == 0:
                continue
            board[i][j] = get_around_min(board, (i, j)) + 1
            max_v = max(max_v, board[i][j])

    return max_v ** 2


def is_all_zero_in_board(board):
    return not any(1 in row for row in board);


def get_around_min(board, location):
    i, j = location
    left, up, left_up = board[i][j-1], board[i-1][j], board[i-1][j-1]
    return min(left, up, left_up);

