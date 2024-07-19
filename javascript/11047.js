// 10 4200
// 1
// 5
// 10
// 50
// 100
// 500
// 1000
// 5000
// 10000
// 50000

const fs = require("fs");

const io = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(io).toString().trim().split("\n");

let [N, K] = input.shift().split(" ").map(Number);
let count = 0;
for (let i = input.length - 1; i >= 0; i--) {
  let money = parseInt(input[i]);
  if (money > K) {
    continue;
  } else {
    count += parseInt(K / money);
    K %= money;
  }
}

console.log(count);
