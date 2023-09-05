
var sideA = 1;
var sideB = 2;
var sideC = 3;

if (sideA == sideB == sideC)
{
    console.log("Equilateral Triangle")
}
else if(sideA == sideB || sideA == sideC || sideB == sideC)
{
    console.log("Isosceles")
}
 else {
    console.log("Scalene Triangle")
 }