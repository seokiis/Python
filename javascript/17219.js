// 16 4
// noj.am IU
// acmicpc.net UAENA
// startlink.io THEKINGOD
// google.com ZEZE
// nate.com VOICEMAIL
// naver.com REDQUEEN
// daum.net MODERNTIMES
// utube.com BLACKOUT
// zum.com LASTFANTASY
// dreamwiz.com RAINDROP
// hanyang.ac.kr SOMEDAY
// dhlottery.co.kr BOO
// duksoo.hs.kr HAVANA
// hanyang-u.ms.kr OBLIVIATE
// yd.es.kr LOVEATTACK
// mcc.hanyang.ac.kr ADREAMER
// startlink.io
// acmicpc.net
// noj.am
// mcc.hanyang.ac.kr

const fs = require("fs");
const io = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(io).toString().trim().split("\n");

const [N, M] = input.shift().split(" ").map(Number);
const dir = new Map();
for (let i = 0; i < N; i++) {
  const [site, password] = input[i].split(" ");
  dir.set(site, password);
}

for (let i = 0; i < M; i++) {
  console.log(dir.get(input[N + i]));
}
