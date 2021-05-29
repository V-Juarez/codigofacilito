fn main() {


    let numero: i32 = 55;

    let mensaje = match numero {
        // valor => sentencia / tarea,
        1 => "El numero es uno",    //println!("El numero es uno."),
        2 => "El numero es dos",    //println!("El numero es dos."),
        3 => "El numero es tres",    //println!("El numero es tres."),
        4 | 5 | 6  => "El numero se encuentra entre cuatro y seis",            //println!("El numero se encuentra entre cuatro y seis"),,
        7..=100 => {
            let mensaje = "El numero se evalua mediante un rango del 7 al 100";

            mensaje
                //{
                //println!("El numero es mayor o igual a 7");
                //rintln!("El numero se evalue mendiante un rango")
                //},
    }
        _ => "numero"//println!("{}", numero)// Default
    };

    println!("El resultado es: {}", mensaje);



        for numero in 1..31 {

            match (numero % 3, numero % 5) {
                (0, 0) => println!("Fizz Buzz"),
                (0, _) => println!("Fizz"),
                (_, 0) => println!("Buzz"),
                _ => println!("{}", numero) //(_, _)
            }
        }

}
