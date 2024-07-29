1. 배열 정의
2. sort => arr.sort((a, b) => a - b);
3. file 입출력
4. stack, queue
5. dfs, bfs
6. parseInt
7. shift
8. Math.max
9. charAt
10. 2차원 배열이나 (10,1),(10,4),(9,9) 이런거에서 람다써서 배열 정렬

```javascript
let array = [
  [0, 1],
  [0, 2],
  [2, 5],
];

array.sort((a, b) => {
  // 첫 번째 숫자가 같으면 두 번째 숫자를 비교하여 정렬
  if (a[0] === b[0]) {
    return a[1] - b[1]; // 두 번째 숫자를 오름차순으로 정렬
  } else {
    return a[0] - b[0]; // 첫 번째 숫자를 오름차순으로 정렬
  }
});

console.log(array); // [[0, 1], [0, 2], [2, 5]]
```

11. 배열에서 중복 없애는 방법

```javascript
let array = [1, 2, 3, 3, 4, 5, 5];

let uniqueArray = [...new Set(array)];
```
