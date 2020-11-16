package main

import "fmt"

func main() {
    var n int
    fmt.Scan(&n)
    
    conv := make(map[string]byte)
    for i := 0; i < n; i++ {
        var b string
        var c byte
        fmt.Scan(&b, &c)
        conv[b] = c
    }
    var s string
    fmt.Scan(&s)

    word := make([]byte, 0)
    pb, pr := 0, 1
    for pr <= len(s) {
        for key, value := range conv {
            if key == s[pb:pr] {
                word = append(word, value)
                pb = pr
            }
        }
        pr++
    }
    
    if pr - pb > 1 {
        fmt.Println("DECODE FAIL AT INDEX", pb)
    } else {
        fmt.Println(string(word))
    }
}
