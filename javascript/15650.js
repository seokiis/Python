const fs = require("fs");
const io = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(io).toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);
const visited = new Array(N);
const output = [];
let result = "";

function dfs(idx, cnt) {
  if (cnt === M) {
    result += `${output.join(" ")}\n`;
    return;
  }

  for (let i = idx; i < N; i++) {
    if (visited[i] === true) continue;
    visited[i] = true;
    output.push(i + 1);
    dfs(i, cnt + 1);
    output.pop();
    visited[i] = false;
  }
}

dfs(0, 0);
console.log(result);
