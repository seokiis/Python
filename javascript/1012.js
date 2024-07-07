const fs = require("fs");
const io = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(io).toString().trim().split("\n");

// 2
// 10 8 17
// 0 0
// 1 0
// 1 1
// 4 2
// 4 3
// 4 5
// 2 4
// 3 4
// 7 4
// 8 4
// 9 4
// 7 5
// 8 5
// 9 5
// 7 6
// 8 6
// 9 6
// 10 10 1
// 5 5

class Queue {
  constructor() {
    this.queue = [];
    this.end = 0;
    this.begin = 0;
  }
  push(element) {
    this.queue[this.end++] = element;
  }
  pop() {
    return this.queue[this.begin++];
  }
  size() {
    return this.end - this.begin;
  }
}

function bfs(x, y, visited, graph, xSize, ySize) {
  let queue = new Queue();
  let dx = [0, 0, 1, -1];
  let dy = [1, -1, 0, 0];

  queue.push([x, y]);
  visited[x][y] = true;

  while (queue.size() > 0) {
    let [x, y] = queue.pop();

    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];

      if (
        nx >= 0 &&
        nx < xSize &&
        ny >= 0 &&
        ny < ySize &&
        !visited[nx][ny] &&
        graph[nx][ny] === 1
      ) {
        queue.push([nx, ny]);
        graph[nx][ny] = 0;
        visited[nx][ny] = true;
      }
    }
  }
}

const t = parseInt(input[0]);
let idx = 1;
for (let i = 0; i < t; i++) {
  let [ySize, xSize, k] = input[idx++].split(" ").map(Number);
  let graph = Array(xSize)
    .fill()
    .map(() => Array(ySize).fill(0));
  let visited = Array(xSize)
    .fill()
    .map(() => Array(ySize).fill(false));

  for (let j = 0; j < k; j++) {
    let [a, b] = input[idx++].split(" ").map(Number);
    graph[b][a] = 1;
  }

  let result = 0;
  for (let i = 0; i < xSize; i++) {
    for (let j = 0; j < ySize; j++) {
      if (graph[i][j] === 1) {
        bfs(i, j, visited, graph, xSize, ySize);

        result++;
      }
    }
  }
  console.log(result);
}
