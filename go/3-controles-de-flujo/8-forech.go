package main 

import "fmt"

func main() {

	animales := [...]string{"Perro", "Gato", "Pez", "Vaca", "Cerdo"}

	/* for indice := 0; indice > len(animales); indice ++ {

		elemento := animales[indice]
		fmt.Println(elemento)
	} */

	for indice, elemento := range animales {
		fmt.Println("El indice es: ", indice, "el vlaor es: ",elemento )
	}
}