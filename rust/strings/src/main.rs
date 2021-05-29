fn main() {
    // str -> Stack
    // String ->  Heap

    //str
    let variable_str = "Hola, soy un tipo str";


    //let variable_string = String::new(); //""
    //new form
    let mut variable_string = String::from("Hola soy un String");

    variable_string.push(',');
    variable_string.push(' ');
    variable_string.push('H');
    variable_string.push('O');
    variable_string.push('L');
    variable_string.push('A');
    variable_string.push(' ');

    variable_string.push_str("Estamos en el curso de CodigoFacilito.");

    let nuevo_string = "Hola, soy una cadena".to_string(); //str

    let igual = nuevo_string == "Hola, soy una cadena".to_string();
    let diferentes = nuevo_string != "Hola, soy una cadena".to_string();



    println!("El str es: {}", variable_str);
    println!("El String es: {}", variable_string);
    println!("El String es: {}", nuevo_string);
    println!("El String son iguales: {}", igual);
    println!("El String son diferentes: {}", diferentes);
}
