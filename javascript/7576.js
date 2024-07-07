const fs = require("fs");
const io = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(io).toString().trim().split("\n");

class Queue {
  constructor() {
    this.q = [];
    this.begin = 0;
    this.end = 0;
  }
  pop() {
    return this.q[this.begin++];
  }
  size() {
    return this.end - this.begin;
  }
  push(el) {
    this.q[this.end++] = el;
  }
}

// 6 4
// 0 0 0 0 0 0
// 0 0 0 0 0 0
// 0 0 0 0 0 0
// 0 0 0 0 0 1

function bfs(array, startPositionArray, xSize, ySize) {
  const dx = [0, 0, -1, 1];
  const dy = [1, -1, 0, 0];
  const q = new Queue();

  for (let node of startPositionArray) {
    q.push(node);
  }

  while (q.size() > 0) {
    let [a, b] = q.pop();
    visited[a][b] = true;
    let prev = array[a][b];

    for (i = 0; i < 4; i++) {
      let nA = a + dx[i];
      let nB = b + dy[i];
      if (
        nA >= 0 &&
        nA < xSize &&
        nB >= 0 &&
        nB < ySize &&
        !visited[nA][nB] &&
        array[nA][nB] === 0
      ) {
        array[nA][nB] = prev + 1;
        visited[nA][nB] = true;
        q.push([nA, nB]);
      }
    }
  }
}

const [meta, ...arr] = input;
const [ySize, xSize] = meta.split(" ").map(Number);

let graph = [];
arr.forEach((line) => {
  graph.push(line.split(" ").map(Number));
});

let visited = Array(xSize)
  .fill()
  .map(() => Array(ySize).fill(0));

console.log(visited);

let tomatoPosition = [];

for (let i = 0; i < xSize; i++) {
  for (let j = 0; j < ySize; j++) {
    if (graph[i][j] === 1) {
      tomatoPosition.push([i, j]);
    }
  }
}

bfs(graph, tomatoPosition, xSize, ySize);

let mostBig = 0;
for (let i = 0; i < xSize; i++) {
  for (let j = 0; j < ySize; j++) {
    if (graph[i][j] > mostBig) {
      mostBig = graph[i][j];
    }
    if (graph[i][j] === 0) {
      console.log(-1);
      return;
    }
  }
}
console.log(mostBig - 1);
