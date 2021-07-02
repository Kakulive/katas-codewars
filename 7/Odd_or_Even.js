// Given a list of integers, determine whether the sum of its elements is odd or even.

// Give your answer as a string matching "odd" or "even".

// If the input array is empty consider it as: [0] (array with a zero).

function oddOrEven(array) {
    if (array.length == 0){
        return "even";
    }
    let sumi = 0;
    for (let i = 0; i < array.length; i++) {
        sumi += array[i];
    }
    if (sumi%2 == 0) {
        return "even";
    } else {
        return "odd";
    }
 }