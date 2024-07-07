const fs = require("fs");
const io = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(io).toString().trim().split("\n");

class stack {
  constructor() {
    this.stack = [];
    this.begin = 0;
    this.end = 0;
  }
  push(element) {
    this.stack[this.end++] = element;
  }
  pop() {
    return this.stack[this.begin++];
  }
  size() {
    return this.end - this.begin;
  }
}

let [n, m, ...arr] = input;
n = parseInt(n);
m = parseInt(m);

let graph = Array(n + 1)
  .fill()
  .map(() => Array().fill());

for (let ar of arr) {
  let [a, b] = ar.split(" ").map(Number);
  graph[a].push(b);
  graph[b].push(a);
}

let visited = Array(n + 1).fill(false);

let s = new stack();
s.push(1);
visited[1] = true;

while (s.size() > 0) {
  let x = s.pop();
  for (node of graph[x]) {
    if (!visited[node]) {
      s.push(node);
      visited[node] = true;
    }
  }
}

let answer = visited.filter((v) => v).length - 1;

console.log(answer);
