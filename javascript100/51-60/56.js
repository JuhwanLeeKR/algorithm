/*
# 문제56 : 객체의 함수 응용

다음의 객체가 주어졌을 때 한국의 면적과 가장 비슷한 국가와 그 차이를 출력하세요.

데이터
nationWidth = {
     'korea': 220877,
     'Rusia': 17098242,
     'China': 9596961,
     'France': 543965,
     'Japan': 377915,
     'England' : 242900,
}

출력
England 22023
*/

nationWidth = {
  korea: 220877,
  Rusia: 17098242,
  China: 9596961,
  France: 543965,
  Japan: 377915,
  England: 242900,
};
const koreaWidth = nationWidth.korea;
const widthList = [];

const objName = Object.keys(nationWidth);
const objValue = Object.values(nationWidth);

for (let i = 0; i < objName.length; i++) {
  widthList.push(Math.abs(objValue[i] - koreaWidth));
}
widthList.sort((a, b) => a - b);
const minWidthGap = widthList[1];

let resultValue = '';
objName.find((key) => nationWidth[key] === koreaWidth + minWidthGap)
  ? (resultValue += objName.find(
      (key) => nationWidth[key] === koreaWidth + minWidthGap
    ))
  : (resultValue += objName.find(
      (key) => nationWidth[key] === koreaWidth - minWidthGap
    ));
console.log(resultValue, minWidthGap);

/*
const nationWidth = {
	'korea': 220877,
	'Rusia': 17098242,
	'China': 9596961,
	'France': 543965,
	'Japan': 377915,
	'England' : 242900,
};

const w = nationWidth['korea'];

delete nationWidth['korea'];

const entry = Object.entries(nationWidth);
const values = Object.values(nationWidth);

//gap에 최댓값 저장
let gap = Math.max.apply(null, values);
let item = [];

for (let i in entry){
  if (gap > Math.abs(entry[i][1] - w)){
    gap = Math.abs(entry[i][1] - w);
    item = entry[i];
  }
}

console.log(item[0], item[1] - w);
*/
