const TYPE = 1;

const pickCloth = (targetCloth, pickedClothes) => {
  pickedClothes.has(targetCloth)
    ? pickedClothes.set(targetCloth, pickedClothes.get(targetCloth) + 1)
    : pickedClothes.set(targetCloth, 2);
};

const getCombinedCount = pickedClothes => {
  let result = 1;
  for (const count of pickedClothes.values()) {
    result *= count;
  }
  return result - 1;
};

const solution = clothes => {
  const pickedClothes = new Map();

  clothes.forEach(cloth => pickCloth(cloth[TYPE], pickedClothes));

  const answer = getCombinedCount(pickedClothes);
  return answer;
};
