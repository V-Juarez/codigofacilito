package main

import "os"
import "fmt"
import "bufio"
import "strings"

var reader *bufio.Reader


func crearUsuario() {
	fmt.Println("Usuario creado exitosamente!")
}

func listarUsuario() {
	fmt.Println("Listado de usuarios!")
}

func actualizarUsuario() {
	fmt.Println("Usuarios actaulizado exitosamente!")
}

func eliminarUsuario() {
	fmt.Println("Usuario eliminado exitosamente!")
}


func readLine() string {
	

	if option, err := reader.ReadString('\n'); err != nil {
		panic("No es posible obtner el valor!")
	} else {
		return strings.TrimSuffix(option, "\n")
	}

}


func main() {


	var option string

	reader = bufio.NewReader(os.Stdin)

	for {
		fmt.Println("A) Crear")
	fmt.Println("B) Listar")
	fmt.Println("C) Actualizar")
	fmt.Println("D) Eliminar")

	fmt.Println("Ingresa una opcion valida: ")

	option = readLine()

	if option == "quit" || option == "q" {
		break
	}


	switch option {
		case "a", "crear":
			crearUsuario()
		case "b", "listar":
			listarUsuario()
		case "c", "actualizar":
			actualizarUsuario()
		case "d", "eliminar":
			eliminarUsuario()	
		default:
			fmt.Println("Opcion no valida!")
		}
	}

	fmt.Println("Adios.")
}