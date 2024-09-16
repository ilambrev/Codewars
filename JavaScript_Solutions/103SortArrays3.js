sortme = function (courses) {
    return courses.sort((c1, c2) => {
        let [name1, num1] = c1.split('-');
        let [name2, num2] = c2.split('-');

        num1 = Number(num1);
        num2 = Number(num2);

        if (num1 < num2) {
            return -1;
        } else if (num1 > num2) {
            return 1;
        } else {
            return name1.localeCompare(name2);
        }
    });
}

// console.log(sortme(["web-1305", "site-1305", "web-1304", "site-1304"]));
// console.log(sortme(['aeb-1305', 'site-1305', 'play-1215', 'web-1304', 'site-1304', 'beb-1305']));
// console.log(sortme(['aeb-1305', 'aeb-1305']));
// console.log(sortme([]));