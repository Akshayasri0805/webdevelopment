/*The functional programming paradigm
 In functional programming, we use a lot of functions and variables.
function getTotal(a,b) {
    return a + b
}
var num1 = 2;
var num2 = 3;

var total = getTotal(num1, num2);
When writing FP code, we keep data and functionality separate and pass data into functions only when we want something computed.
 in functional programming, functions return new values and then use those values somewhere else in the code.
 function getDistance(mph, h) {
    return mph * h
}
var mph = 60;
var h = 2;
var distance = getDistance(mph, h);

console.log(distance); // <====== THIS HERE!
//oops 
//creating an object
var virtualPet = {
    sleepy: true,
    nap: function() {
        this.sleepy = false
    }
}
console.log(virtualPet.sleepy) // true
virtualPet.nap()
console.log(virtualPet.sleepy) // false
//first class functions:
function addTwoNums(a, b) {
    console.log(a + b)
}

function randomNum() {
    return Math.floor((Math.random() * 10) + 1);
}
function specificNum() { return 42 };

var useRandom = true;

var getNumber;

if(useRandom) {
    getNumber = randomNum
} else {
    getNumber = specificNum
}

addTwoNums(getNumber(), getNumber())
//Higher-order functions
function addTwoNums(getNumber1, getNumber2) {
    console.log(getNumber1() + getNumber2());
}
//Pure functions and side-effects
function addTwoNums(a, b) {
    console.log(a + b)
}
*/