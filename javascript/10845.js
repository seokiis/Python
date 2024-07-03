const fs = require("fs");
const io = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(io).toString().trim().split("\n");

class Queue {
  constructor() {
    this.queue = [];
    this.begin = 0;
    this.end = 0;
  }
  push(element) {
    this.queue[this.end++] = element;
  }
  size() {
    return this.end - this.begin;
  }
  empty() {
    return Number(this.size() === 0);
  }
  front() {
    if (this.empty()) return -1;
    return this.queue[this.begin];
  }
  back() {
    if (this.empty()) return -1;
    return this.queue[this.end - 1];
  }
  pop() {
    if (this.empty()) return -1;
    return this.queue[this.begin++];
  }
}

const [, ...lines] = input;
let answer = "";
let queue = new Queue();

for (let line of lines) {
  let [command, num] = line.split(" ");
  switch (command) {
    case "push":
      num = parseInt(num);
      queue.push(num);
      break;
    case "pop":
      answer += queue.pop() + "\n";
      break;
    case "size":
      answer += queue.size() + "\n";
      break;
    case "empty":
      answer += queue.empty() + "\n";
      break;
    case "front":
      answer += queue.front() + "\n";
      break;
    case "back":
      answer += queue.back() + "\n";
      break;
  }
}

console.log(answer);
queue = null;
