package main

import "fmt"


type User struct {
	Name string
	Email string
	Active bool
}

type Student struct {
	User User
	Id string
}

func main() {

	eduardo := User{ Name: "Eduardo", Email: "Eduardo@codigofacilito.com", Active: true }
	uriel := User{ Name: "Uriel", Email: "uriel@codigofacilito.com", Active: true }

	eduardoStudent := Student{ User: eduardo, Id: "f1f" }

	fmt.Println(uriel)
	fmt.Println(eduardoStudent.User.Active)

}