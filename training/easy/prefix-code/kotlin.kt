import java.util.*
import java.io.*
import java.math.*

fun main(args : Array<String>) {
    val input = Scanner(System.`in`)

    val conv = HashMap<String, String>()
    val n = input.nextInt()
    for (i in 0 until n) {
        val b = input.next()
        val c = input.nextInt()
        conv[b] = c.toChar().toString()
    }

    val s = input.next()
    var word = ""
    var pb = 0
    var pr = 1
    while (pr <= s.length) {
        for ((key, value) in conv) {
            if (key == s.slice(pb..pr-1)) {
                word += value
                pb = pr
            }
        }
        pr += 1
    }

    println (if(pr - pb > 1) "DECODE FAIL AT INDEX " + pb.toString() else word)
}
