var L = parseInt(readline());
var H = parseInt(readline());
var texte = readline().toUpperCase().split("");

var alphabet = [];
for (var i = 0; i < H; i++) {
    var ROW = readline();
    alphabet.push(ROW);
}

var correspondance = {};
var liste_lettre = [];
for (var idx = 0; idx < 91 - 65; idx += 1) {
    var elem = idx + 65;
    correspondance[String.fromCharCode(elem)] = idx;
    liste_lettre.push(String.fromCharCode(elem));

}
correspondance[(91 - 65) + 1] = "?";

var liste_indice = [];
for (var i = 0; i < texte.length; i += 1) {
    elem = texte[i];
    for (var idx = 0; idx < liste_lettre.length; idx += 1) {
        if (elem === liste_lettre[idx]) {
            var passage = true;
            break;
        } else {
            var passage = false;
        }
    }
    if (passage === true) {
        liste_indice.push(correspondance[elem]);
    } else {
        liste_indice.push(26);
    }
}

for (var i = 0; i < alphabet.length; i += 1) {
    liste = alphabet[i];
    liste3 = []
    for (var index = 0; index < liste_indice.length; index += 1) {
        idx = liste_indice[index];
        var liste2 = [];
        for (var nb = 0; nb < L; nb += 1) {
            liste2.push(liste[(idx*L)+nb]);
        }
        liste3.push(liste2.join(""))
    }
    print(liste3.join(""));
}
