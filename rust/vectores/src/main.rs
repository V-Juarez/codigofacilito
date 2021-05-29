fn main() {

                //    0   1   2 -> macro
    //let mut vector = vec![1, 2, 3];

// estructura
    let mut vector: Vec<i32> = Vec::new();


    //incrementar los elementos
    vector.push(1);
    vector.push(2);
    vector.push(3);
    vector.push(4);
    vector.push(5);

    //Agregar elemento
    vector.insert(0, -1);
    vector.insert(1, 0);


    //eliminar elemento
    vector.remove(vector.len() -1);

    vector[0] = -10;

    let primer_vector = vector[0];
    //let ultimo_vector = vector[ vector.len() -1];
    let ultimo_vector = vector.pop().unwrap();       // option

    println!("El valor del vector es: {:?}", vector);

    println!("El valor es: {}", primer_vector);
    println!("El valor es: {}", ultimo_vector);
}
