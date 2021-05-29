fn main() {
    //Bloque limita el scope de una variable
    let mensaje = "Hola, soy una variable del bloque main";

    println!("Bloque 1: {}", mensaje);

    {   //Bloque 2

        let mensaje = "Hola, soy una variable del bloque 2";
        println!("Bloque 2: {}", mensaje);

        { //Bloque 3 -> el alcance de las variables va a ser destruida al terminar.

            println!("Bloque 3: {}", mensaje);  //?

            let resultado = 10 + 20;

            println!("EL resultado es: {}", resultado);
        }
    }

    let mensaje = String::from("Hola, soy una variable para prestamo.");

    {
        let prestamo = &mensaje; //prestamos -> se mueve

        mensaje = String::("Cambio de valor");
        println!("{}", prestamo);   //Freezing -> mensaje
    }

    println!("{}", mensaje);
}
