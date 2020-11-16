const L: number = parseInt(readline());
const H: number = parseInt(readline());
const T: string = readline().toLowerCase();

for (let i = 0; i < H; i++) {
    const ROW: string = readline();
    let line = ""
    for (const letter of T) {
        let code = letter.charCodeAt(0)-97
        if (code < 0 || 26 < code) {
            code = 26
        }
        line += ROW.slice(code*L, (code+1)*L)
    }
    console.log(line)
}
