function friend(friends) {
    const friendNameLength = 4;

    return friends.filter(f => f.length === friendNameLength);
}

// console.log(friend(['Ryan', 'Kieran', 'Jason', 'Yous']));
// console.log(friend(['Ryan', 'Kieran', 'Mark']));