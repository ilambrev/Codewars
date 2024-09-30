function removeParentheses(s) {
    let openParenthesisNum = 0;
    let closeParenthesisNum = 0;
    const result = [];

    s.split('').forEach(c => {
        if (c != '(' && c != ')' && openParenthesisNum == 0) {
            result.push(c);
        } else if (c == '(') {
            openParenthesisNum++;
        } else if (c == ')') {
            closeParenthesisNum++;
        }

        if (openParenthesisNum == closeParenthesisNum) {
            openParenthesisNum = 0;
            closeParenthesisNum = 0;
        }
    });

    return result.join('');
}

// console.log(removeParentheses('example(unwanted thing)example'));
// console.log(removeParentheses('example (unwanted thing) example'));
// console.log(removeParentheses('a (bc d)e'));
// console.log(removeParentheses('a(b(c))'));
// console.log(removeParentheses('hello example (words(more words) here) something'));
// console.log(removeParentheses('(first group) (second group) (third group)'));