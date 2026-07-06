//eg:
let arr1=[10,20,30,40]
let arr2=[...arr1];
arr2.push(50);
console.log(arr1);
console.log(arr2);  
//eg3:
let frontend=["html","css"]
let backend=["node","express"]
let fullstack=[...frontend,...backend]
console.log(fullstack)