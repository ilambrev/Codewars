function generateChatRoomNames(users) {
    let result = [];
    const firstNames = {};

    users.forEach(user => {
        let [firstName, lastName] = user.split(' ').map(name => {
            name = name.toLowerCase();
            name = name.charAt(0).toUpperCase() + name.slice(1);

            return name;
        });

        result.push([firstName, lastName]);

        if (!firstNames.hasOwnProperty(firstName)) {
            firstNames[firstName] = { count: 0, initials: {} };
        }

        firstNames[firstName].count += 1;

        const userLastNameInitial = lastName.charAt(0);

        if (!firstNames[firstName].initials.hasOwnProperty(userLastNameInitial)) {
            firstNames[firstName].initials[userLastNameInitial] = 0;
        }

        firstNames[firstName].initials[userLastNameInitial] += 1;
    });

    result.forEach(user => {
        if (firstNames[user[0]].count === 1) {
            user.pop();

            return;
        }

        let userLastNameInitial = user[1].charAt(0);

        if (firstNames[user[0]].count > 1 && firstNames[user[0]].initials[userLastNameInitial] === 1) {
            user[1] = userLastNameInitial;
        }
    });

    result = result.map(user => user.join(' ')).sort((user1, user2) => user1.localeCompare(user2));

    return result;
}

// console.log(generateChatRoomNames(['Joe Bloggs', 'John Smith']));
// console.log(generateChatRoomNames(['Joe Bloggs', 'John Smith', 'Jane Doe']));
// console.log(generateChatRoomNames(['Joe Bloggs', 'John Smith', 'Jane Doe', 'Jane Bloggs']));
// console.log(generateChatRoomNames(['Joe Bloggs', 'John Smith', 'Jane Doe', 'Jane Bloggs', 'John Scott']));