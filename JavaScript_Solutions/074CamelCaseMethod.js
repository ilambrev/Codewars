String.prototype.camelCase = function () {
    return this.toLowerCase()
        .split(/\s+/)
        .map(w => w.charAt(0).toUpperCase() + w.slice(1))
        .join('');
}

// console.log('hello case'.camelCase());
// console.log('camel case word'.camelCase());