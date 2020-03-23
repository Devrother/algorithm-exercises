function solution(board) {
  if (isAllZeroBoard(board)) return 0;

  const rowLength = board.length;
  const colLength = board[0].length;

  let maximumSide = 1;
  for (let i = 1; i < rowLength; i++) {
    for (let j = 1; j < colLength; j++) {
      if (board[i][j] === 0) {
        board[i][j] = 0;
        continue;
      }

      board[i][j] = getLeastSide(board, i, j) + 1;
      maximumSide = Math.max(maximumSide, board[i][j]);
    }
  }

  return maximumSide * maximumSide;
}

const isAllZeroBoard = board => {
  return board.every(row => row.includes(1) === false);
};

const getLeastSide = (board, row, col) => {
  return Math.min(
    board[row][col - 1],
    board[row - 1][col - 1],
    board[row - 1][col]
  );
};

// solution([
//   [1, 1],
//   [1, 0]
// ]);

// solution([
//   [0, 1, 1, 1],
//   [1, 1, 1, 1],
//   [1, 1, 1, 1],
//   [0, 0, 1, 0]
// ]);

solution([
  [0, 0, 0, 1],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0]
]);
