const n: number = parseInt(readline())
let conv = new Map()
for (let i = 0; i < n; i++) {
    var inputs: string[] = readline().split(' ')
    const b: string = inputs[0]
    const c: number = parseInt(inputs[1])
    conv.set(b, String.fromCharCode(c))
}

const s: string = readline()
let pb = 0
let pr = 1
let word = ""
while (pr <= s.length) {
    conv.forEach((v, k) => {
        if (k == s.slice(pb, pr)) {
            word += v
            pb = pr
        }
    })
    pr++
}

console.log(pr - pb > 1 ? ("DECODE FAIL AT INDEX " + pb) : word)
