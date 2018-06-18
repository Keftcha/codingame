var width = parseInt(readline()); // the number of cells on the X axis
var height = parseInt(readline()); // the number of cells on the Y axis
var grille = [];
for (var i = 0; i < height; i++) {
    var line = readline(); // width characters, each either 0 or .
    grille.push(line);
}

var colone = 0;
var ligne = 0;
var nb_colone = width;
var nb_ligne = height;

var liste_neuds = [];

for (var i = 0; i < nb_ligne; i += 1) {
    for (var idx = 0; idx < nb_colone; idx += 1) {
        if (grille[i][idx] === "0") {
            liste_neuds.push([idx, i]);
        }
    }
}

printErr("Lites neuds: ", liste_neuds)

for (var i = 0; i < liste_neuds.length; i += 1) {
    var neud = liste_neuds[i];
    var affiche = [];
    affiche = affiche.concat(neud);

    var index = i + 1;
    var passage = true;
    while (index < liste_neuds.length) {
        if (neud[1] === liste_neuds[index][1]) {
            affiche = affiche.concat(liste_neuds[index]);
            passage = false;
            break;
        }
        index += 1;
    }
    if (passage === true) {
        affiche = affiche.concat([-1, -1]);
    }

    var index2 = i + 1;
    var passage2 = true;
    while (index2 < liste_neuds.length) {
            printErr("ici", neud[0], liste_neuds[index2][0])
        if (neud[0] === liste_neuds[index2][0]) {
            affiche = affiche.concat(liste_neuds[index2]);
            passage2 = false;
            break;
        }
        index2 += 1;
    }
    if (passage2 === true) {
        affiche = affiche.concat([-1, -1]);
    }
    print(affiche.join(" "));
    printErr(affiche.join(" "));
}
