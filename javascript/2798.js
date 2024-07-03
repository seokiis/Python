// 5 21
// 5 6 7 8 9

const fs = require("fs");
const io = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(io).toString().trim().split("\n");

const [N, T] = input[0].split(" ").map(Number);
const numbers = input[1].split(" ").map(Number);

var answer = 0;
for (let i = 0; i < numbers.length - 2; i++) {
  for (let j = i + 1; j < numbers.length - 1; j++) {
    for (let k = j + 1; k < numbers.length; k++) {
      let sum = numbers[i] + numbers[j] + numbers[k];
      if (sum <= T) {
        answer = Math.max(answer, sum);
      }
    }
  }
}

console.log(answer);
