//Program for sum of n natural numbers
let findsum = function (num) {
    if (num == 0) {
        return 0;
    }
    return num + findsum(num - 1);
}
let num = 5;
console.log(findsum(num));
