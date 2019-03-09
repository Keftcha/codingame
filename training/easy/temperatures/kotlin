import java.util.*

fun main(args : Array<String>) {
    val input = Scanner(System.`in`)
    val n = input.nextInt() // the number of temperatures to analyse
    var temps = ArrayList<Int>()
    for (i in 0 until n) {
        temps.add(input.nextInt()) // a temperature expressed as an integer ranging from -273 to 5526
    }
    
    println(
        if (n == 0) {
            0
        } else {
            var closest = temps[0]
            for (idx in 1..temps.size -1) {
                closest = if (Math.abs(closest) == Math.abs(temps[idx])) {
                    Math.max(closest, temps[idx])
                } else if (Math.abs(closest) > Math.abs(temps[idx])) {
                    temps[idx]
                } else {
                    closest
                }
            }
            closest
        }
    )
}
