fn main() {

    let numeros: [i32; 5] = [1, 2, 3, 4, 5];

    for numero in numeros.iter() {
        println!("El valor de numero: {}", numero);
    }

    for numero in 1..101 {
        println!("{}", numero);
    }

    //Fizz Buzz
    for numero in 1..101 {
        
        if numero % 3 == 0 && numero % 5 == 0 {
            println!("Fizz Buzz");
        } else if numero % 3 == 0 {
            println!("Fizz");
        } else if numero % 5 == 0 {
            println!("Buzz");
        } else {
            println!("{}", numero);
        }
    }

}
