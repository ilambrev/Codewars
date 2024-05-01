function solution(str) {

    const letters = [];

    for (let i = str.length - 1; i >= 0; i--) {
        letters.push(str.charAt(i));
    }

    return letters.join('');
}

// console.log(solution('world'));
// console.log(solution('word'));