function meeting(x, need) {
    const maxNumOfChairsInRoom = 8;
    let result = [];

    if (need == 0) {
        return 'Game On';
    }

    for ([occupied, chairs] of x) {
        if (occupied.length < chairs) {
            const free = chairs - occupied.length;
            if (need >= free) {
                result.push(free);
                need -= free;
            } else {
                result.push(need);
                need = 0;
            }
        } else {
            result.push(0);
        }

        if (need == 0) {
            break;
        }
    }

    if (need > 0) {
        return 'Not enough!';
    }

    return result;
}

// console.log(meeting([['XXX', 3], ['XXXXX', 6], ['XXXXXX', 9]], 4));
// console.log(meeting([['XXX', 1], ['XXXXXX', 6], ['X', 2], ['XXXXXX', 8], ['X', 3], ['XXX', 1]], 5));
// console.log(meeting([['XX', 2], ['XXXX', 6], ['XXXXX', 4]], 0));