// 3 4
// ohhenrie
// charlie
// baesangwook
// obama
// baesangwook
// ohhenrie
// clinton

const fs = require("fs");
const io = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(io).toString().trim().split("\n");

const [N, M] = input.shift().split(" ").map(Number);

/**
 * Set
 * 중복되지 않는 값들의 집합입니다.
 * 각 값은 한 번만 등장할 수 있습니다.
 * 키-값 쌍이 아닌 값만 저장합니다.
 * 주요 메서드: add(), has(), delete(), clear()
 */

console.log(c);
const a = new Set(input.slice(0, N));
const b = new Set(input.slice(N));

const result = [];
for (let name of b) {
  if (a.has(name)) result.push(name);
}

console.log(result.length);
console.log(result.sort().join("\n"));
