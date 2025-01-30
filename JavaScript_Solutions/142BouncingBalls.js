function bouncingBall(h, bounce, window) {
    let timesToSeeBall = -1;

    if (h > 0 && (bounce > 0 && bounce < 1) && window < h) {
        timesToSeeBall = 1;
        while (h > window) {
            h *= bounce;
            if (h > window) {
                timesToSeeBall += 2;
            }
        }
    }

    return timesToSeeBall;
}

// console.log(bouncingBall(3.0, 0.66, 1.5));
// console.log(bouncingBall(30.0, 0.66, 1.5));
// console.log(bouncingBall(3.0, 1.0, 1.5));