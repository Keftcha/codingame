var N = parseInt(readline());
dictionaire = [];
for (var i = 0; i < N; i++) {
    var W = readline();
    dictionaire.push(W);
}
var lettres = readline().split("");

var mots_possible = [];

for (var i = 0; i < dictionaire.length; i += 1) {
    mot = dictionaire[i];
    var liste = [];
    for (var idx = 0 ; idx < lettres.length; idx += 1) {
        liste.push(lettres[idx]);
    }
    var passage = true;
    for (var idx = 0; idx < mot.length; idx += 1) {
        lettre = mot[idx];
        if (liste.includes(lettre)) {
            liste.splice(liste.indexOf(lettre), 1);
            continue;
        } else {
            passage = false;
            break;
        }
    }
    if (passage === true) {
        mots_possible.push(mot);
    }
}

var points = 0;
var mots = [];
for (var i = 0; i < mots_possible.length; i += 1) {
    mot = mots_possible[i];
    var pts = 0;
    for (var idx = 0; idx < mot.length; idx += 1) {
        lettre = mot[idx]
        if (["e", "a", "i", "o", "n", "r", "t", "l", "s",
"u"].includes(lettre)) {
            pts += 1;
        } else if (["d", "g"].includes(lettre)) {
            pts += 2
        } else if (["b", "c", "m", "p"].includes(lettre)) {
            pts += 3
        } else if (["f", "h", "v", "w", "y"].includes(lettre)) {
            pts += 4
        } else if (["k"].includes(lettre)) {
            pts += 5
        } else if (["j", "x"].includes(lettre)) {
            pts += 8
        } else if (["q", "z"].includes(lettre)) {
            pts += 10
        }
    }

    if (pts > points) {
        points = pts
        var index = i
    }
}

print(mots_possible[index])
