const fs = require("fs");
const io = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(io).toString().trim().split("\n");

const [N, M] = input.shift().split(" ").map(Number);

/**
 * 시간 초과 코드
 */
// for (let i = 0; i < N; i++) {
//   let pocketmon = input[i + 1];
//   arr.push(pocketmon);
// }
// for (let i = N; i < N + M; i++) {
//   let question = input[i + 1];
//   if (isNaN(question)) {
//     console.log(arr.indexOf(question) + 1);
//   } else {
//     //문자열을 숫자와 함께 사용할 때 자동으로 숫자로 변환을 시도합니다.
//     //배열의 index로 문자열이 들어가면, 문자열이 숫자로 변환되어서 index로 사용됩니다.
//     console.log(arr[question - 1]);
//   }
// }

/**
 * Map을 사용한 코드
 * 해쉬(Hash)란 키(key)와 값(val) 짝을 이루는 dict 형태의 자료구조이다.
 * Hash 함수를 통해 빠른 탐색이 가능하다. 시간복잡도 O(1).
 *
 * Javascript에서는 기본적으로 해쉬테이블을 만들 수 있도록 ES6부터 Map을 지원해주고 있는데,
 * 이를 사용하면 여러가지 메서드를 사용해서 해쉬테이블을 조작할 수 있다.
 *
 * set(key, val)
 * key,val 순으로 저장한다. key에는 Number, String, function, object, NaN의 자료형이 들어갈 수 있다.
 *
 * get(key)
 * val 값을 얻을 수 있다.
 *
 * has(key)
 * val 값을 찾을 수 있다.
 *
 * delete()
 * key나 val 값을 삭제할 수 있다.
 *
 * size(key)
 * val 값의 존재 유뮤를 확인 할 수 있다.
 */

const NumToName = new Map(); // 포켓몬 번호 => 포켓몬 이름
const NameToNum = new Map(); // 포켓몬 이름 => 포켓몬 번호

for (let i = 0; i < N; i++) {
  // N까지
  NumToName.set(i + 1, input[i]); // 1 => 'Bulbasqur' , 2 => 'Ivysaur', ... 26 => 'Raichu'
  NameToNum.set(input[i], i + 1); // 'Bulbasaur' => 1, 'Ivysaur' => 2, ... 'Raichu' => 26
}
const quiz = input.slice(N, input.length); // input에서 quiz 뽑아내고

let answer = "";
quiz.forEach((v) => {
  if (isNaN(v)) {
    // 문자인 경우
    answer += NameToNum.get(v) + "\n";
  } else {
    // 숫자인 경우
    answer += NumToName.get(+v) + "\n";
  }
});
console.log(answer.trim());
