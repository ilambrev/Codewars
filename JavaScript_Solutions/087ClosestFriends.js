const phonebook = {
    'John': '(555) 010-3535',
    'Melissa': '(442) 130-5165',
    'Jack': '(333) 010-5135'
};

function closestFriends(history) {
    const callsDuration = {};

    history.forEach(call => {
        const [code, number, duration] = call.split(' ');
        const contactNumber = code + ' ' + number;
        let [hour, min, sec] = duration.split(':');
        const durationInSec = Number(hour) * 3600 + Number(min) * 60 + Number(sec);

        const friendName = Object.entries(phonebook).find(([k, v]) => v == contactNumber)[0];

        if (!callsDuration.hasOwnProperty(friendName)) {
            callsDuration[friendName] = 0;
        }

        callsDuration[friendName] += durationInSec;
    })

    return Object.entries(callsDuration).sort(([k1, v1], [k2, v2]) => v2 - v1).map(([k, v]) => k).slice(0, 3);
}

// console.log(closestFriends(['(555) 010-3535 00:13:24', '(442) 130-5165 01:36:26', '(333) 010-5135 01:38:24']));