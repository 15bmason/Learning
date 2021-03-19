package main

import (
	"os"
)

func main() {

	file, err := os.OpenFile("newFile", os.O_APPEND, 0600)

	if err != nil {
		panic(err)
	}
	//data := "This is me"
	for i := 0; i < 5; i++ {
		file.WriteString("Hello\n")
	}
	file.Close()

}
