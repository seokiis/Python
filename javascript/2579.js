// 6
// 10
// 20
// 15
// 25
// 10
// 20

const fs = require("fs");
const io = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(io).toString().trim().split("\n");

const N = parseInt(input.shift());
let numbers = input.map(Number);

dp = Array(N).fill(0);
dp[0] = numbers[0];
dp[1] = numbers[0] + numbers[1];

for (let i = 2; i < N; i++) {
  dp[i] = Math.max(
    numbers[i] + dp[i - 2],
    numbers[i] + numbers[i - 1] + dp.at(i - 3)
  );
}

console.log(dp[N - 1]);

// const fs = require("fs");
// const io = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
// const input = fs.readFileSync(io).toString().trim().split("\n");

// const N = parseInt(input.shift());
// let numbers = input.map(Number);

// dp = Array(N).fill(0);
// dp[0] = numbers[0];
// dp[1] = Math.max(numbers[0] + numbers[1], numbers[1]);
// dp[2] = Math.max(numbers[0] + numbers[2], numbers[1] + numbers[2]);

// for (let i = 3; i < N; i++) {
//   dp[i] = Math.max(
//     numbers[i] + dp[i - 2],
//     numbers[i] + numbers[i - 1] + dp[i - 3]
//   );
// }

// console.log(dp[N - 1]);
