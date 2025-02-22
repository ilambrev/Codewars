function isValidWalk(walk) {
    const timeForWalk = 10;
    const stepTime = 1;
    const personCoordinates = [0, 0];

    if (walk.length != timeForWalk) {
        return false
    }

    for (let step of walk) {
        switch (step) {
            case 'n':
                personCoordinates[0]++;
                break;
            case 's':
                personCoordinates[0]--;
                break;
            case 'e':
                personCoordinates[1]++;
                break;
            case 'w':
                personCoordinates[1]--;
                break;
        }
    }

    return personCoordinates[0] == 0 && personCoordinates[1] == 0;
}

// console.log(isValidWalk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']));
// console.log(isValidWalk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']));
// console.log(isValidWalk(['w']));
// console.log(isValidWalk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']));