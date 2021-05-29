struct Rectangulo {
    ancho: u32,
    alto: u32
}

fn area(rectangulo: &Rectangulo) -> u32 {
    rectangulo.ancho * rectangulo.alto
}

fn main() {
    //Ownsership
/*
    * Cada valor en Rust tiene su propio Ownsership.
    * solo puede existir un Ownsership a la vez.
    * Si un Ownsership sale del alcance, el valor se descartara.
*/


    let rectangulo = Rectangulo { ancho:10, alto:20 };

    // Los argumentos son pasados mediante prestamos, prestamos por referencia agregamos &
    let resultado = area(&rectangulo);

    // Los objetos que se almacenan en HEAP
    let nuevo_rectangulo = rectangulo;

    let x = 10; //stack
    let y = x;

    println!("{}", x);
    println!("{}", y);

    println!("El area de rectangulo es: {}", resultado);
    println!("El ancho y el alto del rectangulo es: {} - {}", nuevo_rectangulo.ancho, nuevo_rectangulo.alto);

}
