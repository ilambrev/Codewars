function travel(r, zipcode) {
    const addresses = r.split(',').reduce((a, c) => {
        const firstSpaceIndex = c.indexOf(' ');
        const beforeLastSpaceIndex = c.length - 1 - 8;
        const houseNumber = c.slice(0, firstSpaceIndex);
        const address = c.slice(firstSpaceIndex + 1, beforeLastSpaceIndex);
        const zip = c.slice(beforeLastSpaceIndex + 1);

        if (!a.hasOwnProperty(zip)) {
            a[zip] = [];
        }

        a[zip].push([address, houseNumber]);

        return a;
    }, {});

    if (!zipcode) {
        return ':/';
    }

    if (!addresses.hasOwnProperty(zipcode)) {
        return zipcode + ':/';
    }

    return zipcode + ':' + addresses[zipcode].map(a => a[0]).join(',') + '/' + addresses[zipcode].map(a => a[1]).join(',');
}

// console.log(travel(
//     "123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432",
//     "OH 43071"
// ));
// console.log(travel(
//     "123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432",
//     "NY 56432"
// ));
// console.log(travel(
//     "123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432",
//     "NY 5643"
// ));