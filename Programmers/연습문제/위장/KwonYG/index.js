const TYPE = 1;

const solution = clothes => {
  const pickedClothes = pickCloth(clothes);
  const answer = getMul(pickedClothes) - 1;
  return answer;
};

const pickCloth = clothes =>
  clothes.reduce((pickedClothes, cloth) => {
    pickedClothes[cloth[TYPE]] = pickedClothes[cloth[TYPE]]
      ? pickedClothes[cloth[TYPE]] + 1
      : 2;
    return pickedClothes;
  }, {});

const getMul = pickedClothes =>
  Object.keys(pickedClothes).reduce((mul, key) => mul * pickedClothes[key], 1);
