function mix(s1, s2) {
    function countsLettersOccurrence(s, name) {
        return s.split('').reduce((acc, curr) => {
            if (curr >= 'a' && curr <= 'z') {
                if (!acc.hasOwnProperty(curr)) {
                    acc[curr] = { str: name, count: 0 };
                }

                acc[curr].count += 1;
            }

            return acc;
        }, {});
    }

    let result = '';

    const s1Letters = countsLettersOccurrence(s1, '1');
    const s2Letters = countsLettersOccurrence(s2, '2');

    for (const [letter, value] of Object.entries(s2Letters)) {
        if (s1Letters.hasOwnProperty(letter)) {
            if (value.count > s1Letters[letter].count) {
                s1Letters[letter].str = '2';
                s1Letters[letter].count = value.count;
            } else if (value.count == s1Letters[letter].count) {
                s1Letters[letter].str = '=';
            }

        } else {
            s1Letters[letter] = value;
        }
    }

    return Object.entries(s1Letters)
        .filter(([_, value]) => value.count > 1)
        .map(([key, value]) => `${value.str}:${key.repeat(value.count)}`)
        .sort()
        .sort((l1, l2) => l2.length - l1.length)
        .join('/');
}

// console.log(mix("Are they here", "yes, they are here")) // "2:eeeee/2:yy/=:hh/=:rr"
// console.log(mix("looping is fun but dangerous", "less dangerous than coding")) // "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"
// console.log(mix(" In many languages", " there's a pair of functions")) // "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt"
// console.log(mix("Lords of the Fallen", "gamekult")) // "1:ee/1:ll/1:oo"
// console.log(mix("codewars", "codewars")) // ""
// console.log(mix("A generation must confront the looming ", "codewarrs")) // "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr"