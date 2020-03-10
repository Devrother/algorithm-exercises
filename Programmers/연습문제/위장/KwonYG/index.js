const TYPE = 1;

const getSum = pickedClothes =>
  Object.keys(pickedClothes).reduce((sum, key) => sum * pickedClothes[key], 1);

const pickCloth = clothes =>
  clothes.reduce((pickedClothes, cloth) => {
    pickedClothes[cloth[TYPE]] = pickedClothes[cloth[TYPE]]
      ? pickedClothes[cloth[TYPE]] + 1
      : 2;
    return pickedClothes;
  }, {});

const solution = clothes => {
  const pickedClothes = pickCloth(clothes);
  const answer = getSum(pickedClothes) - 1;
  return answer;
};

console.log(
  solution([
    ["yellow_hat", "headgear"],
    ["blue_sunglasses", "eyewear"],
    ["green_turban", "headgear"]
  ])
);
