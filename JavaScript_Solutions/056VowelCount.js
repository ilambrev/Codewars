function getCount(str) {
    const vowels = 'aeiou';

    return str.split('').filter(e => vowels.includes(e)).length;
}

// console.log(getCount('abracadabra'));