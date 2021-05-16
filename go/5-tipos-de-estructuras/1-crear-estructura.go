package main

import "fmt"

type User struct {
	Name string   // Atributos
	Email string
}

func main() {
	
	
	// var cody User	// Objeto

	// cody.Name = "Cody"
	// cody.Email = "info@codigofacilito.com"

	// cody := User { Name: "Cody", Email: "info@codigofacilito.com"}

	Name := "Cody"
	Email :=  "info@codigofacilito.com"

	cody := User {Name, Email}

	fmt.Println(cody.Name)
	fmt.Println(cody.Email)
}