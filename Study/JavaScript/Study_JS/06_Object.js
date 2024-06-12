const person = {
    name: 'Dmytro',
    age: 25,
    isProgrammer: true,
    laguages: ['ru','en','de'],
    //'complex key':'Complex Value',
    //['key_'+(1+3)]: 'Computed Key',// key_4
    greet() {
        console.log('greet from person')
    },
    info() {
        // console.log('this:',this)
        console.info('Інформація про чоловіка по імені', this.name)
    }
}

// console.log(person.name)
// const ageKey = 'age'
// console.log(person['age'])
// console.log(person['complex key'])
// console.log(person)
// person.greet()

// person.age++
// person.laguages.push('sp')
// console.log(person)
// // person['key_4'] = undefined
// delete person['key_4']

// console.log(person)
// console.log(person['key_4'])

// const name = person.name
// const age = person.age
// const laguages = person.laguages



// console.log(name, age, laguages)

// const {name, age: personAge=10, laguages} = person

// console.log(name, personAge, laguages)

// console.log(person)

// for (let key in person) {
//     if (person.hasOwnProperty(key)) {
//         console.log('key:', key)
//         console.log('value:',person[key])
//     }
// }

// const keys = Object.keys(person)
// // console.log(keys)
// keys.forEach((key) => {
//     console.log('key:', key)
//     console.log('value', person[key])
// })


// Object.keys(person).forEach((key) => {
//     console.log('key:', key)
//     console.log('value', person[key])
// })

//Context 
// person.info()

// const logger = {
//     keys(obj) {
//         console.log('Object Keys: ', Object.keys(obj))
//     }
// }

// logger.keys(person)


const logger = {
    keys() {
        console.log('Object Keys: ', Object.keys(this))
    },   
    keysAndValues(){
        //"key":
        Object.keys(this).forEach(key => {
            console.log(`"${key}": ${this[key]}`)
        })
    }
}

// const bound = logger.keys.bind(person)
// bound()

// const bound = logger.keys.bind(person)
// bound()

// logger.keys(person)
// const bound = logger.keys.bind(logger)
// bound()

// logger.keys.call(person)

