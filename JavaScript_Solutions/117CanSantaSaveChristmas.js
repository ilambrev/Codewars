function determineTime(durations) {
    const DELIVERY_TIME_LIMIT_IN_SECONDS = 24 * 3600;
    let neededTimeInSeconds = 0;

    for (let duration of durations) {
        let [hours, minutes, seconds] = duration.split(':');
        neededTimeInSeconds += Number(hours) * 3600 + Number(minutes) * 60 + Number(seconds);
    }

    return neededTimeInSeconds <= DELIVERY_TIME_LIMIT_IN_SECONDS;
}

// console.log(determineTime(['00:30:00', '02:30:00', '00:15:00']));
// console.log(determineTime([]));
// console.log(determineTime(['04:30:00', '02:00:00', '01:30:00', '16:00:00']));
// console.log(determineTime(['12:00:00', '12:00:00']));
// console.log(determineTime(['12:00:00', '12:00:01']));
// console.log(determineTime(['06:00:00', '12:00:00', '06:30:00']));