// 1 Змінні

// var name = 'Company'  ///Don'used nowadays
// const firstName = 'Dmytro'
// // const lastName = 'Jack'
// const age = 50

// name = 'Feodal'

// age = 28

// console.log (firstName)
// console.log (age)

// 3 Конкантинація

// console.log("Ім'я чоловіка: " + firstName + ', а возрастаст человіка:' + age)
// alert("Ім'я чоловіка: " + firstName + ', а возрастаст человіка:' + age)


// const lastName = prompt ("Ввести ім'я")
// alert(firstName + ' ' + lastName )



// 3 Оператори
// let currentYear = 2020
// const birthYear = 1993

// const age = currentYear - birthYear


// console.log(currentYear--)
// console.log(currentYear)


// 4 Типи данних

// 5 Priority of operators

// const fullAge =26
// const birthYear = 1993
// const currentYear = 2020

// const ifFullAge = currentYear - birthYear <= fullAge

// console.log(ifFullAge)
// console.log(fullAge)



// 6 Decompose Conditional


// const courseStatus = 'fail' // ready, fail, pending 

// if (courseStatus === 'ready') {
//     console.log('Курс готовий і можна його проходити')
    
// } else if (courseStatus === 'pending') {
//     console.log('Курс поки в процесі розробки')
// } else {
//     console.log("Курс не получився")
// }

// const num1 = 42
// const num2 = '42' // string 

// console.log(num1===num2) /// Test with type date are with using '==='

// const isReady = true

// if (isReady === true) {
//     console.log('Все готове!')
// }


// const isReady = false

// // Тернарний вираз

// isReady ? console.log('Все гтове!') : console.log('Все готове!')


// 7 Boolean logic

// https://developer.mozilla.org/ru/docs/Web/JavaScript/Guide/Expressions_and_Operators#%D0%BB%D0%BE%D0%B3%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5_%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80%D1%8B

// 8 Function

// function calculateAge(year) {
//     return 2020-year
// }


// // console.log(calculateAge( 1996 ))


// function logInfoAbout(name, year) {
//     const age = calculateAge(year) 

//     if (age > 0 ) {
//         console.log('Чоловік по імені ' + name + ' зараз має років ' + age)
//     }else {
//     console.log('Взагаліто це вже майбутнє')
//     }
// }

// logInfoAbout('Dmytro','1996')
// logInfoAbout('Dmytro','2022')

// 9 Масиви 

// const cars = ['Мерс', 'Беха', 'Дімітро']
// // console.log(cars)

// // const cars = new Array ('Мерс', 'Беха', 'Дімітро', 'Форд')
// console.log(cars)

// console.log(cars[1])
// console.log(cars.length)

// cars[0] = 'Porsche'
// console.log(cars)


// 10 Cycle
// const cars = ['Мерс', 'Беха', 'Дімітро']

// // for (let i = 0; i < cars.length; i++) {
// //     const car = cars[i]
// //     console.log(car)
// // }

// for (let car of cars) {
//     console.log(car)
// }

// 11 Object

// const person = {
//     firstName: 'Dmytro',
//     lastName: 'Machine',
//     year: '1993',
//     languages: ['Ru','En','De'],
//     greet: function() {
//         console.log('greet from person')
//     }
// }

// console.log(person.firstName)
// console.log(person['lastName'])
// const key = 'languages'
// console.log(person[key])
// person.hasWife = true
// person.isProgrammer = true
// console.log(person)

// person.greet()


//12 Switch

// function learnJavaScript() {
//     let a = 'Apples'
//     let str
//     switch (a) {
//       case 'Apples':
//         str = 'I love ' + a
//         break
//       case 'Oranges':
//         str = 'I love ' + a
//         break
//       case 'Bananas':
//         str = 'I love ' + a
//         break
//       default:
//         str = 'I like other fruits'
//     }
//     return str
//   }