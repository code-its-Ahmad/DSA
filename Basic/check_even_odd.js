function check_even_odd(num) {
    let rem = num % 2;
    if (rem == 0) {
        return true;
    } else {
        return false;
    }
}

let num = 78;
if (check_even_odd(num)) {
    console.log("Even");
} else {
    console.log("Odd");
}
