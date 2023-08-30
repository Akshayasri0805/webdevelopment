//without passing parameters.

function addtwo(){
    var x= 10;
    var y= 20;
    var z= x+y;

    console.log(z);
}
// with passing parameters.
function addtwonumbers(a,b){
    var c=a+b;
    console.log(c);

}
addtwonumbers(2,2);
addtwonumbers(4,4);
//function that takes an array as input and display all items of this array
function listArrayItems(arr) {
    for (var i = 0; i < arr.length; i++) {
        console.log(i, arr[i])
    }
}
var colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink'];
listArrayItems(colors);
//output
/*
0 'red'
1 'orange'
2 'yellow'
3 'green'
4 'blue'
5 'purple'
6 'pink' */
//I can even add one or more conditions, such as:
function listArrayItems(arr) {
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] == 'red') {
            console.log(i*100, "tomato!")
        } else {
            console.log(i*100, arr[i])
        }
    }
}
/* output
0 'tomato!'
100 'orange'
200 'yellow'
300 'green'
400 'blue'
500 'purple'
600 'pink'*/
// letter finder
function letterFinder(word, match) {
    for(var i = 0; i < word.length; i++) {
        if(word[i] == match) {
            //check if the current characater, word[i], is equal to the match
            console.log('Found the', match, 'at', i)
        } else {
            console.log('---No match found at', i)
        }
    }
}

letterFinder("test", "t")
/*output 
Found the t at 0
---No match found at 1
---No match found at 2
Found the t at 3
*/