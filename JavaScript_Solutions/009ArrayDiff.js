function arrayDiff(a, b) {

    const removeElements = (arr, elementValue) => {
        return arr.reduce((acc, curr) => {
            if (curr != elementValue) {
                acc.push(curr);
            }

            return acc;
        }, [])
    };

    for (let element of b) {
        a = removeElements(a, element);
    }

    return a;

}

// console.log(arrayDiff([1, 2, 2, 2, 3], [2]));