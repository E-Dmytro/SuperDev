// const cars = ['БМВ','Бентлі','Дімітро']
// // const people = [
// //     {name: 'Dmytro', budget:4200 },
// //     {name: 'Natalya', budget:3500 },
// //     {name: 'Taras', budget:2500 }
// // ]
// const fib = [1, 1, 2, 3, 5, 8, 13]

// // console.log(cars)

// // Function
// function addItemToEnd() {

// }

//Method
// cars.push('Порш')
// cars.unshift('Russian shib go nahuiy')
// console.log(cars)
// cars.shift()
// console.log(cars)
// const firstCar = cars.shift()
// const lastCar = cars.pop()
// console.log(firstCar)
// console.log(lastCar)

// console.log(cars.reverse())
// console.log(cars)


// const index = cars.indexOf('БМВ!')
// cars[index] = 'Porshe'
// console.log(cars)
//1
// let findedPerson
// for (const person of people) {
//     if (person.budget === 3500) {
//         findedPerson = person
//     }
// }

// console.log(findedPerson)


// const index = people.findIndex(function(person) {
//     return person.budget === 3500 
// })
// const person = people.find(function(person) {
//     return person.budget === 35002 
// // })
// console.log(person)


// console.log(person)

//2
// const person = people.find(person => {
//     return person.budget === 3500
// })
// console.log(person)

//3
// const person = people.find(person => person.budget === 3500)
// console.log(person)


// // Задача 1
// const text = ' Hi, we are learning JS'
// const reverseText = text.split(',').reverse().join()
// console.log(reverseText)

// console.log(cars.includes('Дімітро'))

// const upperCaseCars = cars.map(car => {
//     return car.toUpperCase()
// })

// const pow2 = num => num ** 2
// const sqrt = num => Math.sqrt(num)


// const pow2Fib = fib.map(pow2).map(Math.sqrt)
// console.log(upperCaseCars)
// console.log(cars)
// console.log(pow2Fib)

// const pow2 = num => num**2
// const pow2Fib = fib.map(pow2)
// const filteredNumbers = pow2Fib.filter(num => {
//     return num > 20
// })
// const filteredNumbers = pow2Fib.filter(num => num > 20)
// console.log(pow2Fib)
// console.log(filteredNumbers)

// const people = [
//     {name: 'Dmytro', budget:4200 },
//     {name: 'Natalya', budget:3500 },
//     {name: 'Taras', budget:1500 }
// ]

// const allBudget = people.reduce((acc, person) => {
//     if (person.budget > 2000){
//         acc += person.budget 
//     }
//     return acc
// }, 0)

// console.log(allBudget)


// const allBudget = people
// .filter(person => person.budget > 2000)
// .reduce((acc, person) => {
//     acc += person.budget 
//     return acc
// }, 0)
    
// console.log(allBudget)

// function find_average(array) {
//     if (array.length === 0) {
//     return 0;
//     } else {
//       return array.reduce((sum,item)=>sum+=item)/array.length;
//     }
// }


// console.log(find_average([71,43,68,62,51,51,52,53,91,43,78,49,66,66]))

//Коли цифри в стрінзі  та коли в array потрібно виділити тільки цифри

// function filter_list(l) {
//     return l.filter(e => Number.isInteger(e));


// var numb = 12312214.124124124;
// numb = numb.toFixed(2)

// console.log(numb)

// function SeriesSum(n) {
//     let result = 0;
//     let reverage = 1;
//     for (let i = 0; i < n; i += 1) {
//       if (i === 0) {
//         result = 1;
//       } else {
//         reverage += 3;
//         result = result + (1 / reverage);
//       }
//     }
//     return result.toFixed(2);
//   };


//   console.log(SeriesSum(1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 ))