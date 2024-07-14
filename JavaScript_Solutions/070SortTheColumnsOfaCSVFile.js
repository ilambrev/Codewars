function sortCsvColumns(csvFileContent) {
    const rows = csvFileContent.split('\n').map(row => row.split(';'))
    const columns = rowsToColumns(rows);

    columns.sort((c1, c2) => c1[0].localeCompare(c2[0]));

    const rowsSorted = rowsToColumns(columns);

    function rowsToColumns(arr) {
        const newArr = [];
        for (let i = 0; i < arr[0].length; i++) {
            const row = [];
            for (let j = 0; j < arr.length; j++) {
                row.push(arr[j][i]);
            }
            newArr.push(row);
        }
        return newArr;
    }

    return rowsSorted.map(r => r.join(';')).join('\n');
}

// console.log(sortCsvColumns('Dentzil;myjinxin2015;raulbc777;smile67;SteffenVogel_79\n3907;17945;10091;10088;10132\n48;2;12;13;11'));