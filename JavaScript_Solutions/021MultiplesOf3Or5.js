function solution(number) {
    const firstNum = 3;
    const secondNum = 5;

    const multiples = [];

    for (let i = 3; i < number; i++) {
        if (i % 5 === 0) {
            multiples.push(i);
            continue;
        }

        if (i % 3 === 0) {
            multiples.push(i);
        }
    }

    return number < 0 ? 0 : multiples.reduce((acc, curr) => acc + curr, 0);
}

// console.log(solution(10));