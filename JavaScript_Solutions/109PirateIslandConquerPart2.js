function conquerIsland(map) {

    function findElementsCoordinates(element) {
        const coordinates = [];

        for (let i = 0; i < 8; i++) {
            for (let j = 0; j < 8; j++) {
                if (map[i][j] == element) {
                    coordinates.push([i, j]);
                }
            }
        }

        return coordinates;
    }

    function findDistance(targetCoordinates, piratePosition) {
        return Math.abs(targetCoordinates[0] - piratePosition[0]) + Math.abs(targetCoordinates[1] - piratePosition[1]);
    }

    function findClosestDistance(coordinatesWithDistance) {
        const sortedCoordinates = coordinatesWithDistance.sort((c1, c2) => {
            if (c1[2] < c2[2]) {
                return -1;
            } else if (c1[2] > c2[2]) {
                return 1;
            } else if (c1[0] < c2[0]) {
                return -1;
            } else if (c1[0] > c2[0]) {
                return 1;
            } else if (c1[1] < c2[1]) {
                return -1;
            } else if (c1[1] > c2[1]) {
                return 1;
            } else {
                return 0;
            }
        });

        const bestDistance = sortedCoordinates[0][2];

        return sortedCoordinates.filter(c => c[2] == bestDistance).map(c => c.slice(0, 2));
    }

    let coordinates = findElementsCoordinates('u');

    if (coordinates.length == 0) {
        coordinates = findElementsCoordinates('m');
    }

    if (coordinates.length == 0) {
        return coordinates;
    }

    const pirateInitialPositions = findElementsCoordinates('p');

    const coordinatesWithDistance = [];

    pirateInitialPositions.forEach(p => {
        coordinates.forEach(c => {
            let coordinatesExists = false;
            const distance = findDistance(c, p);
            const newCoordinates = [...c, distance];

            for (let cwd of coordinatesWithDistance) {
                if (cwd.join() == newCoordinates.join()) {
                    coordinatesExists = true;
                    break;
                }
            }
            if (!coordinatesExists) {
                coordinatesWithDistance.push(newCoordinates);
            }
        });
    });

    return findClosestDistance(coordinatesWithDistance);
}

// console.log(conquerIsland(
//     [
//         ['~', '~', '~', 'u', '~', 'p', '~', 'p'],
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~']
//     ]
// ));

// console.log(conquerIsland(
//     [
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['u', '~', '~', '~', '~', '~', 'p', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['p', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['u', '~', '~', '~', '~', '~', '~', '~']
//     ]
// ));

// console.log(conquerIsland(
//     [
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', 'p', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', 'p', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~']
//     ]
// ));

// console.log(conquerIsland(
//     [
//         ['~', '~', 'u', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', 'p', '~', '~', '~', '~'],
//         ['u', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', 'p', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', 'u']
//     ]
// ));

// console.log(conquerIsland(
//     [
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', 'p', '~', '~', '~'],
//         ['~', '~', 'm', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', 'u', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', 'p']
//     ]
// ));

// console.log(conquerIsland(
//     [
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', 'p', 'm', '~', '~', '~', '~'],
//         ['m', '~', 'm', 'p', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', 'm', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', 'm', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~']
//     ]
// ));

// console.log(conquerIsland(
//     [
//         ['u', '~', '~', '~', '~', '~', '~', '~'],
//         ['u', '~', '~', '~', '~', '~', '~', '~'],
//         ['u', '~', 'u', '~', '~', '~', 'm', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', 'p', '~', '~', '~'],
//         ['~', 'p', '~', 'm', '~', '~', '~', '~'],
//         ['~', '~', '~', '~', '~', '~', '~', '~']
//     ]
// ));