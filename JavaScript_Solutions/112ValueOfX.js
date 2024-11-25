function valueOfX(eq) {
    const [leftSide, rightSide] = eq.split('=');
    let result = 0;

    if (leftSide.indexOf('x') > -1) {
        result += sum(rightSide);
        result -= sum(replaceX(leftSide));
    } else {
        result += sum(leftSide);
        result -= sum(replaceX(rightSide));
    }

    function sum(numsAsString) {
        const nums = numsAsString.trim().split(' ');
        let sum = 0;
        let action = 0;

        for (let i = 0; i < nums.length; i++) {
            if (nums[i] == '+') {
                action = 0;
            } else if (nums[i] == '-') {
                action = 1;
            } else {
                if (action == 0) {
                    sum += Number(nums[i]);
                } else {
                    sum -= Number(nums[i]);
                }
            }
        }

        return sum;
    }

    function replaceX(numAsString) {
        if (numAsString.includes('- x ')) {
            numAsString = numAsString.replace('- x ', '');
        } else if (numAsString.includes('+ x ')) {
            numAsString = numAsString.replace('+ x ', '');
        } else if (numAsString.includes('x ')) {
            numAsString = numAsString.replace('x ', '');
        } else {
            numAsString = numAsString.replace('x', '');
        }

        return numAsString;
    }

    if (leftSide.includes('- x') || rightSide.includes('- x')) {
        result *= -1;
    }

    return result;
}

// console.log(valueOfX('x + 1 = 9 - 2'));
// console.log(valueOfX('x - 2 + 3 = 2'));
// console.log(valueOfX('x = + 2 - 5 + 9'));
// console.log(valueOfX('- 10 = x'));
// console.log(valueOfX('- x = - 1'));
// console.log(valueOfX('x - 0 + 0 = 0'));