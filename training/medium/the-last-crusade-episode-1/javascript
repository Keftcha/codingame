var inputs = readline().split(' ');
var W = parseInt(inputs[0]); // number of columns.
var H = parseInt(inputs[1]); // number of rows.
terrain = [];
for (var i = 0; i < H; i++) {
    var LINE = readline(); // represents a line in the grid && contains W
integers. Each integer represents one room of a given type.
    LINE = LINE.split(" ")
    terrain.push(LINE)
}
var EX = parseInt(readline()); // the co||dinate along the X axis of the exit
(not useful f|| this first mission, but must be read).

// game loop
while (true) {
    var inputs = readline().split(' ');
    var XI = parseInt(inputs[0]);
    var YI = parseInt(inputs[1]);
    var POS = inputs[2];

    var x = XI
    var y = YI

    if (terrain[y][x] == "1" || terrain[y][x] == "3" || terrain[y][x] == "7" ||
terrain[y][x] == "8" || terrain[y][x] == "9" || terrain[y][x] == "12" ||
terrain[y][x] == "13") {y += 1}
    else if (POS == "TOP" && (terrain[y][x] == "4" || terrain[y][x] == "10")){x
-= 1}
    else if (POS == "TOP" && (terrain[y][x] == "5" || terrain[y][x] == "11")){x
+= 1}
    else if (POS == "LEFT" && (terrain[y][x] == "2" || terrain[y][x] == "6")){x
+= 1}
    else if (POS == "LEFT" && (terrain[y][x] == "5")){y += 1}
    else if (POS == "RIGHT" && (terrain[y][x] == "2" || terrain[y][x] ==
"6")){x -= 1}
    else if (POS == "RIGHT" && (terrain [y][x] == "4")){y += 1}

    print(String(x) + " " + String(y));
}
