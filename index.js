 //This is my first java script code
 console.log('Hello World');
  
 //variables
 //store data temporarily in a code
 
 let name = 'Lynn';
 console.log(name);

 //They cant be a researved key word let,if,else,voir etc
 //They should be meaningful
 //They cant start with a number
 //They cant contain a space or hyphen
 //They are case sensitive


//Constants
const interestRate = 0.2;
console.log(interestRate); 

//primitive values

let age = 24; //number literal
let LastName = 'Amoit'; //string literal
let isApproved = true; //boolean literal
let lastname = null; //clearing a value of a variable
let Firstname = undefined
//Dynamic typing
//type of a variable can easily be changed

//Checking the data type usingtypeof function
typeof name

name = 1
 typeof name

 //An object is an object in real life
 let person = {
    name: 'Lynn',
    age: 24,
    sex : 'Female'

 };

 //Changing the name of the person in the object
 //Dot notation
 person.name = 'Hellen';
 console.log(person);

 //Bracket notation
 person['name'] = 'Mary';
 console.log(person.name);

 //Arrays
 //stores lists and different types of data
 let selectedcolors = ['red','blue'];
 selectedcolors[2] = 3;
 console.log(selectedcolors[0]); //to specifify a color at a specific index
 console.log(selectedcolors.length);
 
//Functions
//performs a task or calculates a value
//name is a parameter
function greet(name,age){
    console.log('Hello' +  name + '' + age);
    

}
//John is an argument
greet('John', 13);
greet('Mary', 24)

//calculations function
function square(number){
    return number * number;

}

square(2);

