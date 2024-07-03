// 23
// 3 1 4 1 5 9
// 5 7

// 첫 줄에 티셔츠를 T장씩 몇 묶음 주문할 것인지 출력
// P 자루씩 최대 몇 묶음 주문할 수 있는지와, 그 때 펜을 한 자루씩 몇 개 주문하는지 구하세요.

const fs = require("fs");
const io = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = fs.readFileSync(io).toString().trim().split("\n");

const n = parseInt(input[0]);
const arr = input[1].split(" ").map(Number);
const [T, P] = input[2].split(" ").map(Number);

let firstAnswer = 0;
for (let i = 0; i < arr.length; i++) {
  firstAnswer += Math.ceil(arr[i] / T);
}

console.log(firstAnswer);
console.log(Math.floor(n / P), n % P);
