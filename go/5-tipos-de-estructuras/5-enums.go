package main

import "fmt"


type UserType int 

const (
	Teacher UserType = 1
	Student UserType = 2
)

type User struct {
	Username string
	Type UserType
}

func main() {


	eduardo := User { Username: "Eduardo", Type: Student }
	uriel := User { Username: "Uriel", Type: Teacher }

	fmt.Println(eduardo)
	fmt.Println(uriel)

	if eduardo.Type == Student {
		fmt.Println("El usuario", eduardo.Username, "es un estudiante")
	}
}