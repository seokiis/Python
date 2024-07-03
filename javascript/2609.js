// 3
// 40 80 60

const fs = require("fs");
const io = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = fs.readFileSync(io).toString().trim().split("\n");
const [m, n] = input[0].split(" ").map(Number);

const small = Math.min(m, n);
const big = Math.max(m, n);
let gcd = 1;
let lcm = 1;

for (let i = 1; i <= small; i++) {
  if (m % i === 0 && n % i === 0) {
    if (i > gcd) gcd = i;
  }
}

for (let i = big; i <= m * n; i += gcd) {
  if (i % m === 0 && i % n === 0) {
    lcm = i;
    break;
  }
}

console.log(gcd);
console.log(lcm);
