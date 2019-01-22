function anagramCounter (wordsArray) {
  cache = new Map()
  for (const s of wordsArray.map(sortString)) {
    (cache.has(s)) ? cache.set(s, cache.get(s) + 1) : cache.set(s, 0)
  }
  
  let counter = 0
  cache.forEach((cnt) => counter += (cnt * (cnt+1)) / 2)
  return counter;
}

function sortString(word) {
  return word.split('').sort().join('')
}
