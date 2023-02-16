function pow(x, n){
    let res = x;

    for(let i=1; i<n; i++){
        res *=x;
    }
    return res;
}

let x = prompt('The value of x:', '');

let n = prompt('The value of n:', '');

if(n>1){
    alert(pow(x, n));
}
else {
    alert('Only natural values of n!');
}