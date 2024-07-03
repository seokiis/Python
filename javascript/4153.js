// 6 8 10
// 25 52 60
// 5 12 13
// 0 0 0

const fs = require("fs");
const io = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const inputs = fs.readFileSync(io).toString().trim().split("\n");

for (let line of inputs) {
  const [a, b, c] = line.split(" ").map(Number);

  if (a === 0 && b === 0 && c === 0) break;
  const max = Math.max(a, b, c);
  if (max === a) {
    if (a ** 2 === b ** 2 + c ** 2) console.log("right");
    else console.log("wrong");
  } else if (max === b) {
    if (b ** 2 === a ** 2 + c ** 2) console.log("right");
    else console.log("wrong");
  } else {
    if (c ** 2 === a ** 2 + b ** 2) console.log("right");
    else console.log("wrong");
  }
}
