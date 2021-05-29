fn main() {

    // let <nombre de la variable> = <El valor>
    // let <nombre de la variable>: <T> = <El valor>
    // let mut <nombre de la variable>:i = <El valor>
    /*
        Este es un comentario de muchas lineas de
        codigo
    */

        const VALOR: i32 =10;           //constantes en rust en mayuscula, tipo de dato y el valor almacenar

        let mut numero_uno = 10;
        let numero_dos: i32 = 34;

        numero_uno = 100;

        let resultado = numero_uno + numero_dos + VALOR;


        println!("El resultado es: ({} + {} + {}): {}", numero_uno, numero_dos, VALOR, resultado);


}
