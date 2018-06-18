var r = parseInt(readline());
var l = parseInt(readline());

var liste = [r];

for (var i = 0; i < l - 1; i += 1) {
    var liste_suivante = [];
    var pointeur_rouge = 0;
    var pointeur_bleu = 0;
    while (pointeur_bleu < liste.length) {
        while (pointeur_rouge < liste.length && liste[pointeur_rouge] ===
liste[pointeur_bleu]) {
            pointeur_rouge += 1;
        }
        liste_suivante = liste_suivante.concat([pointeur_rouge - pointeur_bleu,
liste[pointeur_bleu]])
        pointeur_bleu = pointeur_rouge
    }
    liste = liste_suivante
}
print(liste.join(" " ))
