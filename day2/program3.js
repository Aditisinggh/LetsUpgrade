// Program to search for an element in a array of strings

let arr = ["Apple","Banana","Guava","Peach"]
let fruit = "Banana"
arr.forEach(function (a)
{
    if(a==fruit)
    {
        console.log(`${fruit} is in the fruit array`);
    }
})
