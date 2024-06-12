//Practic
// Task 1

// const filterNums = (arr, n = 0, how = 'greater') => {
//     return arr.filter(el => how == 'less' / el < n : el > n);
// }

const filterNums = (arr, num = 0, compare = "greater") => {
    let newArray;
    if (compare === "greater") {
            newArray = arr.filter(elem => elem > num);
    } else {
            newArray = arr.filter(elem => elem < num);
        }
        return newArray;
    
};


filterNums([-1, 2, 4, 0, 55, -12, 3], 11, 'greater');  //[ 55]


