function humanReadable(seconds) {

    const secTo = {
        hours: 3600,
        mins: 60,
    }

    const h = Math.floor(seconds / secTo.hours);
    const m = Math.floor((seconds - (h * secTo.hours)) / secTo.mins);
    const s = seconds - (h * secTo.hours + m * secTo.mins);


    return `${h < 10 ? '0' + h : h}:${m < 10 ? '0' + m : m}:${s < 10 ? '0' + s : s}`;
}

// console.log(humanReadable(0));
// console.log(humanReadable(59));
// console.log(humanReadable(60));
// console.log(humanReadable(90));
// console.log(humanReadable(3599));
// console.log(humanReadable(3600));
// console.log(humanReadable(45296));
// console.log(humanReadable(86399));
// console.log(humanReadable(86400));
// console.log(humanReadable(359999));