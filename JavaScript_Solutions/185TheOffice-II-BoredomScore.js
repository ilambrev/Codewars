function boredom(staff) {
    const departments = {
        'accounts': 1,
        'finance': 2,
        'canteen': 10,
        'regulation': 3,
        'trading': 6,
        'change': 6,
        'IS': 8,
        'retail': 5,
        'cleaning': 4,
        'pissing about': 25
    };

    const teamscores = Object.values(staff).reduce((acc, curr) => acc += departments[curr], 0);

    if (teamscores <= 80) {
        return 'kill me now';
    } else if (teamscores < 100) {
        return 'i can handle this';
    } else {
        return 'party time!!';
    }
}

/*
console.log(boredom({
    tim: 'change',
    jim: 'accounts',
    randy: 'canteen',
    sandy: 'change',
    andy: 'change',
    katie: 'IS',
    laura: 'change',
    saajid: 'IS',
    alex: 'trading',
    john: 'accounts',
    mr: 'finance'
}));
console.log(boredom({
    tim: 'IS',
    jim: 'finance',
    randy: 'pissing about',
    sandy: 'cleaning',
    andy: 'cleaning',
    katie: 'cleaning',
    laura: 'pissing about',
    saajid: 'regulation',
    alex: 'regulation',
    john: 'accounts',
    mr: 'canteen'
}));
console.log(boredom({
    tim: 'accounts',
    jim: 'accounts',
    randy: 'pissing about',
    sandy: 'finance',
    andy: 'change',
    katie: 'IS',
    laura: 'IS',
    saajid: 'canteen',
    alex: 'pissing about',
    john: 'retail',
    mr: 'pissing about'
}));
*/