var liste = []
var n = parseInt(readline());
var inputs = readline().split(' ');
for (var i = 0; i < n; i++) {
    var v = parseInt(inputs[i]);
    liste.push(v);
}

var perte = 0;
var max;
var min;

for (var i = 0; i < n; i += 1) {
    if (max === undefined || max < liste[i]) {
        max = liste[i];
        min = liste[i];
        continue;
    }
    if (min <= liste[i]) {
        continue;
    }
    min = liste[i];
    var diff = min - max;
    if (diff < perte) {
        perte = diff
    }
}

print(perte);
