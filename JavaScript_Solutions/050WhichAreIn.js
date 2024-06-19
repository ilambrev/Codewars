function inArray(array1, array2) {
    const result = [];

    array1.forEach(s1 => {
        if (array2.find(s2 => s2.includes(s1)) != undefined) {
            result.push(s1);
        }
    });

    return result.sort((s1, s2) => s1.localeCompare(s2));
}

// console.log(inArray(['arp', 'live', 'strong'], ['lively', 'alive', 'harp', 'sharp', 'armstrong']));
// console.log(inArray(['tarp', 'mice', 'bull'], ['lively', 'alive', 'harp', 'sharp', 'armstrong']));