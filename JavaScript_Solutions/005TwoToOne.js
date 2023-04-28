function longest(s1, s2) {

    return Array.from(new Set((s1 + s2))).sort((a, b) => a.localeCompare(b)).join('');

}

// console.log(longest("xyaabbbccccdefww", "xxxxyyyyabklmopq"));
// console.log(longest("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"));
// console.log(longest("aretheyhere", "yestheyarehere"));
// console.log(longest("loopingisfunbutdangerous", "lessdangerousthancoding"));
// console.log(longest("inmanylanguages", "theresapairoffunctions"));