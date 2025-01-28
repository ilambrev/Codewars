function queueTime(customers, n) {
    let totalTime = 0;

    if (customers.length == 0) {
        return totalTime;
    } else if (n == 1) {
        totalTime = customers.reduce((acc, curr) => acc + curr, 0);
    } else if (customers.length <= n) {
        totalTime = customers.sort((c1, c2) => c2 - c1)[0];
    } else {
        let i = n - 1;
        const currentCustomers = customers.slice(0, n);

        while (currentCustomers.reduce((acc, curr) => acc + curr, 0) > 0) {
            totalTime++;
            for (let j = 0; j < currentCustomers.length; j++) {
                if (currentCustomers[j] > 0) {
                    currentCustomers[j] -= 1;
                }
                if (currentCustomers[j] == 0 && i < customers.length - 1) {
                    i++;
                    currentCustomers[j] = customers[i];
                }
            }
        }
    }

    return totalTime;
}

// console.log(queueTime([], 1));
// console.log(queueTime([1, 2, 3, 4], 1));
// console.log(queueTime([2, 2, 3, 3, 4, 4], 2));
// console.log(queueTime([1, 2, 3, 4, 5], 100));
// console.log(queueTime([5, 3, 4], 1));
// console.log(queueTime([10, 2, 3, 3], 2));
// console.log(queueTime([2, 3, 10, 2], 2));