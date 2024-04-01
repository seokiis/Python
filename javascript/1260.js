const fs = require("fs");

const io = process.platform === "linux" ? "/dev/stdin" : "../input.txt";
let input = fs.readFileSync(io).toString();

const [metadata, ...edges] = input.trim().split("\n");
console.log(edges);

let [n, m, start] = metadata.split(" ").map(Number);

let edge = Array(n + 1)
  .fill()
  .map(() => []);

for (const e of edges) {
  let [from, to] = e.split(" ").map(Number);
  edge[from].push(to);
  edge[to].push(from);
}

let isVisitDFS = Array(n + 1).fill(false);
let isVisitBFS = Array(n + 1).fill(false);

let dfsResult = [];
let bfsResult = [];

function dfs(node) {
  dfsResult.push(node);
  isVisitDFS[node] = true;

  for (const n of edge[node]) {
    if (!isVisitDFS[n]) {
      dfs(n);
    }
  }
}

function bfs(node) {
  let queue = Array();

  queue.push(node);
  isVisitBFS[node] = true;
  bfsResult.push(node);

  while (queue.length > 0) {
    let now = queue.shift();

    for (const n of edge[now]) {
      if (!isVisitBFS[n]) {
        queue.push(n);
        isVisitBFS[n] = true;
        bfsResult.push(n);
      }
    }
  }
}

dfs(start);
bfs(start);

console.log(dfsResult.join(" "));
console.log(bfsResult.join(" "));
