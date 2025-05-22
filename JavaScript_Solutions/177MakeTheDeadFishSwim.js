function parse(data) {
    let value = 0;
    const result = [];

    for (let i = 0; i < data.length; i++) {
        switch (data.charAt(i)) {
            case 'i':
                value++;
                break;
            case 'd':
                value--;
                break;
            case 's':
                value = value ** 2;
                break;
            case 'o':
                result.push(value);
                break;
        }
    }

    return result;
}

// console.log(parse('iiisdoso'));
// console.log(parse('iiisdosodddddiso'));
// console.log(parse('iiisxxxdoso'));