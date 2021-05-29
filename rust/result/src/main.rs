/*enum Result<T, E> {
    Ok(T),      //valores de cualquir tipo
    Err(E)      //cuando existe un error
}
*/

#[derive(Debug)]
enum ErrorDivision {
    DivisionPorCero,
    DivisionNegativos
}

fn division(numero1: i32, numero2: i32) -> Result<i32, ErrorDivision> {
    if numero2 == 0 {
        return Err(ErrorDivision::DivisionPorCero);
    }
    if numero1 < 0 || numero2 < 0 {
        return Err(ErrorDivision::DivisionNegativos);
    }

    Ok(numero1 / numero2)
}

fn main() {

    let resultado = division(20, 25); //Result

    // unwrap, unwrap_or y expec

    // let valor = resultado.unwrap();
    // println!("El resultado es: {}", valor);

    let valor = resultado.unwrap_or(5);
    println!("El resultado es: {}", valor);

    // let valor = resultado.expect("No es posible dividir por 0");
    // println!("El resultado es: {}", valor);

    // match resultado {
    //     Ok(valor) => println!("El resultado es: {}", valor),
    //     Err(ErrorDivision::DivisionPorCero) => {
    //         println!("El error es por intentar dividir entre 0");
    //     }
    //     Err(ErrorDivision::DivisionNegativos) => {
    //         panic!("El error es por intentar dividir con numeros negativos");
    //     }
    //}

}
