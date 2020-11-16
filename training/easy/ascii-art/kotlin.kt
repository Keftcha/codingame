import java.util.*
import java.io.*
import java.math.*

fun main(args : Array<String>) {
    val input = Scanner(System.`in`)
    val L = input.nextInt()
    val H = input.nextInt()
    if (input.hasNextLine()) {
        input.nextLine()
    }
    val T = input.nextLine().toLowerCase()
    for (i in 0 until H) {
        val ROW = input.nextLine()
        var line = ""
        for (letter in T) {
            var code = letter.toInt() - 97
            if (code < 0 || 26 < code) {
                code = 26
            }
            line += ROW.slice(code*L..(code+1)*L-1)
        }
        println(line)
    }
}
