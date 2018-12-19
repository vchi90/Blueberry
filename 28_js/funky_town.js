 // azrael - Jason Tung and Vincent Chi
 // SoftDev1 pd8
 // K28 -- Sequential Progression
 // 2018-12-18


var fib=function fibonacci(n){
  if (n == 0){
    return 0;
  }
  else if (n == 1 || n == 2){
    return 1;
  }
  else{
    return fibonacci(n-1) + fibonacci(n-2);
  };
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
