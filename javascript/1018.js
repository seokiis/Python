const fs = require("fs");
const io = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = fs.readFileSync(io).toString().trim().split("\n");

const [size, ...arr] = input;
const [row, col] = size.split(" ").map(Number);

//하얀색이 먼저 시작하는 판
const white = [
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
];

//검은색이 먼저 시작하는 판
const black = [
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
];

function whiteFirst(row, col, arr) {
  let cnt = 0;
  for (let i = 0; i < 8; i++) {
    for (let j = 0; j < 8; j++) {
      if (arr[row + i][col + j] !== white[i][j]) cnt++;
    }
  }
  return cnt;
}

function blackFirst(row, col, arr) {
  let cnt = 0;
  for (let i = 0; i < 8; i++) {
    for (let j = 0; j < 8; j++) {
      if (arr[row + i][col + j] !== black[i][j]) cnt++;
    }
  }
  return cnt;
}

let result1 = Infinity;
let result2 = Infinity;

for (let i = 0; i < row - 7; i++) {
  for (let j = 0; j < col - 7; j++) {
    result1 = Math.min(result1, whiteFirst(i, j, arr));
    result2 = Math.min(result2, blackFirst(i, j, arr));
  }
}

console.log(Math.min(result1, result2));
