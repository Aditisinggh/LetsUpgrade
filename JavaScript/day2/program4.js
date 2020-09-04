//Program to display only elements containing 'a' in them from a array

let arr=["apple","blue","car","dog","fan","goat"]
arr.forEach(function (a)
{
    if(a.match('a'))
    {
        console.log(`${a} contains 'a'`);
    }
}
)
