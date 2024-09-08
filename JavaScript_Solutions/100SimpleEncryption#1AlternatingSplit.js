function encrypt(text, n) {
    if (!text || n < 1) {
        return text;
    }

    let encryptedText = text;

    for (let i = 1; i <= n; i++) {
        let oddChars = '';
        let evenChars = '';

        for (let j = 0; j < text.length; j++) {
            if (j % 2 == 0) {
                evenChars += encryptedText.charAt(j);
            } else {
                oddChars += encryptedText.charAt(j);
            }
        }

        encryptedText = oddChars + evenChars;
    }

    return encryptedText;
}

function decrypt(encryptedText, n) {
    if (!encryptedText || n < 1) {
        return encryptedText;
    }

    let decryptedText = encryptedText;

    for (let i = 1; i <= n; i++) {
        const borderIndex = Math.floor(decryptedText.length / 2);
        let oddChars = decryptedText.slice(0, borderIndex);
        let evenChars = decryptedText.slice(borderIndex);

        decryptedText = '';

        for (let j = 0; j < encryptedText.length; j++) {
            if (j % 2 == 0) {
                decryptedText += evenChars.charAt(Math.floor(j / 2));
            } else {
                decryptedText += oddChars.charAt(Math.floor(j / 2));
            }

        }
    }

    return decryptedText;
}

// console.log(encrypt('', 1));
// console.log(encrypt('012345', -1));
// console.log(encrypt('012345', 0));
// console.log(encrypt('012345', 1));
// console.log(encrypt('012345', 2));
// console.log(encrypt('012345', 3));

// console.log(decrypt('', 1));
// console.log(decrypt('135024', -1));
// console.log(decrypt('135024', 1));
// console.log(decrypt('304152', 2));
// console.log(decrypt('012345', 3));