const topKFrequent = (nums, k) => {
  const count = {};

  nums.forEach((num) => {
    count[num] ? (count[num].count += 1) : (count[num] = { num, count: 1 });
  });

  const result = Object.keys(count)
    .sort((a, b) => count[b].count - count[a].count)
    .slice(0, k);

  return result;
};

// topKFrequent([-1, -1], 1);
// topKFrequent([1, 1, 1, 2, 2, 3, 3, 3, 3, 3], 2);
