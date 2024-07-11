function catMouse(x, j) {
    const catIndex = x.indexOf('C');
    const dogIndex = x.indexOf('D');
    const mouseIndex = x.indexOf('m');

    if (catIndex == -1 || dogIndex == -1 || mouseIndex == -1) {
        return 'boring without all three';
    }

    if (Math.abs(catIndex - mouseIndex) <= j + 1) {
        if ((dogIndex > catIndex && dogIndex < mouseIndex) || (dogIndex < catIndex && dogIndex > mouseIndex)) {
            return 'Protected!';
        }
        return 'Caught!';
    }

    return 'Escaped!';
}

// console.log(catMouse('..C.....m...D', 5));
// console.log(catMouse('.....C............m......D', 5));
// console.log(catMouse('...m.........C...D', 10));
// console.log(catMouse('...m....D....C.......', 10));
// console.log(catMouse('...m.........C....', 10));
// console.log(catMouse('............C.............D..m...', 8));