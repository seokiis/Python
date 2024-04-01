const fs = require("fs");
const io = process.platform === "linux" ? "/dev/stdin" : "../input.txt";

let [metadata, ...relations] = fs
  .readFileSync(io)
  .toString()
  .trim()
  .split("\n");

let [nodeSize, edgeSize] = metadata.split(" ").map(Number);
let graph = Array(nodeSize + 1)
  .fill()
  .map(() => []);

for (const relation of relations) {
  let [from, to] = relation.split(" ").map(Number);
  graph[from].push(to);
  graph[to].push(from);
}

class Queue {
  constructor() {
    this.queue = [];
    this.begin = 0;
    this.end = 0;
  }

  push(value) {
    this.queue.push(value);
    this.end++;
  }
  pop() {
    return this.queue[this.begin++];
  }

  size() {
    return this.end - this.begin;
  }
}

function KevinBacon(node) {
  let isVisit = Array(nodeSize + 1).fill(false);
  let queue = new Queue();

  queue.push(node);
  isVisit[node] = true;

  while (queue.size() > 0) {
    let now = queue.pop();

    for (const next of graph[now]) {
      if (!isVisit[next]) {
        queue.push(next);
        isVisit[next] = isVisit[now] + 1;
      }
    }
  }

  let sum = 0;
  for (let i = 1; i <= nodeSize; i++) {
    sum += isVisit[i];
  }

  return sum;
}

let arr = [];
for (let node = 1; node <= nodeSize; node++) {
  arr.push({ node, sum: KevinBacon(node) });
}
arr.sort((a, b) => a.sum - b.sum);
console.log(arr[0].node);
