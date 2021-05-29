use std::io;  //libreria

fn main() {
    println!("Ingrese el nombre de usuario");

    let mut username = String::new();  // metodi statico -> de vuelve un striing vacio ""


    // Result -> exito o error
    io::stdin().read_line(&mut username); // referencia

    let username = username.trim();

    println!("Ingresa la edad del usuario");

    let mut edad = String::new();

    io::stdin().read_line(&mut edad);

    //Result
    let edad = edad.trim();

    let edad: i32 = edad.parse().unwrap();

    println!("Hola {} con edad {}", username, edad);


}
