package main

import (
	"crypto/sha256"
	"fmt"
) // Crypto is the hashing module

func main() {
	x := "Hello There"
	y := sha256.Sum256([]byte(x))
	fmt.Println("Original:", x)
	fmt.Printf("SHA256: %x\n", y) // %x changes the output to lower case base 16, it does the ".hexdigest()" like in hashlib

}
