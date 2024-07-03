// 121
// 1231
// 12421
// 0

const fs = require("fs");
const io = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(io).toString().trim().split("\n");

function isPelinDrome(str) {
  let left = 0;
  let right = str.length - 1;

  while (left < right) {
    if (str[left] !== str[right]) return false;
    left++;
    right--;
  }
  return true;
}

for (let line of input) {
  if (line === "0") break;
  if (isPelinDrome(line)) console.log("yes");
  else console.log("no");
}
