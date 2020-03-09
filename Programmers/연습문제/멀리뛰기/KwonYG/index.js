/*
(1칸, 1칸, 1칸, 1칸)
(1칸, 2칸, 1칸)
(1칸, 1칸, 2칸)
(2칸, 1칸, 1칸)
(2칸, 2칸)

1칸: [1]
2칸: [1,1], [2]
3칸: [1,1,1], [1,2], [2,1]
4칸: [1,1,1,1], [1,2,1], [1,1,2], [2,1,1], [2,2]5
5칸: [1,1,1,1,1], [1,2,1,1], [1,1,2,1], [2,1,1,1], [2,2,1],[1,2,2,],[2,1,2] 8


 */

function solution(n) {
  if (n === 1 || n === 2 || n === 3) return n;

  let jumpCaseA = 2;
  let jumpCaseB = 3;
  for (let i = 3; i < n; i++) {
    const nextCase = (jumpCaseA + jumpCaseB) % 1234567;
    jumpCaseA = jumpCaseB;
    jumpCaseB = nextCase;
  }

  return jumpCaseB;
}
solution(5);
