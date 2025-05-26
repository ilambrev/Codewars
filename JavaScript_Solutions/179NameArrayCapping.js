function capMe(names) {
    return names.map(n => n.charAt(0).toUpperCase() + n.slice(1).toLowerCase());
}

// console.log(capMe(["jo", "nelson", "jurie"]));
// console.log(capMe(["KARLY", "DANIEL", "KELSEY"]));
// console.log(capMe(['johnny']));
// console.log(capMe(['RALPH', 'GEORGIA', 'CHRISTINA']));