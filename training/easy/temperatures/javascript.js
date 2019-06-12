var n = parseInt(readline());
var temps = readline();

var temperature = Number.MAX_VALUE

temps = temps.split(" ")

if ( n === 1 ) {
    if (Number((temps[0]) === -273)) {
        temperature = -273
    } else if (Number(temps[0]) === 5526) {
        temperature = 5526
    } else {
        temperature = Number(temps[0])
    }
} else if ( n > 0) {
    for ( var idx = 0; idx < n; idx += 1) {
        if (Math.abs(Number(temps[idx])) === Math.abs(temperature)) {
            if (Number(temps[idx]) < 0 && temperature < 0) {
                temperature = Number(temps[idx])
            } else if (Number(temps[idx]) > 0 || temperature > 0) {
                temperature = Math.abs(Number(temps[idx]))
            }
        } else if (Math.abs(Number(temps[idx])) < Math.abs(temperature)) {
            temperature = Number(temps[idx])
        }
    }
} else {
    temperature = 0
}

print(temperature)
