function anagramCounter(wordsArray) {
    let counter = 0;

    for (let i = 0; i < wordsArray.length - 1; i++) {
        for (let j = i + 1; j < wordsArray.length; j++) {
            if (sortString(wordsArray[i]) === sortString(wordsArray[j])) {
                counter++;
            }
        }
    }
    return counter;
}

function sortString(word) {
    const array = word.split("");
    let result = "";
    array.sort();
    array.forEach(element => {
        result += element;
    });

    return result;
}