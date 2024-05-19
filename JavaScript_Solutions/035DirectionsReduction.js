function dirReduc(arr) {
    let i = 0;

    while (i < arr.length - 1) {
        const firstDirection = arr[i];
        const secondDirection = arr[i + 1];

        if (firstDirection === 'NORTH' && secondDirection === 'SOUTH' ||
            firstDirection === 'SOUTH' && secondDirection === 'NORTH' ||
            firstDirection === 'EAST' && secondDirection === 'WEST' ||
            firstDirection === 'WEST' && secondDirection === 'EAST') {

            arr.splice(i, 2);

            if (i > 0) {
                i--;
            }
        } else {
            i++;
        }
    }

    return arr;
}

// console.log(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]));
// console.log(dirReduc(["NORTH", "SOUTH", "EAST", "WEST"]));
// console.log(dirReduc(["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]));