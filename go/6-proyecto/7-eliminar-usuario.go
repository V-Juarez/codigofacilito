package main

import (
	"os"
  "fmt"
  "bufio"
  "strings"
  "strconv"
  "os/exec"
)

var reader *bufio.Reader

type User struct {
	id       int
	username string
	email    string
	age      int
}

var id int
var users map[int]User

func crearUsuario() {
	clearConsole()

	fmt.Print("Ingresa un valor para username: ")
	username := readLine()

	fmt.Print("Ingresa un valor para email: ")
	email := readLine()

	fmt.Print("Ingresa un valor para edad: ")
	age, err := strconv.Atoi(readLine())

	if err != nil {
		panic("NO es posible convertir de un string a un entero")
	}

	id++
	user := User{id, username, email, age}
	users[id] = user

	fmt.Println(users)

	fmt.Println("\n >>> Usuario creado exitosamente!\n")
}

func listarUsuario() {

	clearConsole()

	for id, user := range users {
		fmt.Println(id, "_", user.username)
	}

	fmt.Println("\n >>> Listado de usuarios!\n")
}

func actualizarUsuario() {

	clearConsole()


	fmt.Print("Ingresa el id del usuario a actualizar: ")
	id, err := strconv.Atoi(readLine())

	if err != nil {
		panic("No es posible convertir de un string a un entero.")
	}


	if _, ok := users[id]; ok {

    fmt.Print("Ingresa un nuevo username: ")
    username := readLine()
    fmt.Print("Ingresa un nuevo email: ")
    email := readLine()
    fmt.Print("Ingresa una nueva edad: ")
    age, err := strconv.Atoi(readLine())

    if err != nil {
        panic("No es posible convertir de un string a un entero")
    }

    fmt.Println("\nEste es el nuevo username: ", username)
    fmt.Println("Este es el nuevo email: ", email)
    fmt.Println("Este es la nueva edad: ", age)

    user := User { id, username, email, age }
    users[id] = user
	}

	fmt.Println("\n >>> Usuarios actaulizado exitosamente!\n ")
}

func eliminarUsuario() {
	clearConsole()

	fmt.Print("Ingresa el id del usuario a eliminar: ")
	id, err := strconv.Atoi(readLine())

	if err != nil {
		panic("No es posible convertir de un string a un entero.")
	}

	if _, ok := users[id]; ok {
		delete(users, id)
	}


	fmt.Println(">>> Usuario eliminado exitosamente!\n")
}

func clearConsole() {
	cmd := exec.Command("clear")
	cmd.Stdout = os.Stdout
	cmd.Run()
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
	users = make(map[int]User)
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