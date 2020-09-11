function greatestCD(num1, num2) {
    if((typeof num1 != 'number') && (typeof num2 != 'number'))
        return false;
    num1 = Math.abs(num1);
    num2 = Math.abs(num2);
    while(num2) {
        var t = num2;
        num2 = num1 % num2;
        num1 = t;
    }
    return num1
}

// console.log(greatestCD(3, 4))

// 35 goes into 95 2 times,
// the remainder 35 X 2 is 70
// 95 - 70 = 25

// exercise 2------------

function reportCard(grade) {
    if (grade >= 90 && grade <= 100) {
        console.log('🤓');
    } 
    else if (grade >= 80 && grade <= 89) {
        console.log('👽'); 
    } 
    else if (grade >= 70 && grade <= 79) {
        console.log('💩');
    }
    else if (grade >= 60 && grade <= 69) {
        console.log('🙊');   
    }
    else if (grade >= 0 && grade <= 59) {
        console.log('💀');
    }
}

// reportCard(3)


// exercise 3-------------

function isLeapYear(year) {
    if (year % 4 == 0 || year % 400 == 0) {
        console.log('It is a leap year!');
    } else {
        console.log(false);
    }

}

// isLeapYear(1754);


// exercise 4------------

function pigLatin(string) {
    let vowels = ['a', 'e', 'i', 'o', 'u']
        if (vowels.includes(string[0])) {
            return string + 'way'
        } 
        else {
            let count = 0
            for (letters of string) {
                if (vowels.includes(letters)) {
                    count = string.indexOf(letters)
                    break
               }
            }

            return string.slice(count) + string.slice(0, count) + 'ay'
        }
    }



// console.log(pigLatin('apple'))

// exercise 5------------------

function isOddorEven(num) {
    if (num % 2 !== 0) {
        console.log('Weird');
    } 
    else if {
        
    }
}