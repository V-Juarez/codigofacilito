/*
enum Option<T>{
    Some(T), -> El valor
    None -> La ausencia del algun valor
}
*/
/*

fn obtener_valor(bandera: bool) -> Option<String> {

    if bandera {
        Some(String::from("Soy un mensaje para la tupla some!"))
    } else {
        None
    }
}

fn main() {
    // Option -> Si existe o no algun valor.
    // Result -> Errores -> panic

    let resultado = obtener_valor(false); //Option

    // match resultado {
    //     Some(valor) => println!("El valor es: {}", valor),
    //     None => println!("No existe valor alguno")
    // }

    //unwrap ->intenta obtener lo que la tupla Some almacena
    //metodos -> unwrap, unwrap_or, expect
    let valor = resultado.expect("Se esperaba un String");            //unwrap_or("La tupla no almacena valor alguno".to_string());
    println!("El valor es: {}", valor);
}

*/
#[derive(Debug)]
struct User {
    username: String,
    password: String,
    email: String,
    edad: Option<u32>
}

fn main() {
    let usuario1 = User{
        username: String::from("Victor"),
        password: String::from("password"),
        email: String::from("victor@caodigofacilito.com"),
        edad:  None //Some(25)
    };

    println!("El usuario es: {:?}", usuario1);

    //let edad = usuario1.edad.unwrap(); //match

    match usuario1.edad {
        Some(edad) => println!("Su edad es: {}", edad),
        None => { },
    }



}
