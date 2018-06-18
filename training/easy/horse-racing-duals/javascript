var N = parseInt(readline());
liste_puissance = [];
for (var i = 0; i < N; i++) {
    var pi = parseInt(readline());
    liste_puissance[i] = pi;
}

var comparer_nombres = function(a, b) {
  return a - b;
}

liste_puissance.sort(comparer_nombres);
var difference = 100000000000000000000;
var idx;
for (idx = N; idx >=  0; idx -= 1) {
    if (difference > Math.abs(liste_puissance[idx] - liste_puissance[idx+1])) {
        difference = Math.abs(liste_puissance[idx] - liste_puissance[idx+1])
    }
}

print(difference);
