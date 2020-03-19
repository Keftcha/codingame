package main

import "fmt"

func main() {
    var surfaceN int
    fmt.Scan(&surfaceN)
    
    for i := 0; i < surfaceN; i++ {
        var landX, landY int
        fmt.Scan(&landX, &landY)
    }
    for {
        var X, Y, hSpeed, vSpeed, fuel, rotate, power int
        fmt.Scan(&X, &Y, &hSpeed, &vSpeed, &fuel, &rotate, &power)
        
        if vSpeed < -39 {
             fmt.Println("0 4")
        } else {
             fmt.Println("0 0")
        }
    }
}
