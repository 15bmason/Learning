package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {

	var wg sync.WaitGroup // Just a counter
	wg.Add(1)             // Says theres one go routine

	go func() {
		count("First")
		wg.Done() // Decrements the counter by 1
	}() // This creates a function and calls it imediately like a lambda

	wg.Wait() // Waits for the counter to be 0

}

func count(thing string) {
	for i := 1; i <= 5; i++ {
		fmt.Println(i, thing)
		time.Sleep(time.Millisecond * 500)
	}
}
