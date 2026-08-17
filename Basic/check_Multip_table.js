function printTable(num) {
    for (let i = 1; i <= 10; i++) {
        console.log(num + " * " + i + " = " + (num * i));
    }
}

let num = 10;
console.log("Multiplication Table of " + num);
printTable(num);
