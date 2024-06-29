function luckCheck(ticket) {
    const regex = /[^0-9]/;

    if (!ticket || regex.test(ticket)) {
        throw new Error('Invalid ticket number');
    }

    const firstIndex = 0;
    const secondIndex = ticket.length / 2;

    function isTicketHalfsEqual(firstHalf, secondHalf) {
        return calcSumOfDigits(firstHalf) == calcSumOfDigits(secondHalf);
    }

    function calcSumOfDigits(str) {
        return str.split('').map(Number).reduce((acc, curr) => acc += curr, 0);
    }

    return isTicketHalfsEqual(ticket.slice(firstIndex, secondIndex), ticket.slice(ticket.length % 2 == 0 ? secondIndex : secondIndex + 1));
}

// console.log(luckCheck('003111'));
// console.log(luckCheck('813372'));
// console.log(luckCheck('17935'));
// console.log(luckCheck('56328116'));