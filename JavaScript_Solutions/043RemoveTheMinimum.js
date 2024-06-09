function removeSmallest(numbers) {
    if (numbers.length > 0) {
        result = [...numbers];

        const smalestElement = result.sort((n1, n2) => n1 - n2)[0];
        const indexOfElement = numbers.findIndex(e => e === smalestElement);

        result = [...numbers];
        result.splice(indexOfElement, 1);

        return result;
    }

    return [];
}

// console.log(removeSmallest([1, 2, 3, 4, 5]));
// console.log(removeSmallest([5, 3, 2, 1, 4]));
// console.log(removeSmallest([2, 2, 1, 2, 1]));
// console.log(removeSmallest([336, 184, 360, 84, 104]));