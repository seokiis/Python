// 3
// 40 80 60

const fs = require("fs");
const io = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

const input = fs.readFileSync(io).toString().trim().split("\n");
const n = parseInt(input[0]);
const arr = input[1].split(" ").map(Number);

const M = Math.max(...arr);
const newArr = arr.map((v) => (v / M) * 100);
const avg = newArr.reduce((acc, cur) => acc + cur) / n;
console.log(avg);
