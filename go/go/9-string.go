package main

import "fmt"
import "reflect"


func main() {

	// var curso string = "Curso Profesional de Go!"  // 1

	// var curso = "Curso Profesional de Goo!"  // 2

	curso := "Cruso profesional de Go!"				//3

	longitud := len(curso)

	fmt.Println(curso, longitud)

	primerCaracter := curso[0]  // char => uint*
	ultimoCaracter := curso [ len(curso) - 1 ]

	fmt.Println(primerCaracter)
	fmt.Println(reflect.TypeOf(primerCaracter))

	fmt.Printf("%c\n", primerCaracter)
	fmt.Printf("%c\n", ultimoCaracter)
}