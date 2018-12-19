 // azrael - Jason Tung and Vincent Chi
 // SoftDev1 pd8
 // K28 -- Sequential Progression
 // 2018-12-18

 var fib = (n) => {
     return fibHelp(1, 0, n);
 }

 // Helper for fibonacci
 var fibHelp = (startNum, sumSoFar, numTimes) => {
     if (numTimes == 0){
         return sumSoFar;
     }
     return fibHelp(startNum + sumSoFar, startNum, numTimes - 1);
 }

var gcd = (a,b)=> {
    if (b == 0){
        return a;
    };
    if (a < b){
        return gcd(b,a);
    };
    return (a-b,b);
};

var randomStudent = (list) =>{
  return list[Math.floor(Math.random()*list.length)];
};

var fibButton = document.getElementById("fib");
fibButton.addEventListener("click", () => {
  console.log(fib(5));
});
