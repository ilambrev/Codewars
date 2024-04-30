function solution(str) {
    str.length % 2 !== 0 ? str += '_' : str;
    const result = [];

    for (let i = 1; i < str.length; i += 2) {
        result.push(str.slice(i - 1, i + 1));
    }

    return result;
}

// console.log(solution('abc'));
// console.log(solution('abcdef'));