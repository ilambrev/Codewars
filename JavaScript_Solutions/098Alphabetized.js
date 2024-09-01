function alphabetized(s) {
    const letters = s.split('').filter(l => l >= 'A' && l <= 'Z' || l >= 'a' && l <= 'z');

    return letters.sort((l1, l2) => l1.toLowerCase().charCodeAt(0) - l2.toLowerCase().charCodeAt(0)).join('');
}

// console.log(alphabetized('The Holy Bible'));
// console.log(alphabetized('^_`'));