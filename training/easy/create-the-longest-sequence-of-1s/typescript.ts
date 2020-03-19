const b: string[] = readline().split("0")

let maxOne = 1
for (let idx = 0; idx+1 < b.length; idx += 1) {
    maxOne = Math.max(maxOne, b[idx].length + b[idx+1].length + 1)
}

console.log(maxOne)
