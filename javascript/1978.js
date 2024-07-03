// 4
// 1 3 5 7

const fs = require("fs");
const io = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = fs.readFileSync(io).toString().trim().split("\n");

const n = parseInt(input[0]);
const arr = input[1].split(" ").map(Number);

function isPrime(num) {
  if (num < 2) return false;
  if (num === 2) return true;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
}

// 소수 개수 구하기
let primeCnt = 0;
for (let i = 0; i < arr.length; i++) {
  if (isPrime(arr[i])) primeCnt++;
}

console.log(primeCnt);
