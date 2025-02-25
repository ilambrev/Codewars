function landPerimeter(arr) {
    const islandsMap = arr.map(r => r.split(''));
    let perimeter = 0;

    for (let i = 0; i < islandsMap.length; i++) {
        for (let j = 0; j < islandsMap[i].length; j++) {
            if (islandsMap[i][j] == 'X') {
                if (i == 0 || islandsMap[i - 1][j] == 'O') {
                    perimeter++;
                }
                if (j == 0 || islandsMap[i][j - 1] == 'O') {
                    perimeter++;
                }
                if (i == islandsMap.length - 1 || islandsMap[i + 1][j] == 'O') {
                    perimeter++;
                }
                if (j == islandsMap[i].length - 1 || islandsMap[i][j + 1] == 'O') {
                    perimeter++;
                }
            }
        }
    }

    return `Total land perimeter: ${perimeter}`;
}

// console.log(landPerimeter([
//     'OXOOOX',
//     'OXOXOO',
//     'XXOOOX',
//     'OXXXOO',
//     'OOXOOX',
//     'OXOOOO',
//     'OOXOOX',
//     'OOXOOO',
//     'OXOOOO',
//     'OXOOXX'
// ]));
// console.log(landPerimeter([
//     'OXOOO',
//     'OOXXX',
//     'OXXOO',
//     'XOOOO',
//     'XOOOO',
//     'XXXOO',
//     'XOXOO',
//     'OOOXO',
//     'OXOOX',
//     'XOOOO',
//     'OOOXO'
// ]));
// console.log(landPerimeter([
//     'XXXXXOOO',
//     'OOXOOOOO',
//     'OOOOOOXO',
//     'XXXOOOXO',
//     'OXOXXOOX'
// ]));
// console.log(landPerimeter([
//     'XOOOXOO',
//     'OXOOOOO',
//     'XOXOXOO',
//     'OXOXXOO',
//     'OOOOOXX',
//     'OOOXOXX',
//     'XXXXOXO'
// ]));
// console.log(landPerimeter([
//     'OOOOXO',
//     'XOXOOX',
//     'XXOXOX',
//     'XOXOOO',
//     'OOOOOO',
//     'OOOXOO',
//     'OOXXOO'
// ]));