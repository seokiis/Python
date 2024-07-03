const fs = require("fs");
const io = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(io).toString().trim().split("\n");

const arr = input[1].split(" ").map(Number);
const arr2 = input[3].split(" ").map(Number);
let answer = [];

arr.sort((a, b) => a - b);
// 이분탐색
arr2.forEach((v) => {
  let start = 0;
  let end = arr.length - 1;
  let res = false;

  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    if (arr[mid] > v) {
      end = mid - 1;
    } else if (arr[mid] < v) {
      start = mid + 1;
    } else {
      res = true;
      break;
    }
  }

  if (res) {
    answer.push(1);
  } else {
    answer.push(0);
  }
});

console.log(answer.join("\n"));
