// class A{
//     #field = 10
//     set_field(val){
//         this.field = val
//     }

//     getField(){
//         return this.#field;
//     }
// }

// let a = new A(10);
// a.set_field(15);
// console.log(a);

// function a1() {
//     setTimeout(() => console.log(1), 1000);
//     console.log(2);
//     setTimeout(() => console.log(3), 0);
//     console.log(4);
// }

// a1();


// class A {
//     static field = 10;
// }

// let a = new A();
// a.field = 999919929;
// let b = new A();
// b.field = 9999;
// console.log(A.field);

console.log('a');

setTimeout(() => {
    Promise.resolve().then(() => {console.log('b')});
}, 100);

function c() {
    setTimeout(() => {
        console.log('c');
    }, 500)
}

setTimeout(() => {
    console.log('d')
}, 1000)

c();