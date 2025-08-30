function findShort(s) {
    return s.split(/\s+/).sort((w1, w2) => w1.length - w2.length)[0].length;
}

// console.log(findShort("bitcoin take over the world maybe who knows perhaps"));
// console.log(findShort("turns out random test cases are easier than writing out basic ones"));
// console.log(findShort("Let's travel abroad shall we"));