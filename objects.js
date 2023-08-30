//Object Literals and the Dot Notation
var table = {
    legs: 3,
    color: "brown",
    priceUSD: 100,
}
console.log(table.color);
/* here dot is used to acesses the colour of the table*/
//the alternative way is the bracket notation.
var car = {};
car.color = "red";
car["color"] = "green";
car["speed"] = 200;
car.speed = 100;
console.log(car); // {color: "green", speed: 100}
//use of bracket notation.
var arrOfKeys = ['speed', 'altitude', 'color'];
var drone = {
    speed: 100,
    altitude: 200,
    color: "red"
}
for (var i = 0; i < arrOfKeys.length; i++) {
    console.log(drone[arrOfKeys[i]])
}
