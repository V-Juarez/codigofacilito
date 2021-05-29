fn main() {


    let mensaje = "Hola, soy una variable en el bloque main.";

    {   // juego de sentencias anidodos, al llegar su alcance esta es destruida
        //shadowing
        let mensaje = "Soy una variable en el bloque anidado";
        println!("Hola desde un segundo bloque!");

        println!("{}", mensaje);

        let mensaje_dos = "Hola, soy una variable en un bloque anidado";

        // este mensaje fuera del bloque, deja de funcionar.
        println!("{}", mensaje_dos);
    }

    println!("{}", mensaje);


// bloque anidado
        let resultado = {
            println!("Hola, nos encontramos en un bloque anidado");

            let variable: i32 = 200;

            println!("{}", variable);

            variable    // retornando su valor -> a partir de un bloque
        };

        println!("El valor de resultado es: {}", resultado);



// calificacion
        let calificacion: i8 = 10;
        let mut mensaje = String::new();

        let mensaje = if calificacion == 10{
//            mensaje = String::from("Felicitaciones, aprobastes la materia.  !!!");
            String::from("Felicitaciones, aprobastes la materia.  !!!")

        } else{
            //mensaje = String::from("Necesitas estudiar mas");
            String::from("Necesitas estudiar mas")
        };

        println!("{}", mensaje);
}
