import java.util.*

fun main(args : Array<String>) {
    val input = Scanner(System.`in`)
    val b = input.nextLine().split("0")

    var maxOne = 1
    for (idx in 0..b.size-2) {
        maxOne = maxOf(maxOne, b[idx].length + b[idx+1].length + 1)
    }

    print(maxOne)
}
