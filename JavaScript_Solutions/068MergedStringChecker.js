function isMerge(s, part1, part2) {
    if (s.length != part1.length + part2.length) {
        return false;
    }

    const stringSorted = s.split('').sort((l1, l2) => l1.localeCompare(l2)).join('');
    const substringsSorted = (part1 + part2).split('').sort((l1, l2) => l1.localeCompare(l2)).join('');

    if (stringSorted !== substringsSorted) {
        return false;
    }

    function checkOrder(string, substring) {
        let currentIndex = string.indexOf(substring.charAt(0));

        for (let i = 1; i < substring.length; i++) {
            const index = string.indexOf(substring.charAt(i), currentIndex + 1);

            if (index <= currentIndex) {
                return false;
            }

            currentIndex = index;
        }

        return true;
    }

    return checkOrder(s, part1) && checkOrder(s, part2);
}

// console.log(isMerge('codewars', 'cdw', 'oears'));
// console.log(isMerge('xcyc', 'xc', 'yc'));
// console.log(isMerge('xcyc', 'yc', 'xc'));
// console.log(isMerge('xcyc', 'xc', 'cy'));
// console.log(isMerge('xcyc', 'cy', 'xc'));
// console.log(isMerge('codewars', 'code', 'wars'));
// console.log(isMerge('codewars', 'cdwr', 'oeas'));
// console.log(isMerge('Making progress', 'Mak pross', 'inggre'));
// console.log(isMerge('codewars', 'code', 'code'));
// console.log(isMerge('More progress', 'More ess', 'pro'));