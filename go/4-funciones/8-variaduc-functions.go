package main

import "fmt"

// Variadic function
func promedio(calificaciones ...int) int {

	var promedio, suma int


	for _, calificacion := range calificaciones {
		suma = suma + calificacion
		// fmt.Println(calificacion)
	}

	promedio = suma / len(calificaciones)

	return promedio
}

func main() {

	// Variadic Function
	// fmt.Println("Hola", "MUndo", "Desde el curso", "Profesional", "de Go!!")

	resultado := promedio(10, 8, 7, 10, 9, 7)
	fmt.Println("Promedio: ", resultado)
}