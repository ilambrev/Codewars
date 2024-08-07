const format = function (str, obj) {
    const strToReplace = (s) => {
        if (Array.isArray(obj)) {
            const index = Number(s);

            if (!isNaN(index)) {
                return obj[index]
            }
        } else {
            if (obj.hasOwnProperty(s)) {
                return obj[s];
            }
        }
        return -1;
    };

    const map = str.split('').reduce((a, c, i) => {
        if (c == '{' || c == '}') {
            a.push(i);
        }

        return a;
    }, []);

    let resultStr = str.slice(0, map[0]);

    for (let i = 0; i < map.length; i += 2) {
        const key = str.slice(map[i] + 1, map[i + 1]);
        let s = strToReplace(key);

        if (s == -1) {
            s = `{${key}}`;
        }


        resultStr += i + 1 < map.length - 1 ? s + str.slice(map[i + 1] + 1, map[i + 2]) : s;
    }

    return resultStr + str.slice(map[map.length - 1] + 1);
}

// console.log(format('Hello {foo} - make me a {bar}', { foo: 'Jack', bar: 'sandwich' }));
// console.log(format('Hello {foo} - {foobar} make me a {bar}... {foo}!!?', { bar: 'sandwich {foo}', foo: 'Jack' }));
// console.log(format('Hello {0} - {foobar} make me {2} {1} - I\'m full..', ['Jack', 'sandwiches', 0]));