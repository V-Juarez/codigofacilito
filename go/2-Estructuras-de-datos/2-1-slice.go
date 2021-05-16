package main

import "fmt"

func main() {

	meses := []string {"Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre"}


	//  Un puntero 

	//  una Longitud
	//  una capacidad

	longitud := len(meses)
	capacidad := cap(meses)

	fmt.Printf("La longuitud es: %v, La capacidad es: %v\n", longitud, capacidad, meses)

	meses = append(meses, "Octubre")	// si la estructura e encuentra en su capacidad maxima se gnera un nuevo arreglo
	meses = append(meses, "Novienbre")
	meses = append(meses, "Diciembre")

	longitud = len(meses)
	capacidad = cap(meses)

	fmt.Printf("La longuitud es: %v, La capacidad es: %v\n", longitud, capacidad, meses)
}