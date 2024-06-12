// 1 Function
//Function Declaration

// function greet(name) {
//     console.log('Привіт - ', name)
// }

// //Function Expression

// const greet2 = function greet2(name) {
//     console.log('Привіт2 - ', name)
// }

// greet('Maryna')
// greet2('Maryna')

// console.log(typeof greet)
// console.dir(greet)

// 2 Anonime function
// let counter = 0
// const interval = setInterval(function() {
//     if (counter === 5) {
//         clearInterval(interval) // clearTimeout
//     } else {
//     console.log(++counter)
//     }
// } , 1000)

// 3 Arrow function
// function greet(name) {
//     console.log('Привіт - ', name)
// }

// const arrow = (name) => {
//     console.log('Привіт - ', name)
// } 

// arrow('Machine')

function makeNegative(num) {
    if (num>0) {
      return console.log('-'+num)
  }
    else { 
      return console.log(num)
  }// Code?
  }

makeNegative('-1')
 