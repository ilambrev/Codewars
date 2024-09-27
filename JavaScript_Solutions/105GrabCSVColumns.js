function csvColumns(csv, indices) {

    const table = csv.split('\n').reduce((acc, curr) => {
        const row = curr.split(',');
        acc.push(row);

        return acc;
    }, []);

    const validIndices = indices.filter(i => i < table[0].length);

    if (!validIndices.length) {
        return '';
    }

    function getColumns() {
        return columns = table.reduce((acc, curr) => {
            const row = curr.filter((num, i) => validIndices.includes(i));
            acc.push(row)

            return acc;
        }, []);
    }

    return getColumns().map(row => row.join(',')).join('\n');
}

// console.log(csvColumns('1,2,3\n4,5,6', [0, 1])); //"1,2\n4,5"
// console.log(csvColumns('1,2\n3,4\n5,6', [5, 6, 7])); //""
// console.log(csvColumns('a,b,c,d,e\n1,2,3,4,5\nf,g,h,i,j', [1, 3, 5, 7])); //"b,d\n2,4\ng,i"
// console.log(csvColumns('1\n2\n3\n4\n5', [0, 1])); //"1\n2\n3\n4\n5"
// console.log(csvColumns('1\n2\n3\n4\n5', [1])); //""
// console.log(csvColumns('1,2,3,4,5,6,7,8,9', [0, 2, 4, 6, 8])); //"1,3,5,7,9"