package main

import "fmt"


func modificarVariable(parametro string) {

	fmt.Println("Valor acutal: ", parametro)
	parametro = "Nuevo curso de Go!!!"
	fmt.Println("Nuevo valor: ", parametro)

	fmt.Printf("%p\n", &parametro)
}

func main() {
	

	var curso = "Curso Profesional de Go!"

	modificarVariable(curso)
	fmt.Println(curso)
		fmt.Printf("%p\n", &curso)
}