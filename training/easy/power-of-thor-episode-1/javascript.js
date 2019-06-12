var inputs = readline().split(' ');
var lightX = parseInt(inputs[0]);
var lightY = parseInt(inputs[1]);
var initialTX = parseInt(inputs[2]);
var initialTY = parseInt(inputs[3]);

var idx_x = 0;
var idx_y = 0;

while (true) {
    var remainingTurns = parseInt(readline());
    var direction = [];
    var deplacement_x = Math.abs(lightX - initialTX)
    var deplacement_y = Math.abs(lightY - initialTY)

    if (idx_y < deplacement_y) {
        if (initialTY < lightY) {
            direction.push("S")
        }
        if (initialTY > lightY) {
            direction.push("N")
        }
        idx_y += 1
    }

    if (idx_x < deplacement_x) {
        if (initialTX < lightX) {
            direction.push("E")
        }
        if (initialTX > lightX) {
            direction.push("W")
        }
        idx_x += 1
    }

    print(direction.join(""))
}
