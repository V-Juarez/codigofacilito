fn main() {

    let mut valor: i32 = 10; // inmutabl

    //valor = 20;

    println!("El valor de la variable es: {}", valor);

    let valor = 20; // shadowing

    println!("El valor de al variable es: {}", valor);

    let valor = false;

    println!("El valor de la variable es: {}", valor);
}
