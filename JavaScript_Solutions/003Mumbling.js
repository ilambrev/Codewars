function accum(s) {

    let result = s.split('');

    for (let i = 0; i < result.length; i++) {

        result[i] = result[i].toUpperCase() + result[i].toLowerCase().repeat(i);

    }

    return result.join('-');

}

// console.log(accum("abcd"));
// console.log(accum("RqaEzty"));
// console.log(accum("cwAt"));
// console.log(accum("ZpglnRxqenU"));
// console.log(accum("NyffsGeyylB"));
// console.log(accum("MjtkuBovqrU"));
// console.log(accum("EvidjUnokmM"));
// console.log(accum("HbideVbxncC"));