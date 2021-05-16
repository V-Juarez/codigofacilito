package main

import "fmt"

func modificarValor(parametro *string) {
	*parametro = "Cambio de valor"
}


func main() {

	var curso = "Curso Profesional de Go!"
	fmt.Println("Antes de la funcion: ", curso)

	modificarValor(&curso) // referencia

	fmt.Println("Despues de la funcion: ", curso)
	// 
}