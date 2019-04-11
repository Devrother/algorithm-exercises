function Counter(list){
    let result = [];
    list.forEach(element => {
        result[element.charCodeAt(0) - 97] = ( result[element.charCodeAt(0) - 97] | 0 ) + 1; 
    });

    return result;
}


function isValid(s) {
    let list = s.split("");
    
    let result = Counter(list).sort().filter(el => el != null);
    console.log(result);

    // 전부 갯수가 같은 경우
    if(result[0] === result[result.length-1])
        return 'YES';
    
    // 한 요소가 나머지요소들 갯수보다 +1 더 큰 경우
    if(result[0] === result[result.length-2] && (result[0] - result[result.length-1] === -1 )) 
        return 'YES';
    
    // 한 요소의 갯수가 1이면서 나머지 요소 갯수가 같은 경우    
    if(result[0] === 1 && (result[1] === result[result.length-1])) 
        return 'YES';
    
    return 'NO';
}

console.log(isValid('abccc'));
