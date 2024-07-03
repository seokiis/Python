const fs = require("fs");
const io = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(io).toString().trim().split("\n");

class Stack {
  constructor() {
    this.stack = [];
  }
  push(element) {
    this.stack.push(element);
  }
  pop() {
    if (this.isEmpty()) return -1;
    return this.stack.pop();
  }
  size() {
    return this.stack.length;
  }
  isEmpty() {
    return Number(this.stack.length === 0);
  }
  top() {
    if (this.isEmpty()) return -1;
    return this.stack.at(-1);
  }
}

let [, ...lines] = input;

let stack = new Stack();
let result = "";

for (let line of lines) {
  let [command, num] = line.split(" ");
  switch (command) {
    case "push":
      num = parseInt(num);
      stack.push(num);
      break;
    case "pop":
      result += stack.pop() + "\n";
      break;
    case "size":
      result += stack.size() + "\n";
      break;
    case "empty":
      result += stack.isEmpty() + "\n";
      break;
    case "top":
      result += stack.top() + "\n";
      break;
  }
}

console.log(result);
result = null;
