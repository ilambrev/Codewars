function solution(str, ending) {
    return str.slice(str.length - ending.length) === ending;
}

// console.log(solution('abc', 'bc'));
// console.log(solution('abc', 'd'));