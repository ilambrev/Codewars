function solution(list) {
    let result = '';

    for (let i = 0; i < list.length; i++) {
        if (i == list.length - 1) {
            result += list[i];
        }
        for (let j = i; j < list.length - 1; j++) {
            if (Math.abs(list[j + 1] - list[j]) != 1) {
                result += j == i ? list[i] : j - i > 1 ? list[i] + '-' + list[j] : list[i] + ',' + list[j];
                result += ',';
                i = j;
                break;
            } if (j == list.length - 2) {
                result += j + 1 - i > 1 ? list[i] + '-' + list[j + 1] : list[i] + ',' + list[j + 1];
                i = j + 1;
            }
        }
    }

    return result;
}

// console.log(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]));
// console.log(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]));