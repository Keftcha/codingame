const n: number = parseInt(readline());
var inputs: string[] = readline().split(' ');

let pertes: number = 0
let vmax: number = -1
let vmin: number = -1

for (let i = 0; i < n; i++) {
    const v: number = parseInt(inputs[i]);
    
    if (vmax == -1 || vmax < v){
        vmax = v
        vmin = v
        continue
    }
    if (vmin <= v){continue}
    vmin = v
    pertes = Math.min(pertes, vmin - vmax)
}

console.log(pertes);
