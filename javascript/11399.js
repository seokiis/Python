// 5
// 3 1 4 3 2

const fs = require("fs");
const io = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(io).toString().trim().split("\n");

const N = parseInt(input.shift());
let numbers = input[0].split(" ").map(Number);
numbers.sort((a, b) => a - b);

let answer = 0;

for (let i = 0; i < N; i++) {
  let tempSum = 0;
  for (let j = 0; j <= i; j++) {
    tempSum += numbers[j];
  }
  answer += tempSum;
}
console.log(answer);
