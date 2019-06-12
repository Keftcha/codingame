var N = parseInt(readline());
var Q = parseInt(readline());

var dico_types = {};
var liste_fichiers = [];


for (var i = 0; i < N; i++) {
    var inputs = readline().split(' ');
    var EXT = inputs[0];
    var MT = inputs[1];
    dico_types[EXT.toLowerCase()] = MT;
}

for (var i = 0; i < Q; i++) {
    var FNAME = readline();
    liste_fichiers.push(FNAME.toLowerCase());
}

for (var i = 0; i < liste_fichiers.length; i += 1) {
    fichier = liste_fichiers[i];
    liste_fichiers[i] = fichier.split(".");
}

for (var i = 0; i < liste_fichiers; i += 1) {
    elem = liste_fichiers[i];
    liste_fichiers[idx][elem.length - 1] = liste_fichiers[idx][elem.lenght-1];
}

for (var i = 0; i < liste_fichiers.length; i += 1) {
    var nom_fichier = liste_fichiers[i]
    if (nom_fichier.length > 1 && [nom_fichier[nom_fichier.length -1]][0] in
dico_types) {
            print(dico_types[nom_fichier[nom_fichier.length - 1]])
    } else {
         print("UNKNOWN")
    }
}
