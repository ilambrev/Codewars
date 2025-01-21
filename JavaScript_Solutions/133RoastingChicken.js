function cookingTime(weight) {
    if (weight <= 0) {
        return 'There is no chicken!';
    }

    const weightInGramms = weight * 1000;
    const timeInMinutes = (weightInGramms / 450) * 20 + 20;
    let hours = Math.trunc(timeInMinutes / 60);
    let minutes = Math.ceil((timeInMinutes - (hours * 60)) / 5) * 5;

    if (minutes == 60) {
        hours++;
        minutes = 0;
    }

    if (hours == 0) {
        return `${minutes} mins`;
    } else if (minutes == 0) {
        return `${hours} ${hours > 1 ? 'hrs' : 'hr'}`;
    } else {
        return `${hours} ${hours > 1 ? 'hrs' : 'hr'} ${minutes} mins`;
    }
}

// console.log(cookingTime(1));
// console.log(cookingTime(2.2));
// console.log(cookingTime(0.3));