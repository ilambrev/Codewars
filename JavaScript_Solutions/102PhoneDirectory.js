function phone(strng, num) {
    const forbidenAddressSymbols = new Set(['~', '`', '"', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '=', ';', '<', '>', '?', '/', ',', ':', '\'']);
    const phoneBook = [];
    const rows = strng.split('\n').filter(r => r != '');

    for (let row of rows) {
        let data = row;
        let startIndex = data.indexOf('<');
        let endIndex = data.indexOf('>');

        const name = data.substring(startIndex + 1, endIndex);
        data = (data.slice(0, startIndex) + data.slice(endIndex + 1)).trim();

        startIndex = data.indexOf('+');
        let phone = data.substring(startIndex + 1, data.length < startIndex + 16 ? data.length : startIndex + 16).trim();
        data = (data.slice(0, startIndex) + data.slice(data.length < startIndex + 16 ? data.length + 1 : startIndex + 16)).trim();

        let lastSymbol = phone.charAt(phone.length - 1);

        if (isNaN(Number(lastSymbol))) {
            phone = phone.slice(0, phone.length - 1);
        }

        let address = data
            .split('')
            .filter(symbol => !forbidenAddressSymbols.has(symbol))
            .map(symbol => symbol == '_' ? ' ' : symbol)
            .join('')
            .trim();

        address = address.split(' ').filter(str => str != '' && str != ' ').join(' ').trim();

        const record = { phone, name, address };

        phoneBook.push(record);
    }

    const matches = phoneBook.filter(rec => rec.phone == num);

    if (matches.length > 1) {
        return `Error => Too many people: ${num}`;
    } else if (matches.length == 0) {
        return `Error => Not found: ${num}`;
    } else {
        return `Phone => ${matches[0].phone}, Name => ${matches[0].name}, Address => ${matches[0].address}`;
    }
}

// const strng = "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010\n"
//     + "+1-541-984-3012 <P Reed> /PO Box 530; Pollocksville, NC-28573\n :+1-321-512-2222 <Paul Dive> Sequoia Alley PQ-67209\n"
//     + "+1-741-984-3090 <Peter Reedgrave> _Chicago\n :+1-921-333-2222 <Anna Stevens> Haramburu_Street AA-67209\n"
//     + "+1-111-544-8973 <Peter Pan> LA\n +1-921-512-2222 <Wilfrid Stevens> Wild Street AA-67209\n"
//     + "<Peter Gone> LA ?+1-121-544-8974 \n <R Steell> Quora Street AB-47209 +1-481-512-2222\n"
//     + "<Arthur Clarke> San Antonio $+1-121-504-8974 TT-45120\n <Ray Chandler> Teliman Pk. !+1-681-512-2222! AB-47209,\n"
//     + "<Sophia Loren> +1-421-674-8974 Bern TP-46017\n <Peter O'Brien> High Street +1-908-512-2222; CC-47209\n"
//     + "<Anastasia> +48-421-674-8974 Via Quirinal Roma\n <P Salinger> Main Street, +1-098-512-2222, Denver\n"
//     + "<C Powel> *+19-421-674-8974 Chateau des Fosses Strasbourg F-68000\n <Bernard Deltheil> +1-498-512-2222; Mount Av.  Eldorado\n"
//     + "+1-099-500-8000 <Peter Crush> Labrador Bd.\n +1-931-512-4855 <William Saurin> Bison Street CQ-23071\n"
//     + "<P Salinge> Main Street, +1-098-512-2222, Denve\n";

// console.log(phone(strng, '48-421-674-8974'));
// console.log(phone(strng, '1-921-512-2222'));
// console.log(phone(strng, '1-908-512-2222'));
// console.log(phone(strng, '1-541-754-3010'));
// console.log(phone(strng, '1-121-504-8974'));
// console.log(phone(strng, '1-498-512-2222'));
// console.log(phone(strng, '1-098-512-2222'));
// console.log(phone(strng, '5-555-555-5555'));