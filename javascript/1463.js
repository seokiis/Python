const fs = require("fs");
const io = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(io).toString();

const num = Number(input);

const DP = Array(num + 1).fill(0);

DP[1] = 0;
DP[2] = 1;

for (let i = 3; i <= num; i++) {
  DP[i] = DP[i - 1] + 1;
  if (i % 2 === 0) DP[i] = Math.min(DP[i], DP[i / 2] + 1);
  if (i % 3 === 0) DP[i] = Math.min(DP[i], DP[i / 3] + 1);
}

console.log(DP[num]);
