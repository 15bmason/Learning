package main

import (
	"fmt"
)

func main() {

	c := make(chan string, 2)
	c <- "hello"
	c <- "world"
	c <- "there" // Deadlock error since the channel already is full

	msg := <-c
	fmt.Println(msg)
	msg = <-c
	fmt.Println(msg)

}
