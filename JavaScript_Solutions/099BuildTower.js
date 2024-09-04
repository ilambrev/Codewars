function towerBuilder(nFloors) {
    const tower = [];
    const elementsOnFloor = (nFloors * 2) - 1;

    for (let i = 0; i < nFloors; i++) {
        const floor = " ".repeat(i) + "*".repeat(elementsOnFloor - (2 * i)) + " ".repeat(i);
        tower.unshift(floor);
    }

    return tower;
}

// console.log(towerBuilder(3));
// console.log(towerBuilder(6));