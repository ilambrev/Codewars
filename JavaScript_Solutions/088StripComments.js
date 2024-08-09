function solution(text, markers) {
    const rows = text.split('\n');
    const strip = (row) => {
        markers.forEach(marker => {
            if (row.includes(marker)) {
                row = row.slice(0, row.indexOf(marker));
            }
        })

        return row.trimEnd();
    };

    return rows.map(strip).join('\n');
}

// console.log(solution('aa / bb\ncc ^ dd\nee $ ff', ['/', '^', '$']));