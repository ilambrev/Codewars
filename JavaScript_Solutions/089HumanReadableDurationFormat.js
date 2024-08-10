function formatDuration(seconds) {
    const timeUnitsToSeconds = [
        ['year', 31536000],
        ['day', 86400],
        ['hour', 3600],
        ['minute', 60],
        ['second', 1]
    ]

    if (seconds < 0) {
        return 'Тhe function does not accept negative values';
    }

    if (seconds == 0) {
        return 'now';
    }

    const timeUnits = [];
    const convert = (seconds, value) => Math.floor(seconds / value);

    for (let [unit, value] of timeUnitsToSeconds) {
        let convertedValue = convert(seconds, value);

        if (convertedValue > 0) {
            timeUnits.push(convertedValue == 1 ? `${convertedValue} ${unit}` : `${convertedValue} ${unit}s`);
            seconds -= convertedValue * value;

            if (seconds == 0) {
                break;
            }
        }
    }

    let result = '';

    if (timeUnits.length == 1) {
        result = timeUnits[0];
    } else {
        result = timeUnits.slice(0, timeUnits.length - 1).join(', ') + ' and ' + timeUnits[timeUnits.length - 1];
    }

    return result;
}

// console.log(formatDuration(1));
// console.log(formatDuration(62));
// console.log(formatDuration(120));
// console.log(formatDuration(3600));
// console.log(formatDuration(3662));