function makeSentence(parts) {
    const regexp = /\.{2,}/;
    let result = '';

    for (let i = 0; i < parts.length; i++) {
        if (parts[i] == ',' || parts[i].match(/^\.+/) || i == 0) {
            result += parts[i];
        } else {
            result += ` ${parts[i]}`;
        }
    }

    const match = regexp.exec(result);
    if (match) {
        result = result.replace(match, '.');
    }

    if (result.charAt(result.length - 1) != '.') {
        result += '.';
    }

    return result;
}

// console.log(makeSentence(['hello', ',', 'my', 'dear']));
// console.log(makeSentence(['hello', 'world']))