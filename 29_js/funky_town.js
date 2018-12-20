// Team Fishies - Vincent Chi, Johnson Li
// SoftDev1 pd8
// K29 -- Sequential Progression II: Electric Boogaloo
// 2018-12-19W

var fibonacci = (n) => {
    return fibHelp(1, 0, n);
}

// Helper for fibonacci
var fibHelp = (startNum, sumSoFar, numTimes) => {
    if (numTimes == 0){
        return sumSoFar;
    }
    return fibHelp(startNum + sumSoFar, startNum, numTimes - 1);
}

var gcd = (a, b) => {
    if(b == 0){
        return a;
    }
    return gcd(b, a % b);
}

var students = ["Bob", "Tim", "Kevin", "John", "Sally"];
var randomStudent = () => {
    var randomIndex = Math.floor(Math.random() * students.length);
    return students[randomIndex];
}

var fibButton = document.getElementById("fib");
var fibNum = document.getElementById("fib-num");
var fibResult = document.getElementById("fib-result");
fibButton.addEventListener("click", () => {
	console.log(fibonacci(fibNum.value));
    fibResult.innerHTML = `result: ${fibonacci(fibNum.value)}`;
});

var gcdButton = document.getElementById("gcd");
var gcdNum0 = document.getElementById("gcd-num0");
var gcdNum1 = document.getElementById("gcd-num1");
var gcdResult = document.getElementById("gcd-result");
gcdButton.addEventListener("click", () => {
	//console.log(gcd(gcdNum0.value,gcd.Num1.value));
    gcdResult.innerHTML = `result: ${gcd(gcdNum0.value, gcdNum1.value)}`;
});

var studentBut = document.getElementById("rand-student");
var student = document.getElementById("student");
studentBut.addEventListener("click", () => {
	console.log(randomStudent());
    student.innerHTML = `random student: ${randomStudent()}`;
})