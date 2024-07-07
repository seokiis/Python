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

const [a, ...arr] = input;
const [n, m] = a.split(" ").map(Number);

let graph = Array(n + 1)
  .fill()
  .map(() => []);

for (let ar of arr) {
  let [a, b] = ar.split(" ").map(Number);
  graph[a].push(b);
  graph[b].push(a);
}

let visited = Array(n + 1).fill(false);
let answer = 0;

for (let node = 1; node <= n; node++) {
  if (!visited[node]) {
    answer++;
    let s = new stack();
    s.push(node);
    visited[node] = true;
    while (s.size() > 0) {
      let x = s.pop();
      for (let nextNode of graph[x]) {
        if (!visited[nextNode]) {
          s.push(nextNode);
          visited[nextNode] = true;
        }
      }
    }
  }
}

console.log(answer - 1);
