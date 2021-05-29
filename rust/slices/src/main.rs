fn main() {
    // Slices -> Heap
    // Arrays -> stack

    let mensaje = String::from("Hola mundo, desde el curso de Rust!");

    //let hola = &mensaje[0..4];    // [star..end]
    let hola = &mensaje[..4];
    let resto_mensaje = &mensaje[4..];
    let mensaje_completo = &mensaje[..];

    println!("El mensaje es: {}", mensaje);
    println!("El slice es: {}", hola);
    println!("El slice es: {}", resto_mensaje);
    println!("El slice es: {}", mensaje_completo);
}
