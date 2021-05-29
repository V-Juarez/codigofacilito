fn main() {

        // loop

        let mut contador = 0;

        loop {
            contador += 1;
            //println!("Hola, nos encontramos en un ciclo infinito.");
            println!("Contador: {}", contador);

            if contador >= 10 {
                break;
            }
        }
}
