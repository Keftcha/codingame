import java.util.*

fun main(args : Array<String>) {
    val input = Scanner(System.`in`)
    val n = input.nextInt()
    
    var pertes = 0
    var vmax = -1
    var vmin = -1
    
    for (i in 0 until n) {
        val v = input.nextInt()
        
        if (vmax == -1 || vmax < v) {
            vmax = v
            vmin = v
            continue
        }
        if (vmin <= v) continue
        vmin = v
        pertes = minOf(pertes, vmin - vmax)
    }

    println(pertes)
}
