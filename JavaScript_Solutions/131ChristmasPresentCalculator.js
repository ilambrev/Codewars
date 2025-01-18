function countPresents(prod, presents) {
    const timeInSeconds = 24 * 60 * 60;

    let workCapacity = Object.values(prod).reduce((acc, curr) => acc += timeInSeconds * curr, 0);
    const timesForPresentsInSeconds = presents.reduce((acc, curr) => {
        const digits = curr.split(':').map(Number);
        const seconds = digits[0] * 60 * 60 + digits[1] * 60 + digits[2];
        acc.push(seconds);

        return acc;
    }, []).sort((t1, t2) => t1 - t2);

    let counter = 0;

    for (let time of timesForPresentsInSeconds) {
        if (workCapacity - time >= 0) {
            counter++;
            workCapacity -= time;
        } else {
            break;
        }
    }

    return counter;
}

// console.log(countPresents(
//     { 'Santa': 1, 'elf_1': 1, 'elf_2': 2 },
//     ['01:00:00', '06:00:00', '12:00:00', '18:00:00', '24:00:00', '36:00:00']
// ));