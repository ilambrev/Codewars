function meeting(x) {
    const index = x.findIndex(r => r == 'O');

    if (index == -1) {
        return 'None available!';
    }

    return index;
}

// console.log(meeting(['X', 'O', 'X']));
// console.log(meeting(['O', 'X', 'X', 'X', 'X']));
// console.log(meeting(['X', 'X', 'X', 'X', 'X']));