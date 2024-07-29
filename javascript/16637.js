const fs = require("fs");
const io = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(io).toString().trim().split("\n");

// 9
// 3+8*7-9*2

const n = parseInt(input.shift());

function calc(operator, x, y) {
  switch (operator) {
    case "+":
      return x + y;
    case "-":
      return x - y;
    case "*":
      return x * y;
  }
}

let answer = -Infinity;
let nums = [];
let operators = [];

input[0].split("").forEach((el, idx) => {
  if (idx % 2 === 0) nums.push(parseInt(el));
  else operators.push(el);
});

// 3+8*7-9*2`
// nums = [3, 8, 7, 9, 2]
// operators = ['+', '*', '-','*']
function check(idx, number) {
  console.log(idx);
  if (idx === nums.length - 1) {
    answer = Math.max(answer, number);
    return;
  }
  // check(1, calc(3, '+', 8))
  // check(2, calc(11, '*', 7))
  // check(3, calc(77, '-', 9))
  // check(4, calc(68, '*', 2))
  check(idx + 1, calc(operators[idx], number, nums[idx + 1]));

  if (idx + 1 < nums.length - 1) {
    // check(4, calc(3, '+', calc(8, '*', 7))
    check(
      idx + 2,
      calc(
        operators[idx],
        number,
        calc(operators[idx + 1], nums[idx + 1], nums[idx + 2])
      )
    );
  }
}

check(0, nums[0]);

console.log(answer);
